/*
550. Game Play Analysis IV
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

The result format is in the following example.

 

Example 1:

Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Explanation: 
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
*/

-- # Write your MySQL query statement below

SELECT round(sum(sec_day_status) / count(*), 2) as fraction
FROM(
    SELECT max(second_day_of_first_login) as sec_day_status
    FROM(
        SELECT 
            a.player_id, a.event_date, b.next_day_of_first_login, 
            CASE
                WHEN datediff(a.event_date, b.next_day_of_first_login) = 0 then 1
                else 0
            END as second_day_of_first_login
        FROM Activity as a
        LEFT JOIN(
            SELECT player_id, event_date, date_add(min(event_date), interval 1 day) as next_day_of_first_login
            FROM Activity
            GROUP BY player_id 
        ) as b
            ON a.player_id = b.player_id
    ) as sub1
    GROUP BY player_id 
) as sbu2;