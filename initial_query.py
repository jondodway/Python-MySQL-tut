import mysql.connectordb = mysql.connector.connect(	host = "localhost",	user="root",	passwd="root",	database="testdatabase"	)mycursor=db.cursor()mycursor.execute("CREATE TABLE Person(name VARCHAR(50) , age smallint UNSIGNED,personID SERIAL PRIMARY KEY )")#mycursor.execute("DESCRIBE Person")#for x in mycursor:	#print(x)