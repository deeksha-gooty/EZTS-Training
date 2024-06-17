#Sprots Equipment Rental System Created By Using File Handling As The Database.

import sys
import os
import random
from datetime import datetime

class Sports_rental:
    def __init__(self):
        self.eid_lst=[]
        self.fields=[]
        self.tid_lst=[]
        self.records=[]
    def create_equipment(self):
        while (True):
            eid=random.randint(100,999)
            with open("sports_equipment.txt","a+b") as se:
                data=se.readlines()
                for i in data:
                    self.eid_lst.append((i[:3].decode('utf-8')))
                    self.fields.append(i[4:].decode('utf-8').split("|"))
                if eid not in self.eid_lst:
                    print("Enter the new Equipment Details:")
                    print("Name:")
                    name=input().capitalize()
                    print("Condition:")
                    cond=input().capitalize()
                    print("Status:")
                    stu=input().capitalize()
                    with open("sports_equipment.txt","a+b") as se:
                        stm=(f"{eid}|{name}|{cond}|{stu}\n")
                        se.write(stm.encode())
                    se.close()
                    print("Equipment add Successfully")
                    print("Equipment ID is : ",eid)
                    break
        self.eid_lst.clear()

    def update_equipment(self,eid):
        with open("sports_equipment.txt","r+b") as se:
            data=se.readlines()
            for i in data:
                self.eid_lst.append((i[:3].decode('utf-8')))
                self.fields.append(i[4:-1].decode('utf-8').split("|"))
            if eid not in self.eid_lst:
                print("Equipment ID not Found")
            else:
                print("Update the Equipment Id")
                while(True):
                    field=input("Enter the field to be updatad: (or 'exit' to go back) ").lower()
                    if field=='exit':
                        break
                    else:
                        if field=='condition':
                            nval=input("Enter new value:").capitalize()
                            self.fields[self.eid_lst.index(eid)][1]=nval
                            se.seek(0)
                            se.truncate()
                            for i in self.eid_lst:
                                n=f"{i}|{self.fields[self.eid_lst.index(i)][0]}|{self.fields[self.eid_lst.index(i)][1]}|{self.fields[self.eid_lst.index(i)][2]}\n"
                                se.write(n.encode())
                            print(f"The {field} updated successfully")
                            break
                        elif field=='status':
                            nval=input("Enter new value:").capitalize()
                            self.fields[self.eid_lst.index(eid)][2]=nval
                            se.seek(0)
                            se.truncate()
                            for i in self.eid_lst:
                                n=f"{i}|{self.fields[self.eid_lst.index(i)][0]}|{self.fields[self.eid_lst.index(i)][1]}|{self.fields[self.eid_lst.index(i)][2]}\n"
                                se.write(n.encode())
                            print(f"The {field} updated successfully")
                            break
                        else:
                            print("Invalid field!......Try again!")
            self.eid_lst.clear()
            self.fields.clear()
            se.close()

    def borrow_equipment(self):
        print("Enter the Details:")
        usn=input("USN : ")
        name=input("Name : ").capitalize()
        eid=input("EID :")
        with open("sports_equipment.txt","r+b") as se:
            data=se.readlines()
            for i in data:
                self.eid_lst.append((i[:3].decode('utf-8')))
                self.fields.append(i[4:-1].decode('utf-8').split("|"))
            if eid not in self.eid_lst:
                print("EID not found!... Enter a valid EID")
            else:
                if self.fields[self.eid_lst.index(eid)][2]!='Available':
                    print("Equipment Not Available")
                else:
                    while(True):
                        tid=random.randint(1000,9999)
                        with open("records.txt","a+b") as re:
                            data=re.readlines()
                            for i in data:
                                self.tid_lst.append((i[:4].decode('utf-8')))
                                self.records.append(i[5:].decode('utf-8').split("|"))
                            if tid not in self.tid_lst:
                                self.fields[self.eid_lst.index(eid)][2]="Not Available"
                                se.seek(0)
                                se.truncate()
                                for i in self.eid_lst:
                                    n=f"{i}|{self.fields[self.eid_lst.index(i)][0]}|{self.fields[self.eid_lst.index(i)][1]}|{self.fields[self.eid_lst.index(i)][2]}\n"
                                    se.write(n.encode())
                                time=datetime.now()
                                t=time.strftime("%H:%M:%S")
                                d=time.strftime("%a %M %Y")
                                tb=d+" "+t
                                tr="Not Returned"
                                stm=(f"{tid}|{usn}|{name}|{eid}|{tb}|{tr}\n")
                                re.write(stm.encode())
                                print(f"The Equipment {eid} Borrowed Successfully by {usn}")
                                print(f"The Tracker ID is {tid}")
                                break
                        re.close()
        se.close()
        self.eid_lst.clear()
        self.fields.clear()
        self.records.clear()
        self.tid_lst.clear()
    
    def return_equipment(self,tid):
        with open("records.txt","r+b") as re:
            data=re.readlines()
            for i in data:
                self.tid_lst.append((i[:4].decode('utf-8')))
                self.records.append(i[5:-1].decode('utf-8').split("|"))
            if tid not in self.tid_lst:
                print("Invalid Tracker ID!.........Try Agani!")
            else:
                if self.records[self.tid_lst.index(tid)][4]=="Not Returned":
                    time=datetime.now()
                    t=time.strftime("%H:%M:%S")
                    d=time.strftime("%a %M %Y")
                    tr=d+" "+t
                    self.records[self.tid_lst.index(tid)][4]=tr
                    re.seek(0)
                    re.truncate()
                    for i in self.tid_lst:
                        idx=self.tid_lst.index(i)
                        n=(f"{i}|{self.records[idx][0]}|{self.records[idx][1]}|{self.records[idx][2]}|{self.records[idx][3]}|{self.records[idx][4]}\n")
                        re.write(n.encode())
                    eid=self.records[self.tid_lst.index(tid)][2]
                    with open("sports_equipment.txt","r+b") as se:
                        data=se.readlines()
                        for i in data:
                            self.eid_lst.append((i[:3].decode('utf-8')))
                            self.fields.append(i[4:-1].decode('utf-8').split("|"))  
                        self.fields[self.eid_lst.index(eid)][2]="Available"
                        se.seek(0)
                        se.truncate()
                        for i in self.eid_lst:
                            n=f"{i}|{self.fields[self.eid_lst.index(i)][0]}|{self.fields[self.eid_lst.index(i)][1]}|{self.fields[self.eid_lst.index(i)][2]}\n"
                            se.write(n.encode())
                    se.close()
                    print(f"Equipment {eid} Returned Successfully!")
                else:
                    print("Enter correct TID")
        re.close()
        self.eid_lst.clear()
        self.fields.clear()
        self.records.clear()
        self.tid_lst.clear()

    def sport_equipment_tracker(self):
        print("The Tracker Records")
        print("TID\tUSN \t\tName\t\tEID\tBorrow Time\t\tReturn Time")
        data=[]
        with open("records.txt","r+b") as re:
            d=re.readlines()
            for i in d:
                data.append(i.decode('utf-8').split("|"))
            for i in data:
                print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\n")
            
        re.close()

s=Sports_rental()
while True:
    print("\n1.Create 2.Update 3.Borrow 4.Return 5.Equipment Tracker 6.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        s.create_equipment()
    elif ch==2:
        eid=input("Enter Equipment ID: ")
        s.update_equipment(eid)
    elif ch==3:
        s.borrow_equipment()
    elif ch==4:
        tid=input("Enter Tracker ID: ")
        s.return_equipment(tid)
    elif ch==5:
        s.sport_equipment_tracker()
    elif ch==6:
        sys.exit()
    else:
        print("Invalid Choice")