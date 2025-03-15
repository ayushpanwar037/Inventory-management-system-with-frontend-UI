CREATE TABLE inventory (
    `item_no` INT,
    `InventoryID` INT PRIMARY KEY AUTO_INCREMENT,
    `quantity` INT CHECK (quantity < 15),
    FOREIGN KEY (`item_no`) REFERENCES items(`item_no`)
);

-- Inserting all items from the items table into the inventory table with quantities
INSERT INTO inventory (`item_no`, `quantity`) VALUES
-- iPhone Series
(10, 10), (11, 8), (12, 6), (13, 12), (14, 5), (15, 9),
-- Samsung S Series
(20, 10),
-- Samsung A Series
(21, 7),
-- PlayStation Series
(30, 14), (31, 6), (32, 8), (33, 11), (34, 4),
-- ROG Monitor Series
(40, 2), (41, 11), (42, 7),
-- ROG Laptop Series
(50, 5), (51, 9), (52, 14), (53, 8), (54, 3), (55, 10), (56, 6), (57, 13),
-- MSI Laptop Series
(60, 7), (61, 5), (62, 12), (63, 9), (64, 4),
-- ROG Pre-built CPU
(70, 3),
-- MSI Pre-built CPU
(71, 8),
-- Lenovo Pre-built CPU
(72, 6),
-- Apple Pre-built CPU
(73, 11),
-- Strix Pre-built CPU
(74, 4);

