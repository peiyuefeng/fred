my_list = [1,2,3]
print dir(my_list)


print(type(''))
print(type([]))
print(type({}))
print(type(()))
print(type(dict))
print(type(3))

name="fred"
print(id(name))

from pprint import pprint
print '------------dir-------------------'
pprint(dir('bbbbbbbbbbaaaaaaaaaaaaaaaaaaaa'))

import inspect
print '------------inspect-------------------'
pprint(inspect.getmembers('bbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaa'))

