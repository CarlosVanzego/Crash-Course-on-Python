# Expressions: A combination of numbers, symbols, and variables to compute and return a result upon evaluation
# Ex
sum = 4 + 4
print(sum)

print(7 + 8.5)

print("a" + "b" + "c")

print("This " + "is " + "pretty " + "cool😎")



# In the example below, I'm calculating the area of a triangle, and when printint it, I'm adding it to a string.
# To do this, I'm calling the str() function to convert a number into a string.
base = 6
height = 3
area = (base*height)/2

print("The area of the triangle is: " + str(area))



# In this scenario, I have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. I then calculate the average file size by having Python add all the values for me, and then set the files variable to the number of files. Finally, I print a message saying "The average size is: " followed by the resulting number.
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total/files

print("The average size is: " + str(average))



