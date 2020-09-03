"""
This python module gives access to functions that allows conversions and operations in number systems.
Conversions available :
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
-> binary subtraction
-> octal subtraction
-> hexadecimal subtraction
"""

__all__=['dtob','btod','dtoo','otod','dtoh','htod','htoo','otoh','htob','btoh','btoo','otob','binadd','binsub','octadd','octsub','hexadd','hexsub','isbinary','isoctal','ishexadecimal']

# Error thrown for bad input - TypeError

#isbinary() - used to check whether the given input is valid binary literal
#input - one
#ouptut- True/False. True if is a binary literal. False otherwise
def isbinary(a):
    if isinstance(a,int):
        c=0
        b=str(a)
        for i in b:
            if i=='0' or i=='1':
                c+=1
        if len(b)==c:
            return True
        else:
            return False
    else:
        raise TypeError("invalid inputs for type 'int'")

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
        raise TypeError("invalid inputs for type 'str'")

#isbinary() - used to check whether the given input is valid octal literal
#input - one
#ouptut- True/False. True if is a octal literal. False otherwise
def isoctal(a):
    if isinstance(a,int):
        b='01234567'
        d,c=str(a),0
        for i in d:
            if i in b:
                c+=1
        if len(d)==c:
            return True
        else:
            return False
    else:
        raise TypeError("invalid inputs for type 'int'")

# dtob() - to convert the given decimal literal to its equivalent binary value
# input - one(decimal literal - int)
#output - equivalent binary value of the given input
def dtob(a):
    if isinstance(a,int)==False:
        raise TypeError("invalid inputs for base 10")
    if a<0:
        raise TypeError("decimal literal should be positive")
    i,b=0,0
    while a:
        r=a%2
        b+=r*pow(10,i)
        a//=2
        i+=1
    return b

# btod() - to convert the given binary literal to its equivalent decimal value
# input - one(binary literal - int)
#output - equivalent decimal value of the given input
def btod(a):
    if isinstance(a,int)==False and isbinary(a)==False:
        raise TypeError("invalid inputs for base 2")
    if a<0:
        raise TypeError("binary literal should be positive")
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
        raise TypeError("invalid inputs for base 10")
    if a<0:
        raise TypeError("decimal literal should be positive")
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
        raise TypeError("invalid inputs for base 8")
    if a<0:
        raise TypeError("octal literal should be positive")
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
        raise TypeError("invalid inputs for base 10")
    if a<0:
        raise TypeError("decimal literal should be positive")
    h='%X'%a
    return h

# htod() - to convert the given hexadecimal literal to its equivalent decimal value
# input - one(hexadecimal literal - int)
#output - equivalent decimal value of the given input
def htod(a):
    if isinstance(a,str)==False and ishexadecimal(a)==False:
        raise TypeError("invalid inputs for base 16")
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
        raise TypeError("invalid inputs for base 16")
    b=htod(a)
    c=dtob(b)
    return c

# btoh() - to convert the given binary literal to its equivalent hexadecimal value
# input - one(binary literal - int)
#output - equivalent hexadecimal value of tw given input
def btoh(a):
    if isinstance(a,int)==False and isbinary(a)==False:
        raise TypeError("invalid inputs for base 2")
    if a<0:
        raise TypeError("binary literal should be positive")
    b=btod(a)
    c=dtoh(b)
    return c

# otob() - to convert the given octal literal to its equivalent binary value
# input - one(octal literal - int)
#output - equivalent binary value of the given input
def otob(a):
    if isinstance(a,int)==False and isoctal(a)==False:
        raise TypeError("invalid inputs for base 8")
    if a<0:
        raise TypeError("octal literal should be positive")
    b=otod(a)
    c=dtob(b)
    return c

# btoo() - to convert the given binary literal to its equivalent octal value
# input - one(binary literal - int)
#output - equivalent octal value of tw given input
def btoo(a):
    if isinstance(a,int)==False and isbinary(a)==False:
        raise TypeError("invalid inputs for base 2")
    if a<0:
        raise TypeError("binary literal should be positive")
    b=btod(a)
    c=dtoo(b)
    return c

