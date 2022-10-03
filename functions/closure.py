

# function within function called closure

def parent(msg):
    def child():
        print("Welcome")
        print(msg)
        print("end child")
    return child()
parent("Parent")

print("End of first example")
#another example
def grant_parent(msg):
    def parent(msg):
        def child():
            print("in child")
            print(msg)
        return child()
    return parent(msg)

grant_parent("msg from grant parent")

#passing function as arguments
def fun1():
    print("I am fun1 function")

def fun_as(fun):
    def child():
        print("in child -: arguments")
        fun()
    return child()

fun_as(fun1)