# datetime
import datetime
from datetime import date
today = date.today()
print("Today's date:", today)
#
file = open("example.txt", "r")
#Reading a file
file = open("example.txt", "r")
content = file.read() 
lines = file.readlines() 
line = file.readline()
print(content)
file.close()
#opening file
import os
if os.path.exists("example.txt"):
    file = open("example.txt", "r")
    print("File opened successfully.")
else:
    print("File does not exist.")
#write file
with open("example.txt", "w") as file:
    file.write("Hello, World!")
#Appending a file
with open("example.txt", "a") as file:
    file.write("\nNew Line Added.") 
# creating directory
import os
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
#Listing files in directory
files = os.listdir(".")

for file in files:
    print(file)
# Logging system
def log_activity(activity):
    with open("log.txt", "a") as log_file:
        log_file.write(activity + "\n")

log_activity("User logged in.")
log_activity("User uploaded a file.")