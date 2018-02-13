drop table if exists;
create table entries (
	id int not null,
	title varchar(255) not null,
	text varchar(255)
	primary key(id)
);