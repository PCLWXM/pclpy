def outer():

    def inner():
        str = "inner"
        print(str)
    inner()
outer()
print("**************")

def outer():
    str = "outer"
    def inner():
        #str = "inner"
        print(str)
    inner()
outer()
print("**************")

str = "global str"
def outer():
    #str = "outer"
    def inner():
        #str = "inner"
        print(str)
    inner()
outer()
print("**************")

#str = "global str"
def outer():
    #str = "outer"
    def inner():
        #str = "inner"
        print(str)
    inner()
outer()
print("**************")