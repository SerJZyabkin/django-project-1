from django.db import models
import psycopg2

conn = psycopg2.connect(database="cabsbordb",  user="admin",  host="localhost",  password="admin")
cursor = conn.cursor()

cursor.execute("""SELECT * FROM cab_sbor_backend_productgroupentry""")

for record in cursor.fetchall():
    print(record)
conn.close()
