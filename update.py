import psycopg2

conn = psycopg2.connect(
    database="testdb",
    user="postgres",
    password="@S3ns31;",
    host="127.0.0.1",
    port=5432
)
print("Opened database successfully!")

cur = conn.cursor()

cur.execute(
    '''
    UPDATE python_company SET salary = 25000.00 WHERE id = 1;
    '''
)
conn.commit
print('Updated {} rows\n'.format(cur.rowcount))

cur.execute(
    '''
    SELECT * FROM python_company;
    '''
)
rows = cur.fetchall()
for row in rows:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3])
    print('\n')
print('Operation done successfully!')
conn.close()
