#APR
#005
#turtle game phase 2 file/io
#10/24/2025

#opening files
data_file = open("myNumbers.txt", "r")
backup_file = open("mybackup.txt", "w")

#processing data and creating backup
reading = True
number_count = 0
number_sum = 0

while reading:
    line = data_file.readline()
    if len(line) == 0:
        reading = False
    else:
        backup_file.write(line)
        number_count += 1
        number_sum += int(line)

#closing files
data_file.close()
backup_file.close()

#printing analyses
print(f"Number Count: {number_count}")
print(f"Number Sum: {number_sum}")
