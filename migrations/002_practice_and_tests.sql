-- Migratie 002: oneindig oefenen per opgave-slot, toetsfunctie, en
-- permanente upload-geschiedenis.
-- Voer dit uit in de Supabase SQL editor (eenmalig, op de bestaande database).

-- ── exercises: markering voor AI-gegenereerde varianten ─────────────────────
alter table exercises add column if not exists is_ai_generated boolean not null default false;
alter table exercises add column if not exists source_exercise_id int references exercises(id);

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

alter table tests             enable row level security;
alter table test_questions    enable row level security;
alter table test_submissions  enable row level security;

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
