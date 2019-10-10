
#övning 506
def create_lock(password,phrase):
    def lock(code):
        if password == code:
            return phrase
        else:
            return "Fel Kod!"
    return lock
#övning 507
#(lambda x: x*2)(2)

#övning 508
#(lambda x,y: y**2+x**2)(2, 2)

#övning 509
#(lambda x: (lambda y: y+x))(5)(2)

#övning 510
def keep_if(predikat, string):
    if not string:
        return ""
    elif predikat(string[0]):
        return string[0]+keep_if(predikat,string[1:])
    else:
        return keep_if(predikat,string[1:])

#övning 511
def foreach(predikat, seq):
    return [predikat(seq[i]) for i in range(len(seq))]

#övning 512
def f(x):
      return x + 10
      
def g(y):
      return 2 * y + 7

def compose(f,g):
    def sammansatt(y):
        return f(g(y))
    return sammansatt

#övning 513
def apply_repeatedly(fn, n, x): 
    res = x
    for i in range(n): 
        res = fn(res)
    return res

def repeat(fn,n):
    def function(x):
        return recursion(fn,n,x)
    return function

def recursion(fn,n,x):
    if n == 0:
        return x
    elif n>0:
        return recursion(fn,n-1,fn(x))
