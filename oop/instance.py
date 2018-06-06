class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 96)
print('bart =', bart)
print('bart,name =', bart.name)
print('bart,score =', bart.score)
bart.print_score()
print('bart.grade =', bart.get_grade())

lisa = Student('Lisa', 59)
print('lisa.grade =', lisa.get_grade())