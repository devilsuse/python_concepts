a_string = "This is global"

'''ABCDE'''
def fun():
    ab="This is local"
    print(locals())


print(globals())
print('******************')
fun()
