count1 = []
count2 = []
count3 = []
count4 = []
log = []
n = 0
x = 0
y = 0
i = 0

text_to_search = input("Text you want to search?\n")
text_to_replace = input("Text you want to replace it with?\n")
file = 'D:\\readme.txt'
temp_file = open(file, 'r')
lines = temp_file.readlines()
for line in lines:
    count1.append(line.count(text_to_search))
    n = n + 1

for line in lines:
    count2.append(line.count(text_to_replace))
    x = x + 1
temp_file.close()

temp_file1 = open(file, 'r')
file_data = temp_file1.read()
file_data = file_data.replace(text_to_search, text_to_replace)
temp_file1 = open(file, 'w')
temp_file1.write(file_data)
temp_file1.close()

temp_file2 = open(file, 'r')
lines1 = temp_file2.readlines()
for line in lines1:
    count3.append(line.count(text_to_replace))
    count4.append(count3[y] - count2[y])
    y = y + 1
temp_file2.close()
while i < n:
    log.append(("\n LINE " + str(i+1) + ":  " + text_to_search + " has occurred " + str(count1[i]) + " times and is replaced by " + text_to_replace + " " + str(count4[i]) + " times.\n"))
    i = i+1
log_file = open("D:\\log.txt", "w")
title = "Input file = readme.txt.\nSearched string:" + text_to_search + "\nReplaced string:" + text_to_replace
log_file.write(title)
i = 0
while i < n:
    log_file.write(log[i])
    i = i+1
