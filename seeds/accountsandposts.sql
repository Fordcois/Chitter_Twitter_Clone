-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS cheeps;
DROP SEQUENCE IF EXISTS cheeps_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    emaiL VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name,email,username,password) VALUES ('Bruno Guimaraes','bruno.G@nufc.sa','Brun0G','password');
INSERT INTO users (name,email,username,password) VALUES ('Joelinton','joelinton@nufc.sa','J0el!nton','password');
INSERT INTO users (name,email,username,password) VALUES ('Alexander Issak','alex.i@nufc.sa','Is@k','password');
INSERT INTO users (name,email,username,password) VALUES ('Sven Botman','sven.b@nufc.sa','B0tm@n','password');
INSERT INTO users (name,email,username,password) VALUES ('Kieran Trippier','k.tripper@nufc.sa','222KTripps','password');

CREATE SEQUENCE IF NOT EXISTS cheeps_id_seq;
CREATE TABLE cheeps (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255),
    time_posted TIMESTAMP,
    poster_id int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO cheeps (content,time_posted,poster_id) VALUES ('Signed my new contract! Geordie until I die!','2023-03-14 01:01:00',1);
INSERT INTO cheeps (content,time_posted,poster_id) VALUES ('We got Bruno in the middle!!!!!','2023-03-14 01:01:00',2);
INSERT INTO cheeps (content,time_posted,poster_id) VALUES ('Smashing Work Today Lads! Absolutely destroyed PSG','2023-03-14 01:01:00',5);
INSERT INTO cheeps (content,time_posted,poster_id) VALUES ('Yohan Cayabye Who? Theres only one super sven botman','2023-03-14 01:01:00',4);
INSERT INTO cheeps (content,time_posted,poster_id) VALUES ('Fill the Gallowgate with Ikea? I can get us a discount!','2023-03-14 01:01:00',3);