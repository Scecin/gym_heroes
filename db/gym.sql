DROP TABLE bookings;
DROP TABLE gym_classes;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (255),
    last_name VARCHAR (255)
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    teacher VARCHAR(255),
    duration INT,
    capacity INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE
);