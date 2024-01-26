# байэль тут 3
# инкапсуляция -- капсула

# уровни доступа
# публичный
# защищенный - protected _
# private скрытый __
# Абстракция

# h=Hum('name')
# h.Hi()



class Person(object):
    def __init__(self,firsname,lastname,age,money):
        self.first=firsname
        self.last=lastname
        self._age=age
        self.__money=money
    def __str__(self):
        return self.first

    def HI(self):
        print(f'Hi my name is {self.first} {self.last}\n'
              f'my old {self._age}')

    def kesh(self):
        print(self.__money)

firstd=Person('beka','qwerty',20,2020)
firstd.first='Бека'
firstd._age=10000
firstd.__money=0
firstd.age2=22
print(firstd,firstd.age2)
firstd.HI()
firstd.kesh()
firstd._Person__money=10
f='erty'
print(dir(firstd))
print(dir(f))
print(firstd)






class P2(Person):

    # def st(self):
    #     return super().__str()

    def __str__(self):
        return f' hi {super().__str__()}'



# p=P2('first')
# print(p)
# print(p.st())


