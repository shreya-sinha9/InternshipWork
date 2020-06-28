import re

file = 'D:\\Error.txt'
temp_file = open(file, 'r')
lines = temp_file.readlines()
temp_file.close()
count = {}
data = []

log_file = open("D:\\log2.txt", "w")
pattern = re.compile(r'[a-zA-Z]+Error:')
for line in lines:
    for match in re.finditer(pattern, line):
        # print(line)
        if line not in count:
            count[line] = 1
        else:
            count[line] += 1
        data.append(line)
for d in data:
    file_write = d + "occurred " + str(count[d]) + " times\n"
    log_file.write(file_write)



