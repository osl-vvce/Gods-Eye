import pymysql
import recognizer # import the recognizer python 

data = recognizer.id # retrieve the name when running recognizer python file
# Create a database and connection credentials 
hostname = 'hostname'
username = 'username'
passwd = 'password'
dbname = 'dbname'

# establish connection to database
myConnection = pymysql.connect( host=hostname, user=username, passwd=passwd, db=dbname )

mycursor = myConnection.cursor()

# Query to update the value of particular person
sql = "Update student set attendance ='P' where Name = %s"

# parameter for format specifier like %s
datatuple = (data)

# execute the sql query with parameters
mycursor.execute(sql,datatuple)

# save changes in database
myConnection.commit()

# print on console the number of rows affected in database
print(mycursor.rowcount,"record affected")

# Select all the data in database
mycursor.execute("Select * from student")

myresult = mycursor.fetchall()

# print the data present in the database to console/command line
for x in myresult:
    print(x)

# close connection
myConnection.close()



