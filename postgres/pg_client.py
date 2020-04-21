import psycopg2

conn = psycopg2.connect("dbname=rainbow_database user=unicorn_user password=magical_password host=database")

cur = conn.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
res = cur.fetchone()
print(f'select result: {res}')

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
