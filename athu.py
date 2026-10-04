x= 5
y=7
v=x+y
print(v)

d= x-y
print(d)
bacche = []
def add_student():
    name = input("enter name :")
    roll = int(input("enter roll no:"))
    marks = float(input("enter marks : "))

    student = {
        "name":name,
        "roll":roll,
        "marks":marks
    }
    bacche.append(student)
    print("student added")

def calculate_res():
    for b in bacche:
        
        if b["marks"] >= 85:
            print("Grade A")
        elif b["marks"] > 75 and b["marks"] <85:
            print("Grade B")
        elif b["marks"] <75 and b["marks"] > 50:
            print("Grade C")
        else :
            print("Fail")

def view_student():
    for b in bacche:
        print("Name :",b["name"])
        print("Roll No:",b["roll"])
        print("Marks:",b["marks"])

def main():
    while True:
        print("1. Add Student")
        print("2. View Student")
        print("3. Calculate Result")
        print("4. Exit")
        choice = (input("Enter you choice :"))

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            calculate_res()
        elif choice == "4":
            print("Thank you for using Student Analyzer!")
            break
        else :
            print("Invalid choice. Try again.")

main()
