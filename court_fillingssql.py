import mysql.connector as mc
import random
import os
from time import time

time_start = time()
db = mc.connect(user="root",passwd="root", db="courtfill")
c = db.cursor()

MENU = """
++++++++++++++++++++++++++++++
C O U R T    F I L I L I N G S
==============================
-------------MENU-------------
==============================
++ 0. Main Menu
++ 1. Input new case
++ 2. Finding file of case
++ 3. Similar cases
++ 4. Verdicts
++ 5. Archive
++ 6. Simplified view of Archive
++ 7. Misinput deletion
++ 8. About judge
++ 9. Total cases
++ 10. Completed cases
++ 11. Pending cases
++ 12. Ongoing cases
++ 13. Juvenile cases
++ 99. Exit
++ clear(to clear the screen)
++++++++++++++++++++++++++++++
"""
print(MENU)

random_judge  = random.randint(1,4)


def get_data():
    query = "select * from haha"
    x = c.execute(query)
    raw_data = c.fetchall()
    data=[]
    for i in raw_data:
        g={}
        g["name"] = i[1]
        g["age"] = i[2]
        g["gender"] = i[3]
        g["charge"] = i[4]
        g["status"] = i[5]
        g["verdict"] = i[6]
        data.append(g)
    return data


    
while True:
    data = get_data()
    choice = input("\nEnter your choice(press 0 for menu): ")
    choice = choice.lower()
    if choice == "0":
        print(MENU)
    elif choice == "1":
        x = {}
        name = input("\nEnter the name of the suspect : ")
        name = name.title()
        x["name"] = name
        age = input("Enter the age of " +name +": ")
        x["age"] = age
        gender = input("Enter the gender of "+name +"(press '0' if you dont want to specify): ")
        gender = gender.title()            
        x["gender"] = gender
        charge = input("Enter the charge on "+name + ": ")
        charge = charge.capitalize()
        x["charge"] = charge
        while True:
            status = input("Enter the status of "+name +" (1: pending, 2: ongoing, 3: completed): ")
            if status == "1":
                status = "Pending"
                verdict = "To be written"
                break
            elif status == "2":
                status = "Ongoing"
                verdict = "To be written"
                break
            elif status == "3":
                status = "Completed"
                verdict = input("Enter the verdict of "+name + ": ")
                verdict = verdict.capitalize()
                break
            else:
                print("Please enter a valid number!")
        x["status"] = status
        x["verdict"] = verdict
        x["status"] = status
        x["verdict"] = verdict
        p=[]
        for i in x:
            p.append(x[i])

        query = "insert into haha values("+str(len(data)+1)+", '"+str(p[0])+"', "+str(p[1])+", '"+str(p[2])+"', '"+str(p[3])+"', '"+str(p[4])+"', '"+str(p[5])+"')"
        c.execute(query)
        db.commit()

    elif choice == "2":
        namo = input("Enter the name to be found: ")
        namo = namo.title()
        choice2 = 0
        for i in data:
            name_found = i["name"]
            if name_found == namo:
                choice2+=1
                print(i)
        if choice2 == 0:
            print("Not found")

    elif choice == "3":
        cases = input("Enter similar cases to be found: ")
        cases = cases.capitalize()
        choice3 = 0
        for i in data:
            cases_found = i["charge"]
            if cases_found == cases:
                choice3+=1                
                print(i)
        if choice3 == 0:
            print("Not found")

    elif choice == "4":
        name_verdict = input("Enter name of the suspect whose verdict is to be found: ")
        name_verdict = name_verdict.title()
        choice4 = 0
        for i in data:
            if i["name"]==name_verdict:
                print("Name =",i["name"])
                print("Verdict =",i["verdict"])
                choice4+=1
        if choice4==0:
            print("Not found")

    elif choice == "5":
        for i in data:
            print(i)
            
    elif choice == "6":
        choice6 = 1
        for i in data:
            print("Case", str(choice6))
            print("Name =",i["name"])
            print("Age =",i["age"])
            print("Gender =",i["gender"])
            print("Charge =",i["charge"])
            print("Status =",i["status"])
            print("Verdict =",i["verdict"])
            choice6+=1
            print()

    elif choice == "7":
        mis_input = input("Enter the name of the suspect whose case is to be deleted: ")
        mis_input = mis_input.title()
        for i in data:
            if i["name"]== mis_input:
                print(i)
                while True:
                    confirm = input("Do you want to delete this misinput file: (y/n) ")
                    confirm =confirm.title()
                    if confirm == "Y":
                        query = "delete from haha where Name='"+str(mis_input)+"'"
                        print(query)
                        c.execute(query)
                        db.commit()
                        print("Successfully deleted the file")
                        break
                    elif confirm == "N":
                        print("Not deleted")
                        break
                    else:
                        print("Please enter a valid argument")

    elif choice == "8":
        if random_judge == 1:
            print("Krishna Murari (born: 9 July 1958) is a Judge of Supreme Court of India and former Chief Justice of Punjab and Haryana High Court. He has also served as Judge of Allahabad High Court till his elevation as Chief justice of Punjab and Haryana High Court")
        elif random_judge == 2:
            print("V. Ramasubramanian (born 30 June 1958) is a Judge of Supreme Court of India. He is former Chief Justice of Himachal Pradesh High Court. He is also former Judge of Madras High Court and Telangana High Court.")
        elif random_judge == 3:
            print("Justice Shripathi Ravindra Bhat (born 21 October 1958) is a Judge of Supreme Court of India. He is former Chief Justice of Rajasthan High Court. He is also former Judge of Delhi High Court. ")
        elif random_judge == 4:
            print("Hrishikesh Roy (born 1 February 1960) is a Judge of Supreme Court of India. He is former Chief Justice of the Kerala High Court. He is also former Judge of Gauhati High Court. ")

    elif choice == "9":
        print("Total cases are:",len(data))

    elif choice == "10":
        completed_cases = 0
        for i in data:
            if i["status"]=="Completed":
                completed_cases+=1
                print(i)
        print("Total completed cases are:", completed_cases)

    elif choice == "11":
        pending_cases = 0
        for i in data:
            if i["status"]=="Pending":
                pending_cases+=1
                print(i)
        print("Total pending cases are:", pending_cases)

    elif choice == "12":
        ongoing_cases = 0
        for i in data:
            if i["status"]=="Ongoing":
                ongoing_cases+=1
                print(i)
        print("Total ongoing cases are:", ongoing_cases)

    elif choice == "13":
        juvenile_cases = 0
        for i in data:
            if int(i["age"]) < 18 :
                juvenile_cases+=1
                print(i)
        print("Total juvenile cases are:", juvenile_cases)

    elif choice == "99":
        print("Time Used", str(int(time()-time_start)), "seconds")
        print("Thank  you for using me!\nHave a nice day\nExiting...")
        break

    elif choice == "":
        pass

    elif choice == "clear":
        os.system('cls')
        # print("\n"*39)
    
    else:
        print("Enter a valid choice")
