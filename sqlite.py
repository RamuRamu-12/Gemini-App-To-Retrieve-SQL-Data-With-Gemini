import sqlite3


## Connect to SQLite
Connection=sqlite3.connect("classes.db")

# Create a cursor object to insert record,create table
cursor=Connection.cursor()

# Create the table
table_info="""
Create table CLASSES(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));


"""
cursor.execute(table_info)

# Inserting the records
cursor.execute('''Insert Into CLASSES values('Ram','App Developer','A')''')
cursor.execute('''Insert Into CLASSES values('Rakesh','Data Science','A')''')
cursor.execute('''Insert Into CLASSES values('Raj','Developer','C')''')
cursor.execute('''Insert Into CLASSES values('Ravi','App Developer','B')''')
cursor.execute('''Insert Into CLASSES values('Raju','Devops','A')''')
cursor.execute('''Insert Into CLASSES values('Rathin','App Developer','B')''')


# Display all the records
print("The Inserted Records are:")
data=cursor.execute("""Select * from CLASSES """)
for row in data:
    print(row)

# Commit the changes.
Connection.commit()
Connection.close()