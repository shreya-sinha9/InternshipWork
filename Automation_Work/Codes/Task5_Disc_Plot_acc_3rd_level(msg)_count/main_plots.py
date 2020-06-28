import myClass
import matplotlib.pyplot as plt

days = input("Enter the number of days\n")
file = "D:\\err_war_day"

# ERROR
print("ERROR disc plot")
e = myClass.Error(days, file)
disc_counts, msg_id_link = e.error()
title = "ERROR:"
type_of_graph = input("Enter the type of graph you want: 1)Bar 2)Line 3)Dot\n")
user = myClass.PLOT(days, type_of_graph, disc_counts, msg_id_link, title)
user.plot()

# WARNING
print("WARNING disc plot")
d = myClass.Warning(days, file)
disc_counts1, msg_id_link1 = d.warn()
title = "WARNING:"
type_of_graph = input("Enter the type of graph you want: 1)Bar 2)Line 3)Dot\n")
user = myClass.PLOT(days, type_of_graph, disc_counts1, msg_id_link1, title)
user.plot()
