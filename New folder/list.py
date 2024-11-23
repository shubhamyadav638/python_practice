def fun(x,y,type):
    if type == 'add':
        z= x+y
    elif type == 'sub':
       z=x-y
    elif type == 'multi':
        z=x*y
    elif type == 'div':
       z = x/y
    else:
       z = 'no data'

    return z

a = fun(12,12,'add')
a = fun(12,12,'sub')
print(a)
  