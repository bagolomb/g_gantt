import g_gantt
from datetime import datetime


# Initialize the chart
chart = g_gantt.Chart("WEEEEE")

# Add sample tasks to the chart
chart.add_task(
    task_id="T1",
    task_name="Design Phase",
    start=datetime(2024, 11, 1),
    duration=10,  # Duration in days
    dependencies=[],
    percent_complete=50,
    resource="Phase 1"
)

chart.add_task(
    task_id="T2",
    task_name="Development",
    start=datetime(2024, 11, 11),
    duration=15,  # Duration in days
    dependencies=["T1"],  # Depends on "T1"
    percent_complete=30,
    resource="Phase 2"
)

chart.add_task(
    task_id="T3",
    task_name="Testing",
    start=datetime(2024, 12, 1),
    duration=5,  # Duration in days
    dependencies=["T2"],  # Depends on "T2"
    percent_complete=0,
    resource="Phase 3"
)
chart.add_task(
    task_id="T4",
    task_name="Testing",
    start=datetime(2024, 12, 1),
    duration=5,  # Duration in days
    dependencies=["T2"],  # Depends on "T2"
    percent_complete=0,
    resource="Phase 3"
)
chart.add_task(
    task_id="T5",
    task_name="Testing",
    start=datetime(2024, 12, 1),
    duration=5,  # Duration in days
    dependencies=["T2"],  # Depends on "T2"
    percent_complete=0,
    resource="Phase 3"
)

# Show the chart in the default web browser
chart.show()

# Or save it to a file (HTML format)
chart.save('gantt_chart.html')