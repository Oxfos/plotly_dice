from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = die.roll_x_times(10_000)

# Analyze results.
frequencies = []
for side in range(1, die.num_sides+1):
    counts = results.count(side)
    frequencies.append(counts/10_000)

print(frequencies)