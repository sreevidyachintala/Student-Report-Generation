import random
import csv
import datetime
#pre-defined list of names included in names.py
import names

#filename with current time
dt = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
filename = 'StudentData'+dt+'.csv'
#report file
report = 'Report'+dt+'.txt'
#By default gave it to generate 4000 students data
num = 4000
myfile = open(filename,'w', newline='')
columnTitleRow = "Student Name, Subject-I \n"
myfile.write(columnTitleRow)

for i in range(num):
    #Random Name Generation using names.py data    
    name = random.choice(names.first_names)+' '+random.choice(names.last_names)
    #Random Marks Generation
    s1 = random.randint(0,100)
    row = [name,s1]
    wr = csv.writer(myfile)
    wr.writerow(row)
#close file
myfile.close()

#reading csv file
#marks list variable for storing all student marks
marks = []
with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None) # skip header line
        for tot,row in enumerate(readCSV):
                marks += [int(row[1])]

        fcount=scount=tcount=flcount = 0
        for fc in marks:
                if(fc>=80):
                        fcount += 1
                elif(fc>65 and fc<80):
                        scount += 1
                elif(fc>45 and fc<65):
                        tcount += 1
                elif(fc<30):
                        flcount += 1                

rp = open(report,'w')

#writing to text file Total Students,First Class,Second Class,Third Class,Failed Students,Highest Mark,Average Mark,Lowest Mark 
rp.write("Student Report - Dated on "+str(datetime.datetime.now())+"\n\n\n")
rp.write("Total Students:"+str(len(marks))+"\n")
rp.write("Highest Mark:"+str(max(marks))+"\n")
rp.write("Lowest Mark:"+str(min(marks))+"\n")
rp.write("Average Mark:"+str(sum(marks)/len(marks))+"\n")
rp.write("First Class:"+str(fcount)+"\n")
rp.write("Second Class:"+str(scount)+"\n")
rp.write("Third Class:"+str(tcount)+"\n")
rp.write("Failed Students:"+str(flcount)+"\n")

#close file
rp.close()

print(filename+ " Generated Successfully")
print(report+ " Generated Successfully")
