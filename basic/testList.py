#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['A', 'B', 'C']
print(classmates)
print("len =", len(classmates))
print("classmates[0] =", classmates[0])
print("classmates[1] =", classmates[1])
print("classmates[2] =", classmates[2])
print("classmates[-1] =", classmates[-1])
print("classmates[-2] =", classmates[-2])
classmates.append('D')
print("classmates =", classmates)
classmates.insert(1, 'Jeck')
print("classmates =", classmates)
classmates.pop()
print("classmates =", classmates)
classmates.pop(1)
print("classmates =", classmates)
classmates[1] = 'Mary'
print("classmates =", classmates)

L=['Apple', 123, True]
s = ['python', 'java', L, 'schema']
print("s = ", s)