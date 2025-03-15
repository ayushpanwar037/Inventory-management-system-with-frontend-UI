CREATE TABLE shipment (
    `shipment_no` INT PRIMARY KEY AUTO_INCREMENT,
    `shipment_date` DATE
);

-- Inserting sample data into the table
INSERT INTO shipment (`shipment_date`) VALUES
('2024-03-01'),
('2024-03-05'),
('2024-03-10'),
('2024-03-15'),
('2024-03-20'),
('2024-03-25'),
('2024-03-30'),
('2024-04-05'),
('2024-04-10');
