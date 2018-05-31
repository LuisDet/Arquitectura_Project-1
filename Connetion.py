import sqlite3
from Company_Employees import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

#c.execute( "CREATE TABLE empleado( first text, last text, pay integer )" )

emp_1 = Employee('David', 'Jose', 4500)
emp_2 = Employee('Camile', 'Jose', 8500)

#c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})
#conn.commit()
#
#c.execute("INSERT INTO employee VALUES (?, ?, ?)", (emp_2.first, emp_2.last, emp_2.pay))
#conn.commit()
c.execute("SELECT * FROM employee where last = ?", ('Jose',))
print (c.fetchall())

c.execute("SELECT * FROM employee where last = :last", {'last': 'Andres'})
print (c.fetchall())

conn.commit()

conn.close()
        
