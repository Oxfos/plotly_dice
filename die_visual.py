from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
times = 10_000
results = die.roll_x_times(times)

# Analyze results.
frequencies = []
for side in range(1, die.num_sides+1):
    counts = results.count(side)
    frequencies.append(counts/times)

# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 10.000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')