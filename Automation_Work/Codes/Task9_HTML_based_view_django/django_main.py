import sys
import djangoClass


type_of_graph = sys.argv[1]
days = int(sys.argv[2])

e = djangoClass.SheetAccess(days)
string, count_string = e.plot_data(days)
user = djangoClass.PLOT(days, type_of_graph, count_string, string)
user.plot(days, type_of_graph, count_string, string)

#  print("/media/temp4.png")