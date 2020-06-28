import re
import matplotlib.pyplot as plt


def error_day(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    id_count = {}
    p = re.compile(r'ERROR:')
    p1 = re.compile(r'testFailCheck[0-9]')
    for line in lines:
        for match in re.finditer(p, line):
            x = (re.findall(p, line))
            ide = line[len(x[0]) + 1:]
            # print(ide)
            for match in re.finditer(p1, ide):
                y = (match.group())

                if y not in id_count:
                    id_count[y] = 1
                else:
                    id_count[y] += 1
    return id_count


def warning_day(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    id_count = {}
    p = re.compile(r'WARNING')
    p1 = re.compile(r'[A-Za-z_]+:')
    for line in lines:
        for match in re.finditer(p, line):
            x = (re.findall(p, line))
            ide = line[len(x[0]) + 1:]
            # print(ide)
            for match in re.finditer(p1, ide):
                y = (match.group())

                msg = ide[11 + len(match.group()) + 1:]
                # print(msg)

                if y not in id_count:
                    id_count[y] = 1
                else:
                    id_count[y] += 1
    return id_count


def plot_data(days, counts, strings, title):
    i = 0
    while i < int(days):
        f = "D:\\err_war_day" + str(i + 1) + ".txt"
        d = []
        e = []
        if title == "ERROR":
             c1 = error_day(f)
        else:
             c1 = warning_day(f)
        for c in c1:
            d.append(c1[c])
            e.append(c)
        counts.append(d)
        strings.append(e)
        i = i +1
    string = strings[0]
    return string


def disc_list(counts):
    disc = []
    n = len(counts)
    m = len(counts[0])
    for i in range(0, m):
        c21 = []
        for j in range(0, n):
            c21.append(counts[0][i] - counts[j][i])
        disc.append(c21)
    return disc


def plot(type_of_graph, days, disc, string, title):
    day_plot = []
    k = 0
    while k < int(days):
        day_plot.append(k + 1)
        k = k + 1
    i = 0
    if type_of_graph == "Bar":
        for row in disc:
            plt.bar(day_plot, row, label=(string[i]))
            i = i + 1
        plt.legend()
        plt.xlabel('DAYS')
        plt.ylabel('DISC')
        plt.title(title)
        plt.show()

    elif type_of_graph == "Line":
        for row in disc:
            plt.plot(day_plot, row, label=(string[i]))
            i = i + 1
        plt.title(title)
        plt.ylabel('DISC')
        plt.xlabel('DAYS')
        plt.legend()
        plt.grid(True, color='k')
        plt.show()

    else:
        for row in disc:
            plt.scatter(day_plot, row, label=(string[i]))
            i = i + 1
        plt.xlabel('DAYS')
        plt.ylabel('DISC')
        plt.title(title)
        plt.legend()
        plt.show()


days = input("Enter the number of days\n")

# ERROR plot
counts = []
strings = []
title = "ERROR"
print(title + " plot\n")
string = plot_data(days, counts, strings, title)
disc = disc_list(counts)
type_of_graph = input("Enter the type of graph you want: 1)Bar 2)Line 3)Dot\n")
plot(type_of_graph, days, disc, string, title)

# WARNING plot
counts = []
strings = []
title = "WARNING"
print(title + " plot\n")
string = plot_data(days, counts, strings, title)
disc = disc_list(counts)
type_of_graph = input("Enter the type of graph you want: 1)Bar 2)Line 3)Dot\n")
plot(type_of_graph, days, disc, string, title)
