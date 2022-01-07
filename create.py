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
    CREATE TABLE python_company(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL
    );
    '''
)
print('Table created successfully!')
conn.commit()
conn.close()
