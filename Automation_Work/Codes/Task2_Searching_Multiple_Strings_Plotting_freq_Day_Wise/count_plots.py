import matplotlib.pyplot as plt


def count_day(file, number, string_f):
    temp_file = open(file, 'r')
    file_data2 = temp_file.read()
    j = 0
    count = []
    while j < int(number):
        count.append(file_data2.count(string_f[j]))
        j = j + 1
    temp_file.close()
    return count


# reading the strings which we want to count
no_of_strings = input("Enter the number of strings you want to count\n")
string = []
i = 0
while i < int(no_of_strings):
    string.append(input("Enter string " + str(i + 1) + "\n"))
    i = i + 1

# storing count day wise
counts = []
days = input("Enter the number of days\n")
i = 0
while i < int(days):
    file1 = "D:\\day_" + str(i + 1) + ".txt"
    c1 = count_day(file1, no_of_strings, string)
    counts.append(c1)
    i = i + 1

# plotting
type_of_graph = input("Enter the type of graph you want: 1)Bar 2)Line 3)Dot\n")
day_plot = []
k = 0
while k < int(days):
    day_plot.append(k+1)
    k = k+1
# print(day_plot)
n = len(counts)
m = len(counts[0])
count_string = []
for i in range(0, m):
    c2 = []
    for j in range(0, n):
        c2.append(counts[j][i])
    count_string.append(c2)
# print(count_string)
i = 0
if type_of_graph == "Bar":
    for row in count_string:
        plt.bar(day_plot, row, label=(string[i]))
        i = i + 1
    plt.legend()
    plt.xlabel('DAYS')
    plt.ylabel('COUNT')
    plt.title('Count of Strings Day Wise')
    plt.show()

elif type_of_graph == "Line":
    for row in count_string:
        x = day_plot
        y = row
        plt.plot(x, y, label=(string[i]), linewidth=5)
        i = i + 1
    plt.title('Count of Strings Day Wise')
    plt.ylabel('COUNT')
    plt.xlabel('DAYS')
    plt.legend()
    plt.grid(True, color='k')
    plt.show()

else:
    for row in count_string:
        x = day_plot
        y = row
        plt.scatter(x, y, label=(string[i]))
        i = i + 1
    plt.xlabel('DAYS')
    plt.ylabel('COUNT')
    plt.title('Count of Strings Day Wise')
    plt.legend()
    plt.show()

