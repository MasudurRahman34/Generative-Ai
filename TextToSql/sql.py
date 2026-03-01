import sqlite3

##connnection
connection = sqlite3.connect("student.db")

##cursor to crud with database
cursor = connection.cursor()

table_info = """CREATE TABLE IF NOT EXISTS Student(name VARCHAR(25), class VARCHAR(25), section VARCHAR(25), marks INT);"""

cursor.execute(table_info)


student_data = [
    ("Rahim", "Nine", "A", 85),
    ("Karim", "Ten", "B", 78),
    ("Ayesha", "Eleven", "A", 92),
    ("Nusrat", "SSC", "C", 88),
    ("Tanvir", "HSC", "A", 90),
]

cursor.executemany(
    """INSERT INTO Student (name, class, section, marks) VALUES(?,?,?,?) """,
    student_data,
)


print("Data inserted")

data = cursor.execute("""SELECT * FROM Student""")

for row in data:
    print(row)

connection.commit()
connection.close()
