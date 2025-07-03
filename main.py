lt = sorted([50,13,15,27,92,50,35,7])
num = int(input("enter a number to check it if exist "))

print(lt)
def check(lt , num):
   if num in lt:
      print(True)
   else:
      print(False)

check(lt , num)