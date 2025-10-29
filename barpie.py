import matplotlib.pyplot as plt

cities = ["Mumbai", "Delhi", "Chennai", "Kolkata", "Pune"]
temperature = [32, 38, 34, 33, 30]

# Bar Graph
plt.title("City Temperature Comparison")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.bar(cities, temperature)
plt.show()

# Pie Chart
plt.title("City Temperature Distribution")
plt.pie(temperature, labels=cities, autopct="%1.1f%%")
plt.show()
