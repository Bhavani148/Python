class multipleFunctions():
    def oddEven():
        num=int(input("Enter a number"))
        if(num%2==0):
            print(num," is Even number")
            message="Even Number"
        else:
            print(num, " is Odd number")
            message="Odd Number"
        return message
    
    def Eligible():
        gender=input("Enter the Gender: ")
        age=int(input("Enter the Age: "))
        if ((gender == "Male" or gender == "male") and age >= 21) or ((gender == "Female" or gender == "female")and age >= 18):
            return "Eligible"
        else:
            return "Not Eligible"
    
    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        Total = sub1+sub2+sub3+sub4+sub5
        Percentage = Total/5
        print("Total:", Total)
        print("Percentage:", Percentage)
        return Total, Percentage

    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        areaoftriangle = (Height*Breadth)/2
        print("Area of Triangle: ", areaoftriangle)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        perimeteroftriangle = Height1+Height2+Breadth
        print("Perimeter of Triangle: ", perimeteroftriangle)