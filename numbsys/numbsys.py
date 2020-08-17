"""
This python module gives access to functions that allows conversions and operations in number systems. Conversions available :
-> decimal to binary and vice versa
-> decimal to octal and vice versa
-> decimal to hexadecimal and vice versa
-> binary to octal and vice versa
-> binary to hexadecimal and vice versa
-> octal to hexadecimal and vice versa
-> Binary conformation
-> Hexadecimal conformation
-> Octal conformation

Operations available:
-> binary addition
-> octal addition
-> hexadecimal addition
-> decimal addition
-> binary subtraction
-> octal subtraction
-> hexadecimal subtraction
-> decimal subtraction
"""

__all__=['BaseError','dtob','btod','dtoo','otod','dtoh','htod','htoo','otoh','htob','btoh','btoo','otob','binadd','binsub','octadd','octsub','hexadd','hexsub','isbinary','isoctal','ishexadecimal']

#isbinary() - used to check whether the given input is valid binary literal
#input - one
#ouptut- True/False. True if is a binary literal. False otherwise
def isbinary(a):
    if isinstance(a,int):
        b,c='',0
        while a:
            r=a%10
            b=b+chr(48+r)
            a//=10
        for i in b:
            if i=='0' or i=='1':
                c+=1
        if len(b)==c:
            return True
        else:
            return False
    else:
        return False

#ishexadecimal() - used to check whether the given input is valid hexadecimal literal
#input - one
#ouptut- True/False. True if is a hexadecimal literal. False otherwise
def ishexadecimal(a):
    if isinstance(a,str):
        a=a.upper()
        b,c='0123456789ABCDEF',0
        for i in a:
            if i in b:
                c+=1
        if len(a)==c:
            return True
        else:
            return False
    else:
        return False

#isoctal() - used to check whether the given input is valid octal literal
#input - one
#ouptut- True/False. True if is a octal literal. False otherwise
def isoctal(a):
    if isinstance(a,int):
        b='01234567'
        d,c='',0
        while a:
            r=a%10
            d=d+chr(48+r)
            a//=10
        for i in d:
            if i in b:
                c+=1
        if len(d)==c:
            return True
        else:
            return False
    else:
        return False

# Error thrown for bad input - BaseError        
class BaseError(Exception):
    def __init__(self,arg):
        self.a=arg
    def __str__(self):
        if self.a==10:
            return 'Invalid inputs of base 2, 8, 16 or other for base 10'
        elif self.a==8:
            return 'Invalid inputs of base 2, 10, 16 or other for base 8'
        elif self.a==16:
            return 'Invalid inputs of base 2, 8, 10 or other for base 16'
        elif self.a==2:
            return 'Invalid inputs of base 8, 10,16 or other for base 2'
        else:
            return 'Invalid inputs of base. Base should be 2, 8, 10 or 16'

# dtob() - to convert the given decimal literal to its equivalent binary value
# input - one(decimal literal - int)
#output - equivalent binary value of the given input
def dtob(a):
    if isinstance(a,int)==False:
        raise BaseError(10)
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


# btod() - to convert the given binary literal to its equivalent decimal value
# input - one(binary literal - int)
#output - equivalent decimal value of the given input
def btod(a):
    if isinstance(a,int)==False and isbinary(a)==False:
        raise BaseError(2)
    i,d,r=0,0,int()
    while a:
        r=a%10
        d+=r*pow(2,i)
        a//=10
        i+=1
    return d


# dtoo() - to convert the given decimal literal to its equivalent octal value
# input - one(decimal literal - int)
#output - equivalent octal value of the given input
def dtoo(a):
    if isinstance(a,int)==False:
        raise BaseError(10)
    i,o,r=0,0,int()
    while a:
        r=a%8
        o+=r*pow(10,i)
        a//=8
        i+=1
    return o

# otod() - to convert the given octal literal to its equivalent decimal value
# input - one(octal literal - int)
#output - equivalent decimal value of the given input
def otod(a):
    if isinstance(a,int)==False and isoctal(a)==False:
        raise BaseError(8)
    i,d,r=0,0,int()
    while a:
        r=a%10
        d+=r*pow(8,i)
        a//=10
        i+=1
    return d


# dtoh() - to convert the given decimal literal to its equivalent hexadecimal value
# input - one(decimal literal - int)
#output - equivalent hexadecimal value of the given input
def dtoh(a):
    if isinstance(a,int)==False:
        raise BaseError(10)
    h='%X'%a
    return h

