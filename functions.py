# Functions: A group of related statements to perform a task and return a value
# Ex.

def to_celsius(x):
    '''Convert Fahrenheit to  Celsius'''
    return (x-32) * 5/9
print(to_celsius(44)) # this will print 6.666666666666667

to_celsius(44) 




def greeting(name):
    print("Welcome, " + name)

greeting("Carlos")  # this will print "Welcome, Carlos"
greeting("V")  # this will print "Welcome, V" 



def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of the " + department)

greeting("Carlos", "IT") # this will print "Welcome , Carlos" You are part of the IT department 