##Question 1

#requesting input from user
x=int(input("Enter number in x: "))
y=int(input("Enter number in y: "))
z=int(input("Enter number in z: "))

print("Value of x is: ",x)
print("Value of y is: ",y)
print("Value of z is: ",z)
#printing final answer
avg= (x+y+z)/3
print("Average of given numbers is: ",avg)



##Question 2

#taking input from the user 
grossInc= float(input("Enter the gross income: "))
dep= int(input("Enter the number of dependents: "))

#standard deduction is in dollars ($) and the rate of the tax is 20%
rate= 0.2
stndDed= 10000
taxableInc= grossInc-stndDed-(dep*3000)
tax= taxableInc*rate

print("tax is: ",tax)



##Question 3

sid= input("Enter SID: ")
name= input("Enter Name: ")
gender= input("Enter Gender(M, F, U for unknown): ")
course= input("Enter Course Name: ")
cgpa= float(input("Enter CGPA: "))
# inserting above items in student list
student= [sid, name, gender, course, cgpa]

print(student)



##Question 4

marks= [78, 55, 98, 75, 69]

#sorting the above list int
marks.sort()
print(marks)



##Question 5

#Part a
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.remove('Black')
print("Part a: ", color)

#Part b
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Replacing Black and Pink with Purple and removing black and pink
color[3:5]= ['Purple'] 
print("Part b: ", color)