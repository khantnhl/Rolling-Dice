from plotly.graph_objs import Bar, Layout
from plotly import offline

from D7_function import Die

#create die
die_1 = Die()
die_2 = Die()
die_3 = Die()
die_4 = Die()
die_5 = Die()
results = []
 


 #kfdashjofhodshiahfoiasdh
for rollnum in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll() + die_4.roll() + die_5.roll()
    results.append(result)

#analyze
frequencies = []
maxresult = die_1.num_sides + die_2.num_sides + die_3.num_sides + die_4.num_sides + die_5.num_sides
for value in range(5,maxresult+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize 
x_values = list(range(5, maxresult+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency'}

my_layout = Layout(title = 'Results of rolling five D7 dice for 10000 times',
    xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d7.html')
            