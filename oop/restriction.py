class Student(object):

    def __init__(self, name, grade):
        self.__name = name;
        self.__grade = grade;

    def print_score(self):
        print('%s %s' % (self.__name, self.__grade))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 96)
print('bart =', bart)
bart.print_score()
print('bart.get_name =', bart.get_name())