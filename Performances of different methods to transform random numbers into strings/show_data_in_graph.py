from matplotlib import pyplot as plt
from json import load

with open("data.json") as f:
    data = load(f)

plt.ylabel("Time (in sec)")
plt.xlabel("Repeat times")

# Plot each curve from the JSON file data
plt.plot(data["loop_generator"]["x"], data["loop_generator"]["y"], label="Loop Generator")
plt.plot(data["loop_list"]["x"], data["loop_list"]["y"], label="Loop List")
plt.plot(data["map"]["x"], data["map"]["y"], label="Map")
plt.plot(data["list_comprehension"]["x"], data["list_comprehension"]["y"], label="List Comprehension")
plt.plot(data["generator"]["x"], data["generator"]["y"], label="Generator")

# Add a legend
plt.legend()

# Display the plot
plt.show()
