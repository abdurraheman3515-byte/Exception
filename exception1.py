for i in range(5):
    try:
        n1=int(input("Enter First number: "))       
        n2=int(input("Enter Second number: ")) 
        print(f"Multiplication = {n1*n2}") 
    except Exception as e:
         print(e)
#============================================================================================
try:
     l=[25,7,8,9,6,3]
     print(l[0])
     print(l[3])
     print(l[15])
except Exception as e:
     print(e)         
#============================================================================================
try:
    with open("data.txt","r") as f1:
        print(f1.read())
        f1.close()
except Exception as e:
    print(e)