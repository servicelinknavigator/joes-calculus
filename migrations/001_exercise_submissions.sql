-- Migratie 001: foto-upload + AI-nakijken van uitwerkingen
-- Voer dit uit in de Supabase SQL editor (eenmalig, op de bestaande database).

create table if not exists exercise_submissions (
  id           serial primary key,
  user_id      uuid not null references profiles(id) on delete cascade,
  exercise_id  int not null references exercises(id) on delete cascade,
  image_path   text,
  ai_verdict   text,
  ai_feedback  text,
  created_at   timestamptz not null default now()
);

alter table exercise_submissions enable row level security;

create policy "submissions select own or admin" on exercise_submissions for select
  using (auth.uid() = user_id or exists (select 1 from profiles p where p.id = auth.uid() and p.role = 'admin'));
create policy "submissions insert own" on exercise_submissions for insert
  with check (auth.uid() = user_id);
