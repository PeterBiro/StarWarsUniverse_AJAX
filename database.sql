DROP TABLE IF EXISTS users, planet_votes;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL);

CREATE TABLE planet_votes(
    id SERIAL PRIMARY KEY,
    planet_name VARCHAR(255),
    user_id INT,
    submission_time TIMESTAMP DEFAULT NOW());

ALTER TABLE planet_votes ADD CONSTRAINT user_id FOREIGN KEY (id) REFERENCES users (id);
