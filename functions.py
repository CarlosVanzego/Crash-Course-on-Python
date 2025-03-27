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




# In the example below, I'm calculating the area of the triangle, and when printing it, I'm addning the result to a string. 
def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum)) # this will print "The sum of both areas is: 20.5"


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds) # this will print 1 23 20 