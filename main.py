
nb = int(input ("Hello, Choose a number "))
def checknumber(nb):
   if nb % 2 == 0:
      print("your number is even")
   elif nb % 4 == 0:
      print("your number is devisors of 4")
   else:
      print("your number is odd")

checknumber(nb)

num=int(input("Let's do another try, now give me a new number "))
dev= int(input("and let's choose another number to divide by the first "))

def checkdev(num , dev):
    if dev % num == 0:
       print("your check divides evenly into the number chosen")
    else:
       print("your check is not divides evenly into the number chosen")

checkdev(num , dev)