import requests
import sqlite3

con = sqlite3.connect('dogs.db')
cursor = con.cursor()

# print all breed in database

cursor.execute('SELECT * FROM dog_breeds')
rows = cursor.fetchall()
for row in rows:
    print(row)

#print total all rows

cursor.execute('''
    SELECT COUNT(*) AS total_row
    FROM dog_breeds
''')
result = cursor.fetchone()
print(f"Total rows: {result[0]}")

#print total breeds

cursor.execute('''
    SELECT COUNT(DISTINCT breed) AS total_breeds
    FROM dog_breeds;
''')
result = cursor.fetchone()
print(f"Total Breeds: {result[0]}")

#print total sub breeds

cursor.execute('''
    SELECT COUNT(*) AS total_sub_breeds
    FROM dog_breeds
    WHERE sub_breed IS NOT NULL;
''')
result = cursor.fetchone()
print(f"Total Sub_Breeds: {result[0]}")


#print top 5 most sub breeds

cursor.execute('''
    SELECT breed,COUNT(sub_breed) AS sub_breed_count
    FROM dog_breeds
    WHERE sub_breed IS NOT NULL
    GROUP BY breed
    ORDER BY sub_breed_count DESC
    LIMIT 5;
''')
result = cursor.fetchall()
print(f"Top 5 most sub_breeds:")
for breed, count in result:
    print(f"{breed}: {count}")


#print breed that have no sub breed

cursor.execute('''
    SELECT COUNT(*) AS no_sub_breeds_count
    FROM dog_breeds
    WHERE sub_breed IS NOT NULL;
''')
result = cursor.fetchone()
print(f"No_sub_breeds_count: {result[0]}")


con.close()