-- Tables
create table if not exists public.user_profile (
	id uuid primary key default gen_random_uuid(),
	date date not null,
	weight numeric,
	height numeric,
	age int,
	gender text,
	activity_level text
);

create table if not exists public.weight_log (
	id uuid primary key default gen_random_uuid(),
	date date not null,
	weight numeric
);

create table if not exists public.diet_log (
	id uuid primary key default gen_random_uuid(),
	date date not null,
	meal_type text,
	food_name text,
	calories numeric,
	protein numeric,
	carbs numeric,
	fat numeric
);

create table if not exists public.workout_log (
	id uuid primary key default gen_random_uuid(),
	date date not null,
	exercise_name text,
	duration_minutes int,
	calories_burned numeric
);

-- Enable Row Level Security
alter table public.user_profile enable row level security;
alter table public.weight_log enable row level security;
alter table public.diet_log enable row level security;
alter table public.workout_log enable row level security;

-- Simple permissive policies for a single-user personal app
-- If you later add auth, scope rows to auth.uid()
create policy "allow all select" on public.user_profile for select using (true);
create policy "allow all insert" on public.user_profile for insert with check (true);
create policy "allow all update" on public.user_profile for update using (true) with check (true);
create policy "allow all delete" on public.user_profile for delete using (true);

create policy "allow all select" on public.weight_log for select using (true);
create policy "allow all insert" on public.weight_log for insert with check (true);
create policy "allow all update" on public.weight_log for update using (true) with check (true);
create policy "allow all delete" on public.weight_log for delete using (true);

create policy "allow all select" on public.diet_log for select using (true);
create policy "allow all insert" on public.diet_log for insert with check (true);
create policy "allow all update" on public.diet_log for update using (true) with check (true);
create policy "allow all delete" on public.diet_log for delete using (true);

create policy "allow all select" on public.workout_log for select using (true);
create policy "allow all insert" on public.workout_log for insert with check (true);
create policy "allow all update" on public.workout_log for update using (true) with check (true);
create policy "allow all delete" on public.workout_log for delete using (true);
