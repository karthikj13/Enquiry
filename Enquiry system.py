import os
import json

#Function for creating enquries
def Create_enq():
    while True:
        print("Enter the following details:\n")
        date = input("Date (DD/MM/YYYY): ")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        phone_num = int(input("Phone number: "))
        email = input("Email: ")
        dob = input("Date of birth (DD/MM/YYYY): ")
        gender = input("Gender: ")
        address = input("Full address: ")
        course_intrested = input("Course intrested: ")
        demo = input("Demo date (DD/MM/YYYY): ")
        education = input("Educational Background: ")
        passed_out = int(input("Passed out year: "))
        work_exp = input("Work experience? (Y/N) ").upper()
        if work_exp == 'Y':
            experience = input("Work Experience in years: ")
            previous_company = input("Previously worked company: ")
        else:
            experience = "N/A"
            previous_company = "N/A"

        enq_dict = {
                    "date":date,
                    "fullname":{"first name":first_name,
                                "last name":last_name},
                    "dob":dob,
                    "contact":{"phone no":phone_num,
                               "email":email},
                    "address":address,
                    "gender":gender,
                    "course":course_intrested,
                    "edu background":education,
                    "working exp":{"worked status":work_exp,
                                   "working years":experience,
                                   "previous company":previous_company}
                    }

        if os.path.exists("enq.json"):
            f = open("enq.json","at")
        else:
            f = open("enq.json","xt")

        json.dump(enq_dict,f,indent=2)
        f.close()

        print("\nPress 'enter' to add new enquiry or 'Q' to quit..")
        q = input().upper()
        if q == 'Q':break

#Function for viewing enquries
def View_enq():
    if os.path.exists("enq.json"):
        f=open("enq.json")
        fdata=f.readlines()
        s1 = json.dumps(fdata)
        data = json.loads(s1)
        f.close()

        for i in data:
            print(i)


#Main program starts here
while True:
    print("Type 'view' to view enquiries or 'create' to create a new enquiry")
    select = input().upper()

    if select == 'CREATE':
        Create_enq()
        break
    elif select == 'VIEW':
        d = View_enq()
        break
    else:
        print("Enter a valid input\n")
        continue
