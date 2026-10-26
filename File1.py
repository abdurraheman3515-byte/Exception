import os
os.chdir("D:\\")
print(os.getcwd())

#Read mode
try:
    with open("readdata.txt", "r") as fr:
        data = fr.read()
        print(data)

except FileNotFoundError:
    print("The file is not found")
#=======================================================================================================
#write mode
try:
    with open("writedata.txt", "w") as fw:
        fw.write("Hello World!")
        fw.write("\nWelcome to Python.")

    print("Data written successfully.")

except:
    print("File could not be written.")


#======================================================================================================
#apend mode
try:
    with open("readdata.txt","a") as fa:
        fa.write("New content into the file")
        fa.write(input("enter some text: "))
        fa.close()
except FileNotFoundError:
    print("Unable to create file!")   
    