# htod() - to convert the given hexadecimal literal to its equivalent decimal value
# input - one(hexadecimal literal - int)
#output - equivalent decimal value of the given input
def htod(a):
    if isinstance(a,str)==False and ishexadecimal(a)==False:
        raise BaseError(16)  
    a=a.upper()
    a=a[::-1]
    h={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    d,j=0,0
    for i in a:
        r=h[i]
        d+=r*pow(16,j)
        j=j+1 
    return d

# htob() - to convert the given hexadecimal literal to its equivalent binary value
# input - one(hexadecimal literal - int)
#output - equivalent binary value of the given input
def htob(a):
    if isinstance(a,str)==False and ishexadecimal(a)==False:
        raise BaseError(16)
    b=htod(a)
    c=dtob(b)
    return c

# btoh() - to convert the given binary literal to its equivalent hexadecimal value
# input - one(binary literal - int)
#output - equivalent hexadecimal value of tw given input
def btoh(a):
    if isinstance(a,int)==False and isbinary(a)==False:
        raise BaseError(2)
    b=btod(a)
    c=dtoh(b)
    return c

# otob() - to convert the given octal literal to its equivalent binary value
# input - one(octal literal - int)
#output - equivalent binary value of the given input
def otob(a):
    if isinstance(a,int)==False and isoctal(a)==False:
        raise BaseError(8)
    b=otod(a)
    c=dtob(b)
    return c

# btoo() - to convert the given binary literal to its equivalent octal value
# input - one(binary literal - int)
#output - equivalent octal value of tw given input
def btoo(a):
    if isinstance(a,int)==False and isbinary(a)==False:
        raise BaseError(2)
    b=btod(a)
    c=dtoo(b)
    return c

# htoo() - to convert the given hexadecimal literal to its equivalent octal value
# input - one(hexadecimal literal - int)
#output - equivalent octal value of the given input
def htoo(a):
    if isinstance(a,str)==False and ishexadecimal(a)==False:
        raise BaseError(16)
    b=htod(a)
    c=dtoo(b)
    return c

# otoh() - to convert the given octal literal to its equivalent hexadecimal value
# input - one(octal literal - int)
#output - equivalent hexadecimal value of the given input
def otoh(a):
    if isinstance(a,int)==False and isoctal(a)==False:
        raise BaseError(8)
    b=otod(a)
    c=dtoh(b)
    return c

# binadd() - to add two binary literals and returns result in the specified number system
#inputs - two binary literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their sum in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='oct' - sum in octal system
#   if sys=='bin ' - sum in binary system
#   if sys=='hex' - sum in hexadecimal system
def binadd(a,b,sys='dec'):
    if(isinstance(a,int) and isbinary(a))==False and (isinstance(b,int) and isbinary(b))==False:
        raise BaseError(2)
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

# binsub() - to subtract two binary literals and returns result in the specified number system
#inputs - two binary literals and sys='dec' / 'bin'
#output - their difference in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='bin' - sum in binary system
def binsub(a,b,sys='dec'):
    if(isinstance(a,int) and isbinary(a))==False and (isinstance(b,int) and isbinary(b))==False:
        raise BaseError(2)
    c,d=btod(a),btod(b)
    e=c-d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f

# octadd() - to add two octal literals and returns result in the specified number system
#inputs - two octal literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their sum in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='oct' - sum in octal system
#   if sys=='bin ' - sum in binary system
#   if sys=='hex' - sum in hexadecimal system
def octadd(a,b,sys='dec'):
    if (isinstance(a,int) and isoctal(a))==False and (isinstance(b,int) and isoctal(b))==False:
        raise BaseError(8)
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

# octsub() - to subtract two octal literals and returns result in the specified number system
#inputs - two octal literals and sys='dec' / 'bin'
#output - their difference in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='bin' - sum in binary system
def octsub(a,b,sys='dec'):
    if (isinstance(a,int) and isoctal(a))==False and (isinstance(b,int) and isoctal(b))==False:
        raise BaseError(8)
    c,d=otod(a),otod(b)
    e=c-d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f

# hexadd() - to add two hexdecimal literals and returns result in the specified number system
#inputs - two hexadecimal literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their sum in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='oct' - sum in octal system
#   if sys=='bin ' - sum in binary system
#   if sys=='hex' - sum in hexadecimal system
def hexadd(a,b,sys='dec'):
    if (isinstance(a,str) and ishexadecimal(a))==False and (isinstance(b,str) and ishexadecimal(b))==False:
        raise BaseError(8) 
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

# hexsub() - to subtract two hexadecimal literals and returns result in the specified number system
#inputs - two hexadecimal literals and sys='dec' / 'bin'
#output - their difference in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='bin' - sum in binary system
def hexsub(a,b,sys='dec'):
    if (isinstance(a,str) and ishexadecimal(a))==False and (isinstance(b,str) and ishexadecimal(b))==False:
        raise BaseError(16)
    c,d=htod(a),htod(b)
    e=c-d
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f

# decadd() - to add two decimal literals and returns result in the specified number system
#inputs - two decimal literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their sum in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='oct' - sum in octal system
#   if sys=='bin ' - sum in binary system
#   if sys=='hex' - sum in hexadecimal system
def decadd(a,b,sys='dec'):
    if (isinstance(a,str) and a.isdecimal())==False and (isinstance(b,str) and b.isdecimal())==False:
        raise BaseError(10)
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

# decsub() - to subtract two decimal literals and returns result in the specified number system
#inputs - two decimal literals and sys='dec' / 'bin'
#output - their difference in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='bin' - sum in binary system
def decsub(a,b,sys='dec'):
    if (isinstance(a,str) and a.isdecimal())==False and (isinstance(b,str) and b.isdecimal())==False:
        raise BaseError(10)
    e=a-b
    if sys=='dec':
        return e
    elif sys=='bin':
        f=dtob(e)
        return f
