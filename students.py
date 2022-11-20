import sqlite3
class Baza():
  def __init__(self,str_baz,str_view,tip_sql = 4):
    self.name_b = str_baz
    self.name_v = str_view
    self.tip = tip_sql 
    self.rec = []

  def get_val(self):
    try:
      connection = sqlite3.connect(self.name_b)
      cursor = connection.cursor()
      cursor.execute(self.name_v)
      if self.tip == 4:
        self.rec = cursor.fetchall()
      connection.commit()
      connection.close()
      return self.rec 
    except(Exception, sqlite3.Error) as error:
      print("Ошибка в получении данных", error)

rec_del = """ DROP table School; """
rec_crt = """CREATE TABLE School
(
School_Id INTEGER NOT NULL PRIMARY KEY,
School_Name TEXT NOT NULL,
Place_Count INTEGER NOT NULL
);"""
rec_ins = """INSERT INTO School (School_Id, School_Name, Place_Count)
VALUES
('1', 'Протон', 200),
('2', 'Преспектива', 300),
('3', 'Спектр', 400),
('4', 'Содружество', 500);
"""
rec_del = """ DROP table Students; """
rec_crt = """CREATE TABLE Students
(
Student_Id INTEGER NOT NULL PRIMARY KEY,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL
);"""
rec_ins = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);
"""

aa1 = Baza('teatchera.db',rec_del,1)
aa1.get_val()
aa1 = Baza('teatchera.db',rec_crt,2)
aa1.get_val()
aa1 = Baza('teatchera.db',rec_ins,3)
aa1.get_val()
rec = """
SELECT Student_Id,  Student_Name, sc.School_Id,School_Name
FROM School sc
JOIN Students st ON st.School_Id = sc.School_Id;
"""
sstr = input('Введите код студента: ')
rec = """
SELECT Student_Id,  Student_Name, sc.School_Id,School_Name
FROM School sc
JOIN Students st ON st.School_Id = sc.School_Id
WHERE Student_Id = """ + sstr + ';'

print('ID студента  Имя студента ID школы Название школы') 
aa1 = Baza('teatchera.db',rec,4)
