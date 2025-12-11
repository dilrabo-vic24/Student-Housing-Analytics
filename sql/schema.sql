create table rooms (
    id int primary key,
    name varchar(255) not null
);

create table students(
    id int primary key,
    name varchar(255) not null,
    birthday date not null,
    sex varchar(10) not null,
    room_id int not null foreign key (room_id) references rooms(id)
);