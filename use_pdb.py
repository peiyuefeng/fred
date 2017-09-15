import pdb 

def fun(b):
        
    def a(b):
        a = '123'
        pdb.set_trace()
        a.replace('1','a')
        b = a
        print b
        return "i don't have time"
    a(b)

print fun('fuck')


