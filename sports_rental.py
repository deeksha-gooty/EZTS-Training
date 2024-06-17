#The Sports Equipment Rental System with Dictionary as Database

import sys
import random
from datetime import datetime

class Sports_rental:
    def __init__(self):
        self.sports_equipment={111:{'name':"Basket Ball 1",'condition':"Good",'status':"available"},
                               435:{'name':"Cricket Ball 1",'condition':"Average",'status':"available"},
                               723:{'name':"Racket",'condition':"Bad",'status':"available"}}
        self.record={}
    def create_equipment(self):
        while (True):
            eid=random.randint(100,999)
            if eid not in self.sports_equipment:
                print("Enter the new Equipment Details:")
                print("Name:")
                name=input()
                print("Condition:")
                cond=input()
                print("Status:")
                stu=input().lower()
                self.sports_equipment[eid]={'name':name,'condition':cond,'status':stu}
                print("Equipment add Successfully")
                print("Equipment ID is : ",eid)
                break
    def update_equipment(self,eid):
        if eid not in self.sports_equipment:
            print("Equipment ID not Found")
        else:
            print("Update the Equipment Id")
            while(True):
                field=input("Enter the field to be updatad: (or 'exit' to go back) ").lower()
                if field=='exit':
                    break
                else:
                    if field in self.sports_equipment[eid]:
                        if field=='condition':
                            nval=input("Enter new value:")
                            del(self.sports_equipment[eid][field])
                            self.sports_equipment[eid][field]=nval
                            print(f"The {field} updated successfully")
                            break
                        else:
                            print("Invalid field!......Try again!")
    def borrow_equipment(self):
        print("Enter the Details:")
        usn=input("USN : ")
        name=input("Name : ")
        eid=int(input("EID :"))
        if eid not in self.sports_equipment:
            print("EID not found!... Enter a valid EID")
        else:
            if self.sports_equipment[eid]['status']!='available':
                print("Equipment Not Available")
            else:
                while(True):
                    tid=random.randint(1000,9999)
                    if tid not in self.record:
                        del(self.sports_equipment[eid]['status'])
                        self.sports_equipment[eid]['status']="Not Available"
                        time=datetime.now()
                        t=time.strftime("%H:%M:%S")
                        d=time.strftime("%a %M %Y")
                        tb=d+" "+t
                        self.record[tid]={'usn':usn,'name':name,'eid':eid,'tb':tb,'tr':"--"}
                        print(f"The Equipment {eid} Borrowed Successfully by {usn}")
                        print(f"The Tracker ID is {tid}")
                        break
    
    def return_equipment(self,tid):
        if int(tid) not in self.record:
            print("Invalid Tracker ID!.........Try Agani!")
        else:
            if self.record[tid]['tr']=="--":
                time=datetime.now()
                t=time.strftime("%H:%M:%S")
                d=time.strftime("%a %M %Y")
                tr=d+" "+t
                del(self.record[tid]['tr'])
                self.record[tid]['tr']=tr
                print(f"Equipment {self.record[tid]['eid']} Returned Successfully!")
            else:
                print("Enter correct TID")
    def sport_equipment_tracker(self):
        if len(self.record)==0:
            print("Record Is Empty")
        else:
            print("The Tracker Records")
            print("USN \t\t Name\t\t EID\t Borrow Time\t\t Return Time")
            for i in self.record:
                print("%-15s\t %-15s %d\t %-20s\t %-20s"%(self.record[i]['usn'],self.record[i]['name'],self.record[i]['eid'],self.record[i]['tb'],self.record[i]['tr']))

s=Sports_rental()
while True:
    print("\n1.Create 2.Update 3.Borrow 4.Return 5.Equipment Tracker 6.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        s.create_equipment()
    elif ch==2:
        eid=int(input("Enter Equipment ID: "))
        s.update_equipment(eid)
    elif ch==3:
        s.borrow_equipment()
    elif ch==4:
        tid=int(input("Enter Tracker ID: "))
        s.return_equipment(tid)
    elif ch==5:
        s.sport_equipment_tracker()
    elif ch==6:
        sys.exit()
    else:
        print("Invalid Choice")
        
                
        
            
