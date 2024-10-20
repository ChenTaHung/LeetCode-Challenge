/*
626. Exchange Seats
Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.
 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output: 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation: 
Note that if the number of students is odd, there is no need to change the last one's seat.
*/

# Write your MySQL query statement below
WITH oddsID AS (
    SELECT *, id + 1 as newid
    FROM Seat
    HAVING mod(id, 2) = 1
), evenID AS (
    SELECT *, id-1 as newid
    FROM Seat
    HAVING mod(id, 2) = 0
)
SELECT s.id, coalesce(coalesce(o.student , e.student), s.student) as student
FROM Seat as s
LEFT JOIN oddsID as o
    ON s.id = o.newid
LEFT JOIN evenID as e
    ON s.id = e.newid ;