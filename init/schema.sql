create table if not exists 'trips' (
  id text primary key,
  destination text not null,
  start_date datetime,
  end_date datetime,
  owner_name text not null,
  owner_email text not null,
  status integer
);

create table if not exists 'emails_to_invite' (
  id text primary key,
  trip_id text,
  email text not null,
  foreign key (trip_id) references trips(id)
);

create table if not exists 'links' (
  id text primary key,
  trip_id text,
  link text not null,
  title text not null,
  foreign key (trip_id) references trips(id)
);

create table if not exists 'participants' (
  id text primary key,
  trip_id text not null,
  emails_to_invite_id text not null,
  name text not null,
  is_confirmed integer,
  foreign key (trip_id) references trips(id)
  foreign key (emails_to_invite_id) references emails_to_invite(id)
);

create table if not exists 'activities' (
  id text primary key,
  trip_id text not null,
  title text not null,
  occurs_at datetime,
  foreign key (trip_id) references trips(id)
);

