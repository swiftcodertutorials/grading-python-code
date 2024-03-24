quiz=input("Are you interested to join this quiz:")
if quiz.lower() !='yes':
    quit()
name=input("Enter your full name :")
print('Full marks 10. Each question carriers 1 marks.')
print("""
                  ----------quiz----------
""")
score=0
answer=input("what is the full name form of 'www' ? ")
if answer.lower()=='world wide web':
    print("Correct Answer")
    score += 1

else:
    print("Wrong Answer .....  Correct Answer is 'World Wide Web'")

answer=input("CPU stands for ______________")
if answer.lower =='central processing unit':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer .......... Correct Answer is 'central processing unit'")

answer=input("What is the full form of 'HTML' ? ")
if answer.lower() =='hyper text markup language':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer  ........ Correct Answer is 'hyper text markup language'")

answer=input(" 'Mouse is an input device' - True or False ? ")
if answer.lower() =='true':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer  ........ Correct Answer is 'true'")

answer=input(" GPU stande for____________ ? ")
if answer.lower() =='graphics processing unit':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer  ........ Correct Answer is 'graphics processing unit'")

answer=input("What is the full form of 'HTTPS' ? ")
if answer.lower() =='hyper text transfer protocol':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer  ........ Correct Answer is 'hyper text transfer protocol'")

answer=input(" what does 'ISP' stands for ? ")
if answer.lower() =='internet service provider':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer  ........ Correct Answer is 'internet service provider'")

answer=input(" 'Webcam is an output device' - True or False ? ")
if answer.lower() =='false':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer  ........ Correct Answer is 'false'")

answer=input(" what does 'RAM' stands for ___________ ? ")
if answer.lower() =='randam processing unit':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer  ........ Correct Answer is 'random processing unit'")

answer=input(" 'ATM' full form_____________? ")
if answer.lower() =='automatted tellor machine':
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer  ........ Correct Answer is 'automated tellor machine'")

print('Dear',name,'you obtained'+ str(score) +'Marks out of 10')
n=(score/10)*100
if(n<40):
    pprint("you are fail")
elif(n>=40 and n<50):
    print("Your grade is Third Devision")
elif(n>=50 and n<60):
    print("Your grade is Second Devision")
elif(n>=60 and n<75):
    print("Your grade is First Devision")
elif(n>=75 and n<80):
    print("Your grade is Star")
elif(n>=80 and n<90):
    print("Congratulation!!! letter")
elif(n>=90 and n<=100):
    print("Congratulation!!! utstanding")
else:
    print("Invalid Input")

  
    
