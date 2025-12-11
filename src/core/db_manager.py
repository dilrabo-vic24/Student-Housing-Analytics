import pyodbc

class DBManager:
    def __init__(self, server, database):
        self.server = server
        self.database = database
    
    def _get_connection_string(self):
        return (
            'DRIVER = {ODBC Driver 17 for SQL Server};'
            f'SERVER = {self.server};'
            f'DATABASE = {self.database};'
            'Trusted_Connection=yes;'
        )
    def connect(self):
        return pyodbc.connect(self._get_connection_string())
    
    def _execute_select(self, query):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query)

            columns = [column[0] for column in cursor.description]

            results = []

            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))

            return results
        
    # 4 querries
    #1.  List of rooms and the number of students in each of them
    def get_rooms_with_student_counts(self):
        query = """
            SELECT r.name, COUNT(s.id) as student_count 
            FROM rooms r
            LEFT JOIN students s ON r.id = s.room_id
            GROUP BY r.id, r.name
            ORDER BY student_count DESC
        """
        return self._execute_select(query)

    #2.  5 rooms with the smallest average age of students
    def get_rooms_min_avg_age(self):
        query = """
            SELECT TOP 5 r.name, AVG(DATEDIFF(year, s.birthday, GETDATE())) as avg_age 
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id, r.name
            ORDER BY avg_age ASC
        """
        return self._execute_select(query)

    #3.  5 rooms with the largest difference in the age of students
    def get_rooms_max_age_diff(self):
        query = """
            SELECT TOP 5 r.name, 
            (MAX(DATEDIFF(year, s.birthday, GETDATE())) - MIN(DATEDIFF(year, s.birthday, GETDATE()))) as age_diff 
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id, r.name
            ORDER BY age_diff DESC
        """
        return self._execute_select(query)

    #4.  List of rooms where different-sex students live
    def get_mixed_sex_rooms(self):
        query = """
            SELECT r.name 
            FROM rooms r
            JOIN students s ON r.id = s.room_id
            GROUP BY r.id, r.name
            HAVING COUNT(DISTINCT s.sex) > 1
        """
        return self._execute_select(query)
