-- Joes Calculus App | Supabase schema (v1.0)
-- Voer dit uit in de Supabase SQL editor van een nieuw (of bestaand) project.

-- ── profiles ─────────────────────────────────────────────────────────────────
create table if not exists profiles (
  id         uuid primary key references auth.users(id) on delete cascade,
  email      text not null,
  name       text,
  role       text not null default 'student' check (role in ('admin', 'student')),
  created_at timestamptz not null default now()
);

-- Automatisch profiel aanmaken zodra een auth-user wordt aangemaakt
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, email, role)
  values (
    new.id,
    new.email,
    case when lower(new.email) = 'contact@slnsolutions.nl' then 'admin' else 'student' end
  )
  on conflict (id) do nothing;
  return new;
end;
$$ language plpgsql security definer;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- ── modules ──────────────────────────────────────────────────────────────────
create table if not exists modules (
  id          serial primary key,
  order_index int not null,
  title       text not null
);

-- ── chapters ─────────────────────────────────────────────────────────────────
create table if not exists chapters (
  id              serial primary key,
  module_id       int not null references modules(id) on delete cascade,
  chapter_number  int not null unique,     -- doorlopende nummering 1..47
  title           text not null,
  theory_content  text,                    -- markdown: de "vooraf"-uitleg
  summary         text,                    -- optionele afsluitende samenvatting
  is_placeholder  boolean not null default false  -- true = "binnenkort beschikbaar"
);

-- ── exercises ────────────────────────────────────────────────────────────────
create table if not exists exercises (
  id                 serial primary key,
  chapter_id         int not null references chapters(id) on delete cascade,
  order_index        int not null,          -- ook de "slot"/subcategorie: meerdere rijen per slot mogelijk
  difficulty         int not null default 1 check (difficulty between 1 and 3),
  question           text not null,           -- opgavetekst (markdown/LaTeX)
  hints              jsonb not null default '[]'::jsonb,  -- progressieve hints ("tijdens")
  full_solution      text not null,           -- volledige uitwerking met toelichting ("achteraf")
  answer_type        text not null default 'open' check (answer_type in ('numeric', 'expression', 'open')),
  correct_answer     text,                    -- indien automatisch controleerbaar
  is_ai_generated    boolean not null default false,  -- true = door AI gemaakte variant, niet de originele seed
  source_exercise_id int references exercises(id)     -- verwijst naar de originele opgave van dit slot
);

-- ── progress ─────────────────────────────────────────────────────────────────
create table if not exists progress (
  id          serial primary key,
  user_id     uuid not null references profiles(id) on delete cascade,
  chapter_id  int not null references chapters(id) on delete cascade,
  status      text not null default 'not_started' check (status in ('not_started', 'in_progress', 'completed')),
  updated_at  timestamptz not null default now(),
  unique (user_id, chapter_id)
);

-- ── exercise_attempts ────────────────────────────────────────────────────────
create table if not exists exercise_attempts (
  id               serial primary key,
  user_id          uuid not null references profiles(id) on delete cascade,
  exercise_id      int not null references exercises(id) on delete cascade,
  submitted_answer text,
  is_correct       boolean,
  hints_used       int not null default 0,
  created_at       timestamptz not null default now()
);

-- ── exercise_submissions ─────────────────────────────────────────────────────
-- Foto-uploads van uitwerkingen op papier, nagekeken door de AI (zie /exercise/<id>/upload)
create table if not exists exercise_submissions (
  id           serial primary key,
  user_id      uuid not null references profiles(id) on delete cascade,
  exercise_id  int not null references exercises(id) on delete cascade,
  image_path   text,                 -- pad in de "solution-uploads" Storage-bucket
  ai_verdict   text,                 -- 'correct' | 'incorrect' | 'unclear'
  ai_feedback  text,
  created_at   timestamptz not null default now()
);

-- ── tests (toetsen) ──────────────────────────────────────────────────────────
create table if not exists tests (
  id           serial primary key,
  chapter_id   int not null references chapters(id) on delete cascade,
  user_id      uuid not null references profiles(id) on delete cascade,
  status       text not null default 'in_progress' check (status in ('in_progress','completed')),
  score        int,
  total        int not null,
  created_at   timestamptz not null default now(),
  completed_at timestamptz
);

