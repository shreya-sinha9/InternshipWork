import re
import matplotlib.pyplot as plt
from collections import defaultdict


class Error:

    def __init__(self, days, file):
        self.days = days
        self.file = file

    def error_day(self, file, days, msg_counts, msg_id_link):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        count = {}
        p = re.compile(r'ERROR:')
        p1 = re.compile(r'testFailCheck[0-9]')
        for line in lines:
            for match in re.finditer(p, line):
                x = (re.findall(p, line))

                ide = line[len(x[0]) + 1:]
                for match in re.finditer(p1, ide):
                    y = (match.group())

                    msg = ide[13 + len(match.group()) + 3:]
                    if msg not in count:
                        count[msg] = 1
                    else:
                        count[msg] += 1
                    if msg not in msg_id_link:
                        msg_id_link[msg] = y
        self.correct(msg_counts, count, days)

    def correct(self, msg_counts, count, days):
        for x in count:
            if x not in msg_counts:
                for t in range(0, days - 1):
                    msg_counts[x].append(0)
                msg_counts[x].append(count[x])
            else:
                msg_counts[x].append(count[x])
        for x in msg_counts:
            if len(msg_counts[x]) < days:
                msg_counts[x].append(0)

    def disc(self, msg_counts):
        disc_counts = defaultdict(list)
        for x in msg_counts:
            l = len(msg_counts[x])
            for y in range(0, l):
                disc_counts[x].append(msg_counts[x][0] - msg_counts[x][y])
        return disc_counts

    def error(self):
        i = 0
        msg_counts = defaultdict(list)
        msg_id_link = {}
        days = self.days
        f1 = self.file
        while i < int(days):
            f = f1 + str(i + 1) + ".txt"

            self.error_day(f, i + 1, msg_counts, msg_id_link)
            i = i + 1
        disc_counts = self.disc(msg_counts)
        return disc_counts, msg_id_link


class PLOT:
    def __init__(self, days, type, disc, link, title):
        self.days = days
        self.type = type
        self.disc = disc
        self.title = title
        self.link = link

    def plot(self):
        day_plot = []
        days = self.days
        type_of_graph = self.type
        disc = self.disc
        title = self.title
        link = self.link

        k = 0
        while k < int(days):
            day_plot.append(k + 1)
            k = k + 1
        i = 0
        if type_of_graph == "Bar":
            for row in disc:
                plt.bar(day_plot, disc[row], label=(link[row] + "->" + row))
            plt.legend()
            plt.xlabel('DAYS')
            plt.ylabel('DISC')
            plt.title(title)
            plt.show()
        elif type_of_graph == "Line":
            for row in disc:
                plt.plot(day_plot, disc[row], label=(link[row] + "->" + row))
            plt.title(title)
            plt.ylabel('DISC')
            plt.xlabel('DAYS')
            plt.legend()
            plt.grid(True, color='k')
            plt.show()
        elif type_of_graph == "Dot":
            for row in disc:
                plt.scatter(day_plot, disc[row], label=(link[row] + "->" + row))
            plt.xlabel('DAYS')
            plt.ylabel('DISC')
            plt.title(title)
            plt.legend()
            plt.show()
        else:
            print("WRONG OPTION!!!! Click 1)BAR 2)LINE 3)DOT")


class Warning:

    def __init__(self, days, file):
        self.days = days
        self.file = file

    def war_day(self, file, days, msg_counts1, msg_id_link1):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        count1 = {}
        p = re.compile(r'WARNING:')
        p1 = re.compile(r'[A-Za-z_]+:')
        for line in lines:
            for match in re.finditer(p, line):
                x = (re.findall(p, line))

                ide = line[len(x[0]) + 1:]
                for match in re.finditer(p1, ide):
                    y = (match.group())

                    msg = ide[11 + len(match.group()) + 1:]
                    if msg not in count1:
                        count1[msg] = 1
                    else:
                        count1[msg] += 1
                    if msg not in msg_id_link1:
                        msg_id_link1[msg] = y
        self.correct(msg_counts1, count1, days)

    def correct(self, msg_counts1, count1, days):
        for x in count1:
            if x not in msg_counts1:
                for t in range(0, days - 1):
                    msg_counts1[x].append(0)
                msg_counts1[x].append(count1[x])
            else:
                msg_counts1[x].append(count1[x])
        for x in msg_counts1:
            if len(msg_counts1[x]) < days:
                msg_counts1[x].append(0)

    def disc(self, msg_counts1):
        disc_counts1 = defaultdict(list)
        for x in msg_counts1:
            l = len(msg_counts1[x])
            for y in range(0, l):
                disc_counts1[x].append(msg_counts1[x][0] - msg_counts1[x][y])
        return disc_counts1

    def warn(self):
        i = 0
        msg_counts1 = defaultdict(list)
        msg_id_link1 = {}
        days = self.days
        f1 = self.file
        while i < int(days):
            f = f1 + str(i + 1) + ".txt"

            self.war_day(f, i + 1, msg_counts1, msg_id_link1)
            i = i + 1
        disc_counts1 = self.disc(msg_counts1)
        return disc_counts1, msg_id_link1
