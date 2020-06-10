import csv
patient_Name=input("Enter patient name\n")
patient_age=int(input("Enter patient age\n"))
patient_phoneNo=int(input("Enter patient phone number\n"))
with open('patients.csv', 'a+') as csvfile:
    patients = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    patients.writerow([patient_Name, patient_age,patient_phoneNo])
print("Records are written successfully")