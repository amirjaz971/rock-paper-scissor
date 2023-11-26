import random

#this program was written by amirjaz
scissor=1
rock=2
paper=3
wins=0
loses=0


print("hi let's play rock,paper or scissor game")
print("choose your answer by typing it or type end to finish the game")

while True:


 human_answer=input("scissor,rock or paper: ")
 if human_answer.lower()=="end":
     break

 print("""1.scissor
 2.rock
 3.paper
 """)
 cpu_answer=random.randint(1,3)
 



 if human_answer.lower()=="rock":
     if cpu_answer==scissor:
         print("the cpu answer is: "+str(cpu_answer))
         print("you won")
         wins+=1
     elif cpu_answer==rock:
         print("the cpu answer is: "+str(cpu_answer))
         print("equal")
     else:
         print("the cpu answer is: "+str(cpu_answer))
         print("you lost")
         
         loses+=1
 elif human_answer.lower()=="paper":
     if cpu_answer==scissor:
         print("the cpu answer is: "+str(cpu_answer))
         print("you lost")
         loses+=1
     elif cpu_answer==rock:
         print("the cpu answer is: "+str(cpu_answer))
         print("you won")
         wins+=1
     else:
         print("the cpu answer is: "+str(cpu_answer))
         print("equal")
         
 elif human_answer.lower()=="scissor":
     if cpu_answer==scissor:
         print("the cpu answer is: "+str(cpu_answer))
         print("equal")
     elif cpu_answer==rock:
         print("the cpu answer is: "+str(cpu_answer))
         print("you lost")
         loses+=1
     else:
         print("the cpu answer is: "+str(cpu_answer))
         print("you won")
         wins+=1
       
 else:
     print("you must choose between the given words")
 
 print("wins: "+str(wins))
 print("loses: "+str(loses))


        








