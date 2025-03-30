# # # #HOW TO CREATE A DATABASE
# import sqlite3
# # Connect to the SQLite database (or create it if it doesn't exist)
# conn = sqlite3.connect("sample.db")
# print("Database is created")
# # Create a table if it doesn't exist
# conn.execute('''CREATE TABLE IF NOT EXISTS sample (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);''')
# # Insert records into the table
# conn.execute("INSERT INTO sample(ID, NAME) VALUES (1, 'RAM')")
# conn.execute("INSERT INTO sample(ID, NAME) VALUES (2, 'SHYAM')")
# # Commit the changes to the database
# conn.commit()
# print("Records are created")
# # Close the database connection
# conn.close()



# # HOW TO PRINT THE DATA IN TABLE OF THE DATABASE
# import sqlite3
# conn=sqlite3.connect("sample.db")
# print("databse is created")
# cursor=conn.execute("select ID,NAME FROM Sample")
# for row in cursor:
#     print("ID",row[0])
#     print("NAME",row[1])
# print("data has been displayed")
# conn.close()


# #HOW TO UPDATE THE EXISTING DATA FROM DATABSE
# import sqlite3
# conn=sqlite3.connect("sample.db")
# print(" databse is created")
# conn.execute(" UPDATE SAMPLE set NAME='ASH' where ID=1")
# conn.commit()
# cursor=conn.execute("select * from sample")
# for row in cursor:
#     print("ID",row[0])
#     print("NAME",row[1])
# print("data has been displayed")
# conn.close()


# #DELETE A ROW FROM DATABASE
# import sqlite3
# conn=sqlite3.connect("sample.db")
# print(" databse is created")
# conn.execute("DELETE from sample where ID=2")
# conn.commit()
# print("total no of rows are deleted")
# cursor=conn.execute("select * from sample")
# for row in cursor:
#     print("ID",row[0])
#     print("NAME",row[1])
# print("data has been displayed")
# conn.close()


# ***#CREATE A MINI PROJECT OF LIUBRARY MANAGEMENT CONSISTING OF STUDENT DEATILS.
##DISPLAY THE CONTENTS OF STUDENTS
# import sqlite3
# conn=sqlite3.connect("librarymanagement.db")
# print("Database is created")
# conn.execute('''CREATE TABLE IF NOT EXISTS studentdata(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,YEAR INT NOT NULL)''')
# conn.execute("INSERT INTO studentdata (ID,NAME,YEAR) VALUES(1, 'ASH' ,8)")
# conn.execute("INSERT INTO studentdata (ID,NAME,YEAR) VALUES(2 ,'TUSHU' ,5)")
# conn.commit()
# print("Record created ")
# conn.close()


##how to display only on row
# import sqlite3
# conn=sqlite3.connect("librarymanagement.db")
# print("Database is created")
# cursor=conn.execute("SELECT * from studentdata")
# print(cursor.fetchone())  ##to fetch just one row
# print(cursor.fetchaall())   ##to fetch all rows
# conn.close()

#





