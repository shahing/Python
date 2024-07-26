name = "ApnaCollege"
#print(name[9])
print(name[1:4])
print(name[:7])# 0:7
print(name[5:]) #5:len(name )

str = "apple"   # -2  -1

str = "my name is Ghazala Shhain" 
print(str.endswith("in"))
print(str.capitalize())

str = "my name is ghazala shahin"
print(str.replace("name ", "work")) # REPLACE

#print(str.find("a"))  # FIND
print(str.count("a"))  #COUNT 

age = 27
if(age>18):
    print("Eligible for vote")
elif(age<10): print("Not eligible for vote")
else: print("NOne")

num = int(input("Enter Number: "))

if(num%2==0): 
    print("Even")
else:
     print("odd")

     a = int(input("Enter first number: "))
     b = int(input("Enter second number: "))
     c = int(input("Enter third number: "))

     if(a>b and a>c):
         print(a, "is greater number")
     elif(b>a and b>c):
         print(b, "is greater number")
     else: print(c, "is greater number")    