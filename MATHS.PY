import random
import math
a=input("Enter your Name : ")
print("WELCOME to the MATHS EXHIBITION ",a)
a1=input("  ")
print("Choose your Level")
print("-------------------------------------------------------------------------------")
print("choose Level 1 if you are from class 6th ")
print("choose Level 2 if you are from class 7th ")
print("choose Level 3 if you are from class 8th ")
print("choose Level 4 if you are from class 9th ")
print("choose Level 5 if you are from class 10th ")
print("choose Level 6 if you are from class 11th ")
print("choose Level 7 if you are from class 12th ")
print("-------------------------------------------------------------------------------")
b=int(input("choose your level(1/2/3/4/5/6/7)"))
print(" ")
print("-------------------------------------------------------------------------------")
print(" ")
c=0
if b==1:
    for i in range(1,6):
        print("Question",i)
        if i==1:
            m1=random.randint(5,15)
            m2=random.randint(5,15)
            m4=str(m1)+"X"+str(m2)+"="
            m3=int(input(m4))
            if m3==(m1*m2):
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else :
                print('Oops! You Loose it')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",m1*m2)
            print("-------------------------------------------------------------------------------")
            a=input(" ")
        
        elif i==2:
            m1=random.randint(5,15)
            m2=str(m1)+"^2"+"="
            m3=int(input(m2))
            if m3==m1**2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",m1**2)
            print("--------------------------------------------------------------------------------")
            a=input(" ")

        elif i==3:
            m1=random.randint(5,15)
            m2=random.randint(5,15)
            print("let the length of rectangle is :",m1)
            print("let the breadth of rectangle is :",m2)
            m3=int(input("THE AREA OF RECTANGLE IS??? "))
            if m3==m1*m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",m1*m2)
            print("-------------------------------------------------------------------------------")
            a=input(" ")
        
        elif i==4:
            m1=random.randint(1,80)
            m2=random.randint(1,80)
            m4="If the two angles of triangle are "+str(m1)+" and "+ str(m2)+" Then the third ANGLE is ??? "
            m3=int(input(m4))
            if m3==180-(m1+m2):
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",180-(m1+m2))
            print("-------------------------------------------------------------------------------")
            a=input(" ")
        elif i==5:
            m1= random.randrange(1200,8000,100)
            m3=str(m1)+"grams =______ kilograms?? "
            m2=eval(input(m3))
            if m2==(m1/1000):
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",m1/1000)
            print("-------------------------------------------------------------------------------")
            a=input(" ")
        else:
            m1=random.randint(-80,1)
            m2=random.randint(1,80)
            m3=str(m1)+"+" +str(m2)
            m4=int(input(m3))
            if m4==m1+m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print(" ")
            print("-------------------------------------------------------------------------------")
            print(" ")
            a=input(" ")
if b==2:
    for i in range(1,6):
        print("Question",i)
        if i==1:
            m1=random.randrange(7,70,7)
            m2="if the radius of the circle is "+str(m1)+" The circumference of the circle is :"
            m3=int(input(m2))
            if m3==2*22*(m1/7):
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it ')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",44*(m1/7))
            print("-------------------------------------------------------------------------------")
            a=input(" ")

        elif i==2:
            m1=random.randint(1,800)
            m2="Is "+str(m1)+" divisble by 3 ???(Y/N) "
            m3=input(m2)
            if m3 == "Y" and m1%3 == 0 :
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            elif m3 == "N" and m1%3 != 0 :
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print("-------------------------------------------------------------------------------")
            a=input(" ")

        elif i==3:
            m1=random.randint(2,11)
            m2=str(m1)+"^2"+"="
            m3=int(input(m2))
            if m3==m1**2:
                print("YOU GOT IT RIGHT:)")
                c+=10

                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",m1**2)
            print("-------------------------------------------------------------------------------")
            a=input(" ")

        elif i==4:
            m1= random.randint(1,100)
            m3=str(m1)+"litres =______ mililitres?? "
            m2=eval(input(m3))
            if m2==(m1*1000):
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",m1*1000)
            print("-------------------------------------------------------------------------------")
            a=input(" ")

        else :
             m1=random.randint(1,10)
             m2="if the side of a cube is "+ str(m1)+" Then the VOLUME OF CUBE is ??? "
             m3=int(input(m2))
             if m3==m1**3:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it')
             print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",m1**3)
             print("-------------------------------------------------------------------------------")
             a=input(" ")

