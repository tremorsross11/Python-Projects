
import os

directory = os.fsencode("pythontest")
    
for file in os.listdir("C:\pythontest"):
     filename = os.fsdecode(file)
     if filename.endswith(".txt"): 
         print(os.path.join("pythontest", "test2.txt", "test1.txt"))
         continue
     else:
         continue
