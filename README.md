# Sensei PostgreSQL - Python Interface

### Installation
The PostgreSQL can be integrated with Python using psycopg2 module. sycopg2 is a PostgreSQL database adapter for the Python programming language. psycopg2 was written with the aim of being very small and fast, and stable as a rock. You do not need to install this module separately because it is shipped, by default, along with Python version 2.5.x onwards.
If you do not have it installed on your machine then you can use yum command to install it as
follows −
```
$ sudo apt-get install python-psycopg2
```
### API & Description
##### psycopg2.connect(database="testdb",user="postgres",password="my_password", host="127.0.0.1", port="5432")
This API opens a connection to the PostgreSQL database. If database is opened
successfully, it returns a connection object.
##### connection.cursor()
This routine creates a cursor which will be used throughout of your database
programming with Python.
##### cursor.execute(sql [, optional parameters])
This routine executes an SQL statement. The SQL statement may be parameterized (i.e., placeholders instead of SQL literals). The psycopg2 module supports placeholder using %s sign For example:
```
cursor.execute("insert into people values (%s, %s)", (who, age))
cursor.executemany(sql, seq_of_parameters)
```
This routine executes an SQL command against all parameter sequences or
mappings found in the sequence sql.
##### cursor.callproc(procname[, parameters])
This routine executes a stored database procedure with the given name. The
sequence of parameters must contain one entry for each argument that the
procedure expects.
##### cursor.rowcount
This read-only attribute which returns the total number of database rows that have
been modified, inserted, or deleted by the last last execute*().
##### connection.commit()
This method commits the current transaction. If you do not call this method,
anything you did since the last call to commit() is not visible from other database
connections.
##### connection.rollback()
This method rolls back any changes to the database since the last call to commit().
##### connection.close()
This method closes the database connection. Note that this does not automatically
call commit(). If you just close your database connection without calling commit()
first, your changes will be lost!
##### cursor.fetchone()
This method fetches the next row of a query result set, returning a single
sequence, or None when no more data is available.
##### cursor.fetchmany([size=cursor.arraysize])
This routine fetches the next set of rows of a query result, returning a list. An empty list is returned when no more rows are available. The method tries to fetch as many rows as indicated by the size parameter.
##### cursor.fetchall()
This routine fetches all (remaining) rows of a query result, returning a list. An empty list is returned when no rows are available.