import builtins

a= dir(builtins)
print(type(a))



o = a.index("tuple")
for i in a :
    print(i)
    
print(help(a[o]))