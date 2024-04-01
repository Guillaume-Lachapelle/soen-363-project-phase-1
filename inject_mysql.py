import mysql.connector

def inject_mysql():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password_here"
  )

  print('Connected to MySQL database.')
  cursor = mydb.cursor()
  cursor.execute("USE soen363_project_phase1;")

  print('Executing DML.sql...')
  with open('DML.sql', 'r') as file:
      for line in file:
          cursor.execute(line)

  mydb.commit()