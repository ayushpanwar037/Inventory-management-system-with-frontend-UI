CREATE TABLE orders (
    `order_no` INT PRIMARY KEY AUTO_INCREMENT,
    `date_required` DATE,
    `date_completed` DATE
);

-- Inserting sample data into the table
INSERT INTO orders (`date_required`, `date_completed`) VALUES
('2024-03-01', '2024-02-25'),
('2024-03-05', '2024-03-03'),
('2024-03-10', NULL),
('2024-03-15', '2024-03-12'),
('2024-03-20', NULL),
('2024-03-25', NULL),
('2024-03-30', '2024-03-28'),
('2024-04-05', NULL),
('2024-04-10', '2024-04-08');