create table if not exists test_questions (
  id            serial primary key,
  test_id       int not null references tests(id) on delete cascade,
  order_index   int not null,
  question      text not null,
  full_solution text not null,
  verdict       text,
  ai_feedback   text
);

create table if not exists test_submissions (
  id                serial primary key,
  test_question_id  int not null references test_questions(id) on delete cascade,
  user_id           uuid not null references profiles(id) on delete cascade,
  image_path        text,
  ai_verdict        text,
  ai_feedback       text,
  created_at        timestamptz not null default now()
);

-- ── RLS ──────────────────────────────────────────────────────────────────────
alter table profiles              enable row level security;
alter table modules               enable row level security;
alter table chapters              enable row level security;
alter table exercises             enable row level security;
alter table progress              enable row level security;
alter table exercise_attempts     enable row level security;
alter table exercise_submissions  enable row level security;
alter table tests                 enable row level security;
alter table test_questions        enable row level security;
alter table test_submissions      enable row level security;

-- profiles: iedereen mag het eigen profiel lezen/updaten, admin mag alles lezen
create policy "profiles select own or admin" on profiles for select
  using (auth.uid() = id or exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'admin'));
create policy "profiles update own" on profiles for update
  using (auth.uid() = id);

-- modules/chapters/exercises: leesbaar voor elke ingelogde gebruiker (geen prive content)
create policy "modules select authenticated" on modules for select
  using (auth.role() = 'authenticated');
create policy "chapters select authenticated" on chapters for select
  using (auth.role() = 'authenticated');
create policy "exercises select authenticated" on exercises for select
  using (auth.role() = 'authenticated');

-- progress: eigen rijen, admin ziet alles
create policy "progress select own or admin" on progress for select
  using (auth.uid() = user_id or exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'admin'));
create policy "progress upsert own" on progress for insert
  with check (auth.uid() = user_id);
create policy "progress update own" on progress for update
  using (auth.uid() = user_id);

-- exercise_attempts: eigen rijen, admin ziet alles
create policy "attempts select own or admin" on exercise_attempts for select
  using (auth.uid() = user_id or exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'admin'));
create policy "attempts insert own" on exercise_attempts for insert
  with check (auth.uid() = user_id);

-- exercise_submissions: eigen rijen, admin ziet alles
create policy "submissions select own or admin" on exercise_submissions for select
  using (auth.uid() = user_id or exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'admin'));
create policy "submissions insert own" on exercise_submissions for insert
  with check (auth.uid() = user_id);

-- tests / test_questions / test_submissions
create policy "tests select own or admin" on tests for select
  using (auth.uid() = user_id or exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'admin'));
create policy "tests insert own" on tests for insert
  with check (auth.uid() = user_id);
create policy "tests update own" on tests for update
  using (auth.uid() = user_id);

create policy "test_questions select via test" on test_questions for select
  using (exists (
    select 1 from tests t where t.id = test_questions.test_id
    and (t.user_id = auth.uid() or exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'admin'))
  ));
create policy "test_questions insert via test" on test_questions for insert
  with check (exists (select 1 from tests t where t.id = test_questions.test_id and t.user_id = auth.uid()));
create policy "test_questions update via test" on test_questions for update
  using (exists (select 1 from tests t where t.id = test_questions.test_id and t.user_id = auth.uid()));

create policy "test_submissions select own or admin" on test_submissions for select
  using (auth.uid() = user_id or exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'admin'));
create policy "test_submissions insert own" on test_submissions for insert
  with check (auth.uid() = user_id);

-- ── seed: modules ────────────────────────────────────────────────────────────
insert into modules (id, order_index, title) values
  (1, 1, 'Calculus 1'),
  (2, 2, 'Calculus 2'),
  (3, 3, 'Calculus 3'),
  (4, 4, 'Lineaire algebra'),
  (5, 5, 'Differentiaalvergelijkingen')
on conflict (id) do nothing;
