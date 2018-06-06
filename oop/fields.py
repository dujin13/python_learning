class Student(object):
    name = 'Student'

s = Student()
s.score = 90
print('s.name =', s.name)
print('Student.name =', Student.name)
s.name = 'Bob'
print('s.name =', s.name)
print('Student.name =', Student.name)
del s.name
print('s.name =', s.name)