from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
times = 50_000
for time in range(1, times+1):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze results.
results_range = sorted(set(results))
"""
frequencies = []
for result in results_range:
    counts = results.count(result)
    frequencies.append(counts/times)
"""
# Frequencies with 'list comprehension' syntax:
frequencies = [results.count(result)/times for result in results_range]

# Visualize the results.
x_values = results_range
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling twp d6 dice 50.000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')