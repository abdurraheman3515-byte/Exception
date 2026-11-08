import csv

field = [
    "empid", "empname", "gender", "age","department", "role", "city", "salary"
]


def creat_file():
    with open("employees3.csv", "w", newline="") as fw:
        csvwriter = csv.DictWriter(fw, fieldnames=field)
        csvwriter.writeheader()
    print("File created successfully!")


def write_records():
    with open("employees3.csv", "a", newline="") as fw:
        csvwriter = csv.DictWriter(fw, fieldnames=field)
        emp = dict()
        empid = int(input("Enter Employee ID: "))
        emp.update({"empid": empid})
        empname = input("Enter Employee Name: ")
        emp.update({"empname": empname})
        gender = input("Enter Employee Gender: ")

        if gender in ("male", "female","Male","Female"):
            emp.update({"gender": gender})
        else:
            print("Invalid Gender!")

        age = int(input("Enter Employee Age: "))
        if age>=20 and age <= 50:
            emp.update({"age": age})
        else:
            print("Invalid Age!")

        department = input("Enter Employee Department: ")
        if department in ("It", "Hr", "Sales", "Finance"):
            emp.update({"department": department})
        else:
            print("Invalid Department!")

        role=input("Enter role :")
        emp.update({"role":role})

        city = input("Enter Employee City: ")
        emp.update({"city":city})

        salary = int(input("Enter Basic Salary: "))
        if salary>=20000 and salary <= 100000:
            emp.update({ "salary": salary})
        else:
            print("Invalid Salary! Salary must be between 20000 and 100000.")

        csvwriter.writerow(emp)
        print("Employee record added successfully!")



def display_Record():
    with open("employees3.csv", "r", newline="") as fr:
        csvReader = csv.DictReader(fr)
        record = list(csvReader)
        for emp in record:
            print(emp)

        return record            



def checkid():
    id = int(input("Enter Employee ID to search: "))
    found = False
    allrecord = display_Record()
    for r in allrecord:
        if id == int(r["empid"]):
            print(r)
            found = True

    if found == False:
        print("ID not found!")


def male_salary(g,s):
    record=display_Record()
    for r in record:
        if r["gender"]==g and float(r["Basic_salary"])>s:
            print(r)




def display_Acending():
    record=display_Record()
    temp=dict()
    for i in range(len(record)):
        for j in range(i+1,len(record)):
            if record[i]["empname"]>record[j]["empname"]:
                temp=record[i]
                record[i]=record[j]
                record[j]=temp
        for r in record:
            print(r)



def increment():
    record=display_Record()
    for r in record:
        if r["department"]=="Support":
            r["basis_salary"]= r["basis_salary"]*0.1+ r["basis_salary"]

    for r in record:
        print(r)
        '''  
def increment():
    record = display_Record()

    for r in record:
        if r["department"] == "Support":
            r["salary"] = int(r["salary"]) + 200

    print("\nAfter Increment:")
    for r in record:
        print(r)
        '''


 
creat_file()
write_records()
display_Record()
checkid()
male_salary("Male", 30000)
display_Acending()
increment()        












































