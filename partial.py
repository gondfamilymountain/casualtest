#!/usr/bin/env python
def sayhello(name):
   return "hello %s" % name

print sayhello('dongtui')


from functools import partial
sayhello2=partial(sayhello,'dicaprio')

print sayhello2()
