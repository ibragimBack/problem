# множественное наследование
# venv - модули библиотеки зависимости фреймворки пакеты

# модуль 3 встроенные #random = библиотека

# встроенный
from random import randint
print(randint(2,9))

from math import *
print(pi)

import math
print(math.nan)


# собственные модули

# внешние модули
# venv - виртуальная среда/ для скачивания модулей

# class A:
#     def __init__(self,b,c,d):
#         self._b=b
#         self._c=c
#         self._d=d
#
#     def get_point(self):
#         print(self._d,self._c,self._b)
#
#     def set_point(self,b,c,d):
#         self._b=b
#         self._c=c
#         self._d=d
#
#     @property
#     def point(self):
#         return  f"{self._d},{self._c},{self._b}"
#
#     @point.setter
#     def point(self,b,c,d):
#         self._b = b
#         self._c = c
#         self._d = d
#
#     @point.deleter
#     def point(self):
#         del self._b
#         del self._c
#         del self._d
#
# a = A('b','c',14)
# print(a.point)
# a.point=15
# print(a.point)
#
#
#
# class Hum:
#     def __init__(self,name1):
#         self.name1=name1
#
#     def run(self):
#         print(self.name1, 'run')
#
#
# hum1 = Hum('albus')
# hum1.run()
#
#
# class Hum3(Hum):...
#
# class SuperHum:
#     def __init__(self,name,superpower):
#         self.name=name
#         self.power=superpower
#
#     def run(self):
#         # super().run()
#         print(self.power)
#
# c=SuperHum('Albus','Mage')
# c.run()
#
#
# class Hum2(SuperHum,Hum3,Hum):
#     def __init__(self,name,superpower,name1):
#         SuperHum.__init__(self,name,superpower)
#         Hum.__init__(self,name1)
#
#     def run(self):
#         Hum.run(self)
#         SuperHum.run(self)
#
#
# h=Hum2('name1','super','name1')
# h.power='Rave'
# h.name2='q'
# h.run()
#
#
# # MRO - method resolution order
# print(Hum2.mro())