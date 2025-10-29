from matplotlib import pyplot as plt
from matplotlib_venn import venn2

job_roles = ["Developer", "Tester", "Manager", "Analyst"]
salary = [6, 4, 10, 5]  # LPA

# Bar Chart
plt.title("Salary Comparison by Job Role")
plt.xlabel("Job Roles")
plt.ylabel("Salary (LPA)")
plt.bar(job_roles, salary)
plt.show()

# Venn Diagram Example (Developers vs Managers with overlap)
plt.title("Job Skills Overlap")
venn2(subsets=(30, 20, 10), set_labels=("Developers", "Managers"))
plt.show()
