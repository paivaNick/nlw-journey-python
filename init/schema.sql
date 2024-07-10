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
  foreign key (trip_id) references trips(id)
)
