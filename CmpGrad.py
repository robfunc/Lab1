''' Activity No. 1 '''

import os
import platform
import time

prelims =""; midterm=""; semifinals=""; final=""; ave="";remarks=""

#clean the screen before starting the code
def clean():
    if platform.system() == "Windows":
        os.system("cls")
        os.system("MODE CON: COLS=82 LINES=17")
    else:
        os.system("clear")
clean()

def col_inputs():
    global prelims; global midterm; global semifinals; global finals; global remarks

    print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")
    print("░▓░▓░▓░▓░▓                    Average Student Grades                    ░▓░▓░▓░▓░▓")
    print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓\n")
    print("░▓░▓░▓░▓░▓ Please Input the grades on required fields!\n")

    prelims =       float(input("░▓░▓░▓░▓░▓     Prelims:\t"))
    midterm =       float(input("░▓░▓░▓░▓░▓     Midterm:\t"))
    semifinals =    float(input("░▓░▓░▓░▓░▓ Semi-Finals:\t"))
    finals =         float(input("░▓░▓░▓░▓░▓      Finals:\t"))
    print("\n")

def calculate():
    global ave; global remarks; global EqGrade
    #calculating the inputted values
    ave = float(prelims+midterm+semifinals+finals)
    ave = float(ave/4)
    '''۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝'''

    #2
    if float(ave) > float("74"):
        remarks= "Passed"
    else:
        remarks = "Failed"

    # To get Equivalent Grade
    if(ave >= 99 and ave <= 100):
        EqGrade = "A"
    elif(ave >= 90 and ave < 99):
        EqGrade = "B"
    elif(ave >= 80 and ave < 90):
        EqGrade = "C"
    elif(ave >= 71 and ave < 80):
        EqGrade = "D"
    elif(ave >= 61 and ave < 71):
        EqGrade = "E"
    else:
        EqGrade = "F"

    '''۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝۝'''

repeat = "Y"

'''Main Procedure'''
while repeat=="Y" or repeat=="y":
    prelims =0; midterm=0; semifinals=0; final=0; ave=0; remarks=""
    clean()
    col_inputs()
    calculate()

    print("░▓░▓░▓░▓░▓ Total Average: " + str(ave)+"\t  Equivalent Grade: "+EqGrade+"\tRemarks: "+remarks+"\n")



    print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")
    repeat = input("░▓░▓░▓░▓░▓ Calculate new Student: ([Y]/[N]) ")


clean()
print("\n\n\n\n\n\n")

print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")
print("░▓░▓░▓░▓░▓               Thank You for using Calculator                 ░▓░▓░▓░▓░▓")
print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓\n")

time.sleep(3)