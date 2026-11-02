import os
'''
with open ("All_Data.txt","r") as fr, open("salary.txt","w") as fw:
    fileData=fr.readlines()
    for line in fileData:
        l=list(line.split())
        print(l)
'''

import os

class FileOperation:
    def __init__(self, source, n):
        self.source = source
        self.n = n

    def copyData(self, fileData):
        os.chdir("D:\\")

        with open(self.source, "r") as fr, open("salary.txt", "w") as fw:

            fileData = fr.readlines()
            for line in fileData:
                l = list(line.split())
                fw.write(f"{' '.join(l)}\n")


C1 = FileOperation("All_Data.txt", 1)
C1.copyData(None)

print("Data copied successfully!")