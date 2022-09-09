import csv
import calendar

infile = open('steps.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

outfile = open('avg_steps.csv', 'w', newline='')

next(csvfile) # This skips first line
writer = csv.writer(outfile, delimiter=',')
header = ['Month', 'Steps']
writer.writerow(header)

total_steps = 0
current_month = 1
count = 0

for row in csvfile:
    if int(row[0]) == current_month:
        count += 1
        total_steps += int(row[1])

    else:
        average = round((total_steps / count), 2)
        month_name = calendar.month_name[int(row[0])]
        data = [month_name, average]
        writer.writerow(data)
        current_month = int(row[0])
        total_steps = int(row[1])
        count = 1

outfile.close()