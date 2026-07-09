/*
==========================================================
Retail Sales Data Warehouse
File: 01_database.sql
Description: Creates the RetailDW database
Author: Rayan Prabhu
==========================================================
*/

-- Remove the database if it already exists
DROP DATABASE IF EXISTS RetailDW;

-- Create a fresh database
CREATE DATABASE RetailDW
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Switch to the new database
USE RetailDW;

-- Verify the current database
SELECT DATABASE() AS CurrentDatabase;