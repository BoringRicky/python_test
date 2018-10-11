class Person(object):
    def run(self):
        print('Person can running')
    
        
class Student(Person):
    def run(self):
        print("Student run fast")



class Employee(Person):
    def run(self):
        print("Employee run slower")


p = Person()
p.run()
print('p 属于 Person' if isinstance(p,Person)  else 'p 不属于 Person')
print('---------------------\n')

p1 = Student()
p1.run()
print('p1 属于 Person' if isinstance(p1,Person)  else 'p1 不属于 Person')
print('p1 属于 Student' if isinstance(p1,Student)  else 'p1 不属于 Student')
print('---------------------\n')

p2 = Employee()
p2.run()
print('p2 属于 Person' if isinstance(p2,Person)  else 'p2 不属于 Person')
print('---------------------\n')


def run(person):
    person.run()

run(p)
run(p1)
run(p2)


