class SubfieldsInAI:
    def Subfields():
        print("Sub-fields in AI are: ")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        
        
class OddEven:
    def OddEven():
        num=int(input("Enter the number: "))
        if(num%2==1):
            print(num, "is Odd number")
        else:
            print(num, "is Even number")
            
class FindPercent:
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
    
class triangle:
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