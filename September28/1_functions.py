"""****************************************************************"""
def sayHello():
    print("Hello");
	
sayHello()

"""****************************************************************"""
def sayHelloWithDoc():
    """This function just says hello"""
    print("Hello");
	
sayHelloWithDoc.__doc__

sayHello.__doc__

"""****************************************************************"""
def sayName(name):
    """This function says the inputed name"""
    """Need to pass a parameter"""
    print("Hello " + name);
	
sayName("Krisanth Kumar")

"""****************************************************************"""
def sayWelcome(name, loc="Chennai"):
    """This functions gives a welcome message"""
    """Need to pass a parameter"""
    print("Hi " + name + ", Welcome to " + loc);
	
sayWelcome("Kumar")
sayWelcome("Kumar","Madurai")

"""****************************************************************"""
def returnCheck():
    """Function to check the return values"""
    if(1==10):
        return '1 is equal to 10'
    else:
        return '1 is not equal to 10'
		
a = returnCheck()
print(a)

"""****************************************************************"""
def test():
    val=10

a = test()
print(a) 

def test():
    val=10
    return val

a = test()
print(a)
"""****************************************************************"""
def fnCall():
    """Function to test function call"""
    sayWelcome("Kumar","Madurai")
    res = returnCheck()
    print("Retuned value : " + res)
	
fnCall()
	
"""****************************************************************"""
def localScope():
    x="Test"
    return x

localScope()
print("X:" + x)


"""****************************************************************"""
x="Test"
def localScope():
    return "Value from function " + x

localScope()
print("X:" + x)