# htoo() - to convert the given hexadecimal literal to its equivalent octal value
# input - one(hexadecimal literal - int)
#output - equivalent octal value of the given input
def htoo(a):
    if isinstance(a,str)==False and ishexadecimal(a)==False:
        raise TypeError("invalid inputs for base 16")
    b=htod(a)
    c=dtoo(b)
    return c

# otoh() - to convert the given octal literal to its equivalent hexadecimal value
# input - one(octal literal - int)
#output - equivalent hexadecimal value of the given input
def otoh(a):
    if isinstance(a,int)==False and isbinary(a)==False:
        raise TypeError("invalid inputs for base 8")
    if a<0:
        raise TypeError("octal literal should be positive")
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
        raise TypeError("invalid inputs for base 2")
    if (a<0) or (b<0):
        raise TypeError("binary literal should be positive")
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
#inputs - two binary literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their difference in the specified system
#   if sys=='dec' - difference in decimal system
#   if sys=='bin' - difference in binary system
#   if sys=='oct ' - difference in octal system
#   if sys=='hex' - difference in hexadecimal system
def binsub(a,b,sys='dec'):
    if(isinstance(a,int) and isbinary(a))==False and (isinstance(b,int) and isbinary(b))==False:
        raise TypeError("invalid inputs for base 2")
    if (a<0) or (b<0):
        raise TypeError("binary literal should be positive")
    if a<b:
        raise TypeError("first input should be greater")
    c,d=btod(a),btod(b)
    e=c-d
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

# octadd() - to add two octal literals and returns result in the specified number system
#inputs - two octal literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their sum in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='oct' - sum in octal system
#   if sys=='bin ' - sum in binary system
#   if sys=='hex' - sum in hexadecimal system
def octadd(a,b,sys='dec'):
    if (isinstance(a,int) and isoctal(a))==False and (isinstance(b,int) and isoctal(b))==False:
        raise TypeError("invalid inputs for base 8")
    if (a<0) or (b<0):
        raise TypeError("octal literal should be positive")
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
#inputs - two octal literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their difference in the specified system
#   if sys=='dec' - difference in decimal system
#   if sys=='bin' - difference in binary system
#   if sys=='oct ' - difference in octal system
#   if sys=='hex' - difference in hexadecimal system
def octsub(a,b,sys='dec'):
    if (isinstance(a,int) and isoctal(a))==False and (isinstance(b,int) and isoctal(b))==False:
        raise TypeError("invalid inputs for base 8")
    if (a<0) or (b<0):
        raise TypeError("octal literal should be positive")
    if a<b:
        raise TypeError("first input should be greater")
    c,d=otod(a),otod(b)
    e=c-d
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

# hexadd() - to add two hexdecimal literals and returns result in the specified number system
#inputs - two hexadecimal literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their sum in the specified system
#   if sys=='dec' - sum in decimal system
#   if sys=='oct' - sum in octal system
#   if sys=='bin ' - sum in binary system
#   if sys=='hex' - sum in hexadecimal system
def hexadd(a,b,sys='dec'):
    if (isinstance(a,str) and ishexadecimal(a))==False and (isinstance(b,str) and ishexadecimal(b))==False:
        raise TypeError("invalid inputs for base 16")
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
#inputs - two hexadecimal literals and sys='dec' / 'bin' / 'oct' / 'hex'
#output - their difference in the specified system
#   if sys=='dec' - difference in decimal system
#   if sys=='bin' - difference in binary system
#   if sys=='oct ' - difference in octal system
#   if sys=='hex' - difference in hexadecimal system
def hexsub(a,b,sys='dec'):
    if (isinstance(a,str) and ishexadecimal(a))==False and (isinstance(b,str) and ishexadecimal(b))==False:
        raise TypeError("invalid inputs for base 16")
    if a<b:
        raise TypeError("first input should be greater")
    c,d=htod(a),htod(b)
    e=c-d
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
