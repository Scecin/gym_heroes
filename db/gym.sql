DROP TABLE bookings;
DROP TABLE gym_classes;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (255),
    last_name VARCHAR (255),
    membership VARCHAR (100),
    state VARCHAR (100)
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    teacher VARCHAR(255),
    duration INT,
    capacity INT,
    peak_hour VARCHAR(100),
    state VARCHAR (100)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    --delete the rows from the child table automatically, when the rows from the parent table are deleted
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE
);

-- -- Create some members 
-- INSERT INTO members (first_name, last_name, membership, state) VALUES ('David', 'Mackenzie', 'Standard', 'Activate');
-- INSERT INTO members (first_name, last_name, membership, state) VALUES ('Anna', 'Douglas', 'Premium', 'Activate');
-- INSERT INTO members (first_name, last_name, membership, state) VALUES ('Mary', 'Thomson', 'Standard', 'Activate');

-- -- -- Create some classe 
-- INSERT INTO gym_classes (name, teacher, duration, capacity, peak_hour, state) VALUES ('BodyCombat', 'Linzi Draw', 45, 25, 'Peak hour', 'Activate');
-- INSERT INTO gym_classes (name, teacher, duration, capacity, peak_hour, state) VALUES ('Group Cycle', 'Nick Dickson', 45, 20, 'Peak hour', 'Activate');
-- INSERT INTO gym_classes (name, teacher, duration, capacity, peak_hour, state) VALUES ('Hatha Yoga', 'Judy Elliot', 50, 15, 'off-Peak hours', 'Activate');