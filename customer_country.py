import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

outfile = open('customer_country.csv', 'w', newline='')

next(csvfile) # This skips first line
writer = csv.writer(outfile, delimiter=',')
header = ['Full Name', 'Country']
writer.writerow(header)
count = 0

for record in csvfile:
    full_name = record[1] + ' ' + record[2]
    country = record[4]
    data = [full_name, country]
    writer.writerow(data)
    count = count + 1

print(count)
outfile.close()