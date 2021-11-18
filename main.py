"""#EXCERCISE 1 (A)
for i in range(2,15,3):
  print(i)
#EXCERCISE 1 (B)
num = 2
while num < 15:
  print(num)
  num = num + 3"""

"""#EXCERCISE 2
sum = 0
value=int(input("Insert number"))
for i in range(value+1):
  sum=sum+i
print(sum)"""


"""#EXCERCISE 3
highest=0
for i in range(3):
  total_score=0
  for i in range(3):
    myscore= int(input("what is yourscore 1-300: "))
    while myscore < 0 or myscore > 300:
      print("invalid")
      myscore= int(input("try again 1-300: "))
    total_score += myscore
  if highest < total_score:
    highest = total_score
  print("total score is: " , total_score)
print("highest score is: " , highest)"""

"""#EXERCISE 4
import random
hp=100
complete=False
while not complete: 
 cont=input("play another round? (y/n)")
 if cont=="y":
   damage=random.randint(0,100)
   hp-=damage
   if hp<=0:
     print("Game Over")
     complete=True
   else:
      print("you were by damaged by",damage, "and your HP is now",hp)
 elif cont =="n":
   complete=True
 else:
   print("enter valid input")"""
  
