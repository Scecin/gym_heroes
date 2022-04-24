DROP TABLE gym;
DROP TABLE members;
DROP TABLE classes;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (255),
    last_name VARCHAR (255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    teacher VARCHAR(255),
    duration INT
);

CREATE TABLE gym (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE
);