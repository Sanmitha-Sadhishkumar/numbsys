def dtob(a):
    i,b,r=0,0,int()
    d= -a if a<0 else a
    while d:
        r=d%2
        b+=r*pow(10,i)
        d//=2
        i+=1
    if a>=0:
        return b
    else:
        c=bin(b)
        d=c[3:]
        return int(d)

def btod(a):
    i,d,r=0,0,int()
    while a:
        r=a%10
        d+=r*pow(2,i)
        a//=10
        i+=1
    return d

def dtoo(a):
    i,o,r=0,0,int()
    while a:
        r=a%8
        o+=r*pow(10,i)
        a//=8
        i+=1
    return o

def otod(a):
    i,d,r=0,0,int()
    while a:
        r=a%10
        d+=r*pow(8,i)
        a//=10
        i+=1
    return d

def dtoh(a):
    h='%X'%a
    return h

def htod(a):
    a=a.upper()
    a=a[::-1]
    h={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    d,j=0,0
    for i in a:
        r=h[i]
        d+=r*pow(16,j)
        j=j+1
    return d

def htob(a):
    b=htod(a)
    c=dtob(b)
    return c

def btoh(a):
    b=btod(a)
    c=dtoh(b)
    return c

def otob(a):
    b=otod(a)
    c=dtob(b)
    return c

def btoo(a):
    b=btod(a)
    c=dtoo(b)
    return c

def htoo(a):
    b=htod(a)
    c=dtoo(b)
    return c

def otoh(a):
    b=otod(a)
    c=dtoh(b)
    return c

def binadd(a,b,sys='dec'):
    c,d=btod(a),btod(b)
    e=c+d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f
    elif sys=='oct':
        g=dtoo(e)
        return g
    elif sys=='hex':
        h=dtoh(e)
        return h

def binsub(a,b,sys='dec'):
    c,d=btod(a),btod(b)
    e=c-d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f

def octadd(a,b,sys='dec'):
    c,d=otod(a),otod(b)
    e=c+d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f
    elif sys=='oct':
        g=dtoo(e)
        return g
    elif sys=='hex':
        h=dtoh(e)
        return h

def octsub(a,b,sys='dec'):
    c,d=otod(a),otod(b)
    e=c-d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f

def hexadd(a,b,sys='dec'):
    c,d=htod(a),htod(b)
    e=c+d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f
    elif sys=='oct':
        g=dtoo(e)
        return g
    elif sys=='hex':
        h=dtoh(e)
        return h

def hexsub(a,b,sys='dec'):
    c,d=htod(a),htod(b)
    e=c-d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f

def decadd(a,b,sys='dec'):
    e=a+b
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f
    elif sys=='oct':
        g=dtoo(e)
        return g
    elif sys=='hex':
        h=dtoh(e)
        return h

def decsub(a,b,sys='dec'):
    e=a-b
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f

print(hexadd('ff','10','bin'))
