CREATE TABLE Customer_table (
    customer_ID INT PRIMARY KEY,
    name VARCHAR(255),
    contact_details VARCHAR(10),
    number_of_purchases INT,
    discount_given DECIMAL(10, 2)
);

-- Populate the table with 20 entries
INSERT INTO Customer_table (customer_ID, name, contact_details, number_of_purchases, discount_given)
VALUES
    (1001, 'John Smith', '1234567890', 8, 0.24),
    (1002, 'Jane Doe', '2345678901', 12, 0.36),
    (1003, 'Michael Johnson', '3456789012', 15, 0.45),
    (1004, 'Emily Williams', '4567890123', 10, 0.30),
    (1005, 'William Brown', '5678901234', 18, 0.54),
    (1006, 'Emma Jones', '6789012345', 7, 0.21),
    (1007, 'Daniel Miller', '7890123456', 14, 0.42),
    (1008, 'Olivia Davis', '8901234567', 6, 0.18),
    (1009, 'Matthew Garcia', '9012345678', 11, 0.33),
    (1010, 'Ava Rodriguez', '0123456789', 9, 0.27),
    (1011, 'Sophia Martinez', '9876543210', 17, 0.51),
    (1012, 'Ethan Hernandez', '8765432109', 20, 0.60),
    (1013, 'Isabella Lopez', '7654321098', 13, 0.39),
    (1014, 'Mia Gonzalez', '6543210987', 19, 0.57),
    (1015, 'James Perez', '5432109876', 16, 0.48),
    (1016, 'Alexander Wilson', '4321098765', 5, 0.15),
    (1017, 'Benjamin Moore', '3210987654', 10, 0.30),
    (1018, 'Harper Taylor', '2109876543', 14, 0.42),
    (1019, 'Evelyn Anderson', '1098765432', 11, 0.33),
    (1020, 'Charlotte Thomas', '0987654321', 20, 0.60);
