import matplotlib.pyplot as plt

# Sample Data
subjects = ["Math", "Science", "English", "History", "CS"]
marks = [78, 85, 90, 70, 88]

# Histogram
plt.title("Histogram of Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.bar(subjects, marks)
plt.show()

# Scatter Plot
plt.title("Scatter Plot - Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.scatter(subjects, marks)
plt.show()
