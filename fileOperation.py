import os
class InvalidGenderException(Exception):
        def __init__(self):
            pass
        def __str__(self):
            return "Please Enter M for Male and F for Female!"

class InvalidMarksException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "please Enter only 3 subjects"


class FileOperation:
    def __init__(self,n,file_name):
        os.chdir("D:\\FileOperations")
        self.n=n
        self.file_name=file_name


    def writeData(self):
        Allstudent=[]
        try:
            for i in range(self.n):
                r=int(input("Enter Roll no : "))
                name=input("Enter Name :  ")
                gender=input("Enter Gender :  ")
                if gender not in("M","F"):
                    raise InvalidGenderException
                marks=list(map(int,input("Enter marks in three subject :  ")))
                totel=sum(marks)
                percent=round(totel/len(marks),2)
                student=[r,name,gender,marks,totel,percent]
                Allstudent.append(student)

                f1=open(self.file_name,"w")
                for l in Allstudent:
                    for data in l: 
                        if isinstance(data,list):
                            for x in data:
                                f1.write(str(x)+" ")
                        else:
                            f1.write(str(data)+" ")
                    f1.write("\n")
                f1.close()
                print("All Data Added to the file!")

        except ValueError:
            print("Please Enter Value In  Integer format Only !")
        
        except InvalidGenderException as e:
            print(e)

        except InvalidMarksException as e:
            print(e)

        except FileNotFoundError:
            print("The File not found or you are in only Read Mode")

        except Exception as e:
            print(e)


    def backUpData(self):
            os.chdir("D:\\FileOperations")
            f1=open(self.file_name,"r")
            f2=open("backup.txt","w")
            f2.write(f1.read())
            print("File Backup Created!")
            f1.close()
            f2.close()
    
    def addNewStudent(self):
            f3=open(self.file_name,"a")
            print("\n Enter new data! ")
            roll=int(input("Enter Roll Number: "))
            name=input("Enter name: ")
            gender=input("Enter M for Male and F for Female: ")
            marks=list(map(int,input("Enter marks in 3 subjects:").split()))
            total=sum(marks)
            percent=round(total/len(marks),2)
            f3.write(f"{roll} {name} {gender} {marks[0]} {marks[1]} {marks[2]} {total} {percent}\n")
            print("Data Addded to the file!")
            f3.close()
    
    
F1=FileOperation(2,"students.txt")
F1.writeData()
F1.backUpData()
F1.addNewStudent()
    
              


        
            


    
