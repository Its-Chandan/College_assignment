import sqlite3

con = sqlite3.connect('employee1.db')
query = "SELECT * from employee"

#cur = con.cursor()
output= con.execute(query) 


for rec in output:
   print(rec)

con.close()
