def agefun(g):#how to define and call a function
    age=eval(input("Enter your age:- "))
    if age > g:
        print("You are adult")
    elif age < g:
        print("You are teenager")
    else:
        print("Enter the correct age")
g=18
agefun(g)
def Scholarship_marks(E):#another example of defining and calling a function
    marks=int(input("Enter your marks:- "))
    if marks > E:
        print("You are eligible")
    elif marks < E:
        print("Try next time")
    else:
        print("Enter the right marks:-")
E=85
Scholarship_marks(E)









def Agefunction(f):
    age=eval(input("Enter your Age:- "))
    if age > f:
        print("You are eligible")
    elif age < f:
        print("you are not eligible")
    else:
        print("enter right age")
f=18
Agefunction(f)


def merit_form(M):
    marks=int(input("Enter your marks"))
    if marks > M:
        print("Congratulation you get scholarship")
    elif marks < M:
        print("Better luck next time")
    else:
        print("Enter correct marks")
M=90
merit_form(M)