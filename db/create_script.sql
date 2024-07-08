#
# Optional Script
#

-- CREATE DATABASE
create database toby;

-- CREATE SCHEMA
create schema movies_collection;

-- TABLES
-- not using yet
create table movies_collection.app
(
	id int not null
		primary key,
	name varchar(50) null,
	constraint movie_app_name_uindex
		unique (name)
);

create table movies_collection.country
(
	id int not null
		primary key,
	name varchar(30) not null
);

create table movies_collection.director
(
	id int not null
		primary key,
	name varchar(100) not null,
	constraint director_name_uindex
		unique (name)
);

create table movies_collection.genre
(
	id int not null
		primary key,
	name varchar(150) not null,
	constraint genre_name_uindex
		unique (name)
);

create table movies_collection.movie
(
	id int not null
		primary key,
	title varchar(200) not null,
	release_year int null,
	age int null,
	imdb_rate float null,
	rotten_tomatoes_pctg int null,
	type int null,
	runtime float null,
	country_id int not null,
	genre_id int not null
);

create table movies_collection.movie_director
(
	id int not null
		primary key,
	movie_id int not null,
	director_id int not null
);

create table movies_collection.movie_genre
(
	id int not null
		primary key,
	movie_id int not null,
	genre_id int not null
);


-- COPY FROM S3
copy dip_de_usach.movies
from 's3://dip-de-2024/MoviesOnStreamingPlatforms_updated.csv'
access_key_id 'ACCESS_KEY'
secret_access_key 'SECRET_KEY'
csv
IGNOREHEADER 1
delimiter ','
TRUNCATECOLUMNS;

-- CREATE DATABASE USER
CREATE USER admin PASSWORD 'ABC1234567890.';
grant all on schema dip_de_usach to admin;