if b==3:
    for i in range(1,6):
        print("Question",i)
        if i==1:
             m1=random.randint(15,30)
             m2=str(m1)+"^2"+"="
             m3=int(input(m2))
             if m3==m1**2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it')
             print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",m1**2)
             print("-------------------------------------------------------------------------------")
             a=input(" ")

        elif i==2:
             m1=random.randint(0,80)
             m2="if x and y are two complementary angles and x="+str(m1)
             m3=" Then the value of y is??? "
             m4=m2+m3
             m5=int(input(m4))
             if m5==90-m1:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it')
             print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",90-m1)
             print("-------------------------------------------------------------------------------")  
             a=input(" ")

        elif i==3:
              m1=random.randint(5,15)
              m2=random.randint(2,6)
              m3=m1+m2
              m4=m1+2*m2
              m5="what is next term? "+str(m1)+","+str(m3)+","+str(m4)+",____"
              m6=int(input(m5))
              if m6==m1+3*m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
              else :
                print('Oops! You Loose it:(')
                print(" ")
              print("|||||||||||||||||||||||||||||||||||||||||||||")
              print(" ")
              print("The correct answer is ",m1+3*m2)
              print("-------------------------------------------------------------------------------")
              a=input(" ")

        elif i==4:
             m1=random.randint(5,10)
             m2=random.randint(10,15)
             m3='If the base and height of a parallelogram are '+str(m1)+' and '+str(m2)
             m4=' respectively....Then the area of parallelogram is???'
             m5=m3+m4
             m6=int(input(m5))
             if m6==m1*m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it:(')
                print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",m1*m2)
             print("-------------------------------------------------------------------------------")
             a=input(" ")

        else :
            m1=random.randrange(7,70,7)
            m2="if the radius of the circle is "+str(m1)+" The circumference of the circle is :"
            m3=int(input(m2))
            if m3==2*22*(m1/7):
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it :(')
                print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",44*(m1/7))
            print("-------------------------------------------------------------------------------")
            a=input(" ")

if b==3:
    for i in range(1,6):
        print("Question",i)
        if i==1:
             m1=random.randint(15,30)
             m2=str(m1)+"^2"+"="
             m3=int(input(m2))
             if m3==m1**2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it')
             print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",m1**2)
             print("-------------------------------------------------------------------------------")
             a=input(" ")
        
        elif i==2:
             m1=random.randint(0,80)
             m2="if x and y are two complementary angles and x="+str(m1)
             m3=" Then the value of y is??? "
             m4=m2+m3
             m5=int(input(m4))
             if m5==90-m1:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it')
             print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",90-m1)
             print("-------------------------------------------------------------------------------")  
             a=input(" ")
        
        elif i==3:
              m1=random.randint(5,15)
              m2=random.randint(2,6)
              m3=m1+m2
              m4=m1+2*m2
              m5="what is next term? "+str(m1)+","+str(m3)+","+str(m4)+",____"
              m6=int(input(m5))
              if m6==m1+3*m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
              else :
                print('Oops! You Loose it:(')
                print(" ")
              print("|||||||||||||||||||||||||||||||||||||||||||||")
              print(" ")
              print("The correct answer is ",m1+3*m2)
              print("-------------------------------------------------------------------------------")
              a=input(" ")
        
        elif i==4:
             m1=random.randint(5,10)
             m2=random.randint(10,15)
             m3='If the base and height of a parallelogram are '+str(m1)+' and '+str(m2)
             m4=' respectively....Then the area of parallelogram is???'
             m5=m3+m4
             m6=int(input(m5))
             if m6==m1*m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it:(')
                print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",m1*m2)
             print("-------------------------------------------------------------------------------")
             a=input(" ")
        
        else :
            m1=random.randrange(7,70,7)
            m2="if the radius of the circle is "+str(m1)+" The circumference of the circle is :"
            m3=int(input(m2))
            if m3==2*22*(m1/7):
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it :(')
                print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",44*(m1/7))
            print("-------------------------------------------------------------------------------")
            a=input(" ")

if b==4:
    for i in range(1,6):
        print("Question",i)
        if i==1:
            m1=random.randint(1,2000)
            m2="Is "+str(m1)+" divisble by 4 ???(Y/N) "
            m3=input(m2)
            if m3 == "Y" and m1%4 == 0 :
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            elif m3 == "N" and m1%4 != 0 :
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it :(')
            print("-------------------------------------------------------------------------------")
            a=input(" ")

        elif i==2:
             m1=random.randint(15,30)
             m2=str(m1)+"^2"+"="
             m3=int(input(m2))
             if m3==m1**2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it')
             print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",m1**2)
             print("-------------------------------------------------------------------------------")
             a=input(" ")

        elif i==3:
              m1=random.randint(30,150)
              m2="if x and y are two suplementary angles and x="+str(m1)
              m3=" Then the value of y is??? "
              m4=m2+m3
              m5=int(input(m4))
              if m5==180-m1:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
              else :
                print('Oops! You Loose it:(')
                print(" ")
              print("|||||||||||||||||||||||||||||||||||||||||||||")
              print(" ")
              print("The correct answer is ",180-m1)
              print("-------------------------------------------------------------------------------")
              a=input(" ")

        elif i==4:
            m1=random.randint(1,80)
            m2=random.randint(1,80)
            m4="If the two angles of triangle are "+str(m1)+" and "+ str(m2)+" Then the third ANGLE is ??? "
            m3=int(input(m4))
            if m3==180-(m1+m2):
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print(" ")
            print("|||||||||||||||||||||||||||||||||||||||||||||")
            print(" ")
            print("The correct answer is ",180-(m1+m2))
            print("-------------------------------------------------------------------------------")
            a=input(" ")

        else:
              m1=random.randint(5,15)
              m2=random.randint(2,6)
              m3=m1+m2
              m4=m1+2*m2
              m5="what is next term? "+str(m1)+","+str(m3)+","+str(m4)+",____"
              m6=int(input(m5))
              if m6==m1+3*m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
              else :
                print('Oops! You Loose it:(')
                print(" ")
              print("|||||||||||||||||||||||||||||||||||||||||||||")
              print(" ")
              print("The correct answer is ",m1+3*m2)
              print("-------------------------------------------------------------------------------")
              a=input(" ")

if b==5:
     for i in range(1,6):
        print("Question",i)
        if i==1:
             m1=random.randint(15,30)
             m2=str(m1)+"^2"+"="
             m3=int(input(m2))
             if m3==m1**2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
             else :
                print('Oops! You Loose it')
             print(" ")
             print("|||||||||||||||||||||||||||||||||||||||||||||")
             print(" ")
             print("The correct answer is ",m1**2)
             print("-------------------------------------------------------------------------------")
             a=input(" ")
        
        if i==2:
            m1=random.randint(1,2000)
            m2="Is "+str(m1)+" divisble by 4 ???(Y/N) "
            m3=input(m2)
            if m3 == "Y" and m1%4 == 0 :
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            elif m3 == "N" and m1%4 != 0 :
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it :(')
            print("-------------------------------------------------------------------------------")
            a=input(" ")
        
        if i==3:
              m1=random.randint(35,55)
              m2=random.randint(11,20)
              m3=m1+m2
              m4=m1+2*m2
              m5="what is next term? "+str(m1)+","+str(m3)+","+str(m4)+",____"
              m6=int(input(m5))
              if m6==m1+3*m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
              else :
                print('Oops! You Loose it:(')
              print(" ")
              print("|||||||||||||||||||||||||||||||||||||||||||||")
              print(" ")
              print("The correct answer is ",m1+3*m2)
              print("-------------------------------------------------------------------------------")
              a=input(" ")

if b==6:
     for i in range(1,6):
         print("Question",i)
         if i==1:
            m1=random.randint(25,50)
            m2=str(m1)+"^2"+"="
            m3=int(input(m2))
            if m3==m1**2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print("-------------------------------------------------------------------------------")
            a=input(" ")    
         elif  i==2:
             m1=random.randrange(50,101,2)
             m2="i^"+str(m1)+"  (where 'i' is iota) = "
             m3=int(input(m2))
             if m3== -1 and m1%4==2:
                  print("YOU GOT IT RIGHT:)")
                  c+=10
                  print("YOUR SCORE IS",c)
             elif m3== 1 and m1%4==0:
                  print("YOU GOT IT RIGHT:)")
                  c+=10
                  print("YOUR SCORE IS",c)
             else:
                  print('Oops! You Loose it')
                  
             print("-------------------------------------------------------------------------------")
             a=input(" ")
         elif i==3:
              m1= random.randrange(1000,9500,100)
              m3=str(m1)+"litres =______ m^3?? "
              m2=eval(input(m3))
              if m2==(m1/1000):
                  print("YOU GOT IT RIGHT:)")
                  c+=10
                  print("YOUR SCORE IS",c)
              else:
                  print('Oops! You Loose it')
              print("-------------------------------------------------------------------------------")
              a=input(" ")
                  
         
         elif i==4:
              m1=random.randint(35,55)
              m2=random.randint(11,20)
              m3=m1+m2
              m4=m1+2*m2
              m5="what is next term? "+str(m1)+","+str(m3)+","+str(m4)+",____"
              m6=int(input(m5))
              if m6==m1+3*m2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
              else :
                print('Oops! You Loose it:(')
                print(" ")
              print("|||||||||||||||||||||||||||||||||||||||||||||")
              print(" ")
              print("The correct answer is ",m1+3*m2)
              print("-------------------------------------------------------------------------------")
              a=input(" ")
         elif i==5:
            m1=random.randint(1,2000)
            m2="Is "+str(m1)+" divisble by 4 ???(Y/N) "
            m3=input(m2)
            if m3 == "Y" and m1%4 == 0 :
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            elif m3 == "N" and m1%4 != 0 :
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it :(')
if b==7:
     for i in range(1,6):
         print("Question",i)
         if i==1:
            m1=random.randint(25,50)
            m2=str(m1)+"^2"+"="
            m3=int(input(m2))
            if m3==m1**2:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print("-------------------------------------------------------------------------------")
            a=input(" ")
         elif i==2:
            m1=random.randint(2,5)
            m2=random.randint(2,4)
            m4="If the order of matrix is "+str(m1)+"x"+str(m2)
            m5=".....Then no. of elements in matrix with entry (0,1) only is??? "
            m6=m4+m5
            m7=m1*m2
            m3=int(input(m6))
            if m3==2**m7:
                print("YOU GOT IT RIGHT:)")
                c+=10
                print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print("-------------------------------------------------------------------------------")
            a=input(" ")
         elif i==3:
            print("If A is | -1 0 1|")
            print("            |  0 1 2|")
            print("            |  0 2 4|")
            m1="Then the value of A is ??? "
            m2=int(input(m1))
            if m2==0:
                 print("YOU GOT IT RIGHT:)")
                 c+=10
                 print("YOUR SCORE IS",c)
            else:
                print('Oops! You Loose it')
            print("-------------------------------------------------------------------------------")
            a=input(" ")
         elif i==4:
           m1=random.randint(25,800)
           m2="Is "+str(m1)+" divisible by 12???(Y/N) "
           m3=input(m2)
           if m3 == "Y" and m1%12 == 0 :
                 print("YOU GOT IT RIGHT:)")
                 c+=10
                 print("YOUR SCORE IS",c)
           elif m3 == "N" and m1%12 != 0 :
                 print("YOU GOT IT RIGHT:)")
                 c+=10
                 print("YOUR SCORE IS",c)
           else:
                 print('Oops! You Loose it')
           print("-------------------------------------------------------------------------------")
           a=input(" ")
         else:
             m1=random.randrange(50,101,2)
             m2="i^"+str(m1)+"  (where 'i' is iota) = "
             m3=int(input(m2))
             if m3== -1 and m1%4==2:
                  print("YOU GOT IT RIGHT:)")
                  c+=10
                  print("YOUR SCORE IS",c)
             if m3== 1 and m1%4==0:
                  print("YOU GOT IT RIGHT:)")
                  c+=10
                  print("YOUR SCORE IS",c)
             else:
                  print('Oops! You Loose it')
             print("-------------------------------------------------------------------------------")
             a=input(" ")
print("You scored ",c,"points")
if c>=40:
    print("you played well")
if c==50:
    print("YOU ARE THE CHAMPION")