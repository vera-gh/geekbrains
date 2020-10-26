/* Задание 2.
 Создайте базу данных example, разместите в ней таблицу users, 
состоящую из двух столбцов, числового id и строкового name.
*/
-- создание базы данных
DROP DATABASE IF EXISTS example;
CREATE DATABASE example;
-- создание таблицы
DROP TABLE IF EXISTS example.users;
CREATE TABLE example.users (
id INT,
name VARCHAR(50)
);
/* Задание 3.
 Создайте дамп базы данных example из предыдущего задания, 
разверните содержимое дампа в новую базу данных sample.*/
DROP DATABASE IF EXISTS sample;
CREATE DATABASE sample;