SELECT r.name, COUNT(s.id) as student_count 
            FROM rooms r
            LEFT JOIN students s ON r.id = s.room_id
            GROUP BY r.id, r.name
            ORDER BY student_count DESC
            
SELECT TOP 5 r.name, AVG(DATEDIFF(year, s.birthday, GETDATE())) as avg_age 
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id, r.name
            ORDER BY avg_age ASC

SELECT TOP 5 r.name, 
            (MAX(DATEDIFF(year, s.birthday, GETDATE())) - MIN(DATEDIFF(year, s.birthday, GETDATE()))) as age_diff 
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id, r.name
            ORDER BY age_diff DESC
SELECT r.name 
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id, r.name
            HAVING COUNT(DISTINCT s.sex) > 1