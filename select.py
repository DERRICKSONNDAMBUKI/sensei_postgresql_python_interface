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
    SELECT * FROM python_company;
    '''
)
rows = cur.fetchall()
for row in rows:
    print('Id = ',row[0])
    print('Name = ',row[1])
    print('Address = ',row[2])
    print('Salary = ',row[3])
    print('\n')
    
print('Operation done successfully')
conn.close()