import csv

infile = open('EmployeePay.csv', 'r')
csvfile = csv.reader(infile,delimiter= ',')
next(csvfile)
count = 0
for record in csvfile:
    idcode = record[0]
    full_name = record[1] + ' ' + record[2]
    salary = record[3]
    bonus = record[4]
   
    print('ID: ', idcode)
    print('Name: ', full_name)
    print('Salary: ', salary)
    print('Bonus: ', bonus)
    print('Total Pay:', str((int(record[3]) + int(record[3]) * float(record[4]))))

    input()
    

    count = count + 1