from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll in range(100):
    results.append(die.roll())

print(results)