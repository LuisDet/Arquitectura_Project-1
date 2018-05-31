import pyodbc as db
from Company_Employees import Employee as em

conn = db.connect("driver={SQL Server Native Client 11.0}; server=localhost; database=Registrodb; trusted_connection=yes")
cur = conn.cursor()

def insert (emp):
	with conn:
		cur.execute("INSERT INTO empleado VALUES(?,?,?,?,?,?)",
			(emp.firstName, emp.lastName, emp.age, emp.address, emp.pay, emp.email))

def show (lastname):
	cur.execute("SELECT * FROM empleado where lastName = ?", (lastname))
	print(cur.fetchall()) 

def update(emp, pay):
	with conn:
		cur.execute("UPDATE empleado SET pay = ? where firstName = ? AND lastName = ?",
		(pay, emp.firstName, emp.lastName))

def delete(emp):
	with conn:
		cur.execute("DELETE FROM empleado WHERE firstName = ? and lastName = ?",
		(emp.firstName, emp.lastName))

emp_1 = em('Jose', 'Cabrera', 25, 'Autopista las americas', 150000)
emp_2 = em('Ana', 'Correa', 38, 'Los cacicasgos', 75000)
emp_3 = em('Fausto', 'Espinosa', 21, 'Autopista las americas', 25000)
emp_4 = em('Estefani', 'Peña', 27, 'Puñal parte atras', 68000)
emp_5 = em('Josefina', 'Cabrera', 32, 'Colinas de estrellas', 300000)



insert(emp_1)
insert(emp_2)
insert(emp_3)
insert(emp_4)
insert(emp_5)

show('Cabrera')
show('Espinosa')

update(emp_1, 10)
update(emp_3, 78500)

delete(emp_4) 

cur.close()
conn.close()
