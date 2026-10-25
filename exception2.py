# Handle Multiple Exception
# Handle any type of exception
# Handle Custome Exception
# use of finally
# use of else
class InvalidageException(Exception):
    def __init__(self,message,age):
        self.message=message
        self.age=age
  
    def __str__(self):
        return f"{self.message} and {self.age}"

class InvalidmarksExeption(Exception):
     def __init__(self,message,marks):
            self.message=message
            self.age=marks
      
     def __str__(self):
            return f"{self.message} and {self.marks}"

try :
   age=int(input("Enter staff age"))
   marks=int(input("Enter staff marks"))
   a=int(input("Enter your firt number"))     
   b=int(input("Enter your second number"))
   c=a+b
   d=a-b
   e=a*b
   f=a/b
   if age>20 and age<60:
      raise InvalidageException(age,"Age must be between 20 to 60") 
   if marks>0 and age<100:
      raise InvalidmarksExeption(marks,"Marks is between 0 to 100") 

except ValueError:
    print("Invalid Value enterted")

except ZeroDivisionError:
    print("You cannot divide a number by zero!")

except InvalidageException as e:
    print(e)

except InvalidmarksExeption as e:
    print(e)
    
except Exception as e:
    print("Some Error has occured:",e)

else:
    # if no exception occur, this block will run 
    print("No exception occured")
    print(c,d,e,f,sep="\t")
   
finally:
    # this block will run in any case
    print("Your program  is finished!")
    
     













        