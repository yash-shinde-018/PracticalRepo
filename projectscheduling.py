import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

tasks = [
    ("Requirement Gathering", "2025-08-12", "2025-08-22", "2025-08-12", "2025-08-20"),
    ("Design/Modeling", "2025-08-23", "2025-09-12", "2025-08-24", "2025-09-14"),
    ("Coding", "2025-09-13", "2025-10-10", "2025-09-16", "2025-10-12"),
    ("Testing", "2025-10-11", "2025-10-31", "2025-10-14", "2025-10-30"),
    ("Deployment", "2025-11-01", "2025-11-07", "2025-11-02", "2025-11-06"),
]

def convert_dates(start_date, end_date):
    return datetime.strptime(start_date, "%Y-%m-%d"), datetime.strptime(end_date, "%Y-%m-%d")

estimated_start_dates = [convert_dates(task[1], task[2])[0] for task in tasks]
estimated_end_dates = [convert_dates(task[1], task[2])[1] for task in tasks]

actual_start_dates = [
    max(convert_dates(task[3], task[4])[0], est_start)
    for task, est_start in zip(tasks, estimated_start_dates)
]

actual_end_dates = [
    min(convert_dates(task[3], task[4])[1], est_end)
    for task, est_end in zip(tasks, estimated_end_dates)
]

fig, ax = plt.subplots(figsize=(10, 6))
bar_height = 0.4

# Estimated Timeline Bars
for i, (task, est_start, est_end) in enumerate(zip(tasks, estimated_start_dates, estimated_end_dates)):
    ax.barh(i - bar_height/2, (est_end - est_start).days, left=est_start, height=bar_height,
            label=f"Estimated: {task[0]}", color="skyblue")

# Actual Timeline Bars
for i, (task, act_start, act_end) in enumerate(zip(tasks, actual_start_dates, actual_end_dates)):
    ax.barh(i + bar_height/2, (act_end - act_start).days, left=act_start, height=bar_height,
            label=f"Actual: {task[0]}", color='orange')

ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task[0] for task in tasks])

ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator())

plt.xticks(rotation=45)
ax.set_xlabel("Date")
ax.set_title("Project Schedule Gantt Chart (Estimated vs. Actual)")

# Fix duplicate legend labels
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc="upper left", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()
