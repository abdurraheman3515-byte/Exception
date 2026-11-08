import csv

with open("employees2.csv", "r") as fr:
    csvReader = csv.DictReader(fr)
    totel=0
    for l in csvReader:
       if l["gender"]=="Male":
        l["basic_salary"]=str(int(l["basic_salary"])+0.1*int(l["basic_salary"]))
        print(l)

   