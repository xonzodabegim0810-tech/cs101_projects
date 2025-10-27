#Time Converter and Scheduler
def hours_to_minutes(hours):
    minutes = 60 * hours
    return minutes
def minutes_to_seconds(minutes):
    seconds = minutes * 60
    return seconds
def total_seconds(hours, minutes, seconds):
    minutes_h = hours_to_minutes(hours)
    seconds_m = minutes_to_seconds(minutes)
    t_seconds = minutes_h * 60 + seconds_m + seconds
    return t_seconds
def format_time(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    time = f" {hours} hours and {minutes} minutes"
    return time

def can_fit_task(available_hours, task_hours, task_minutes):
    total_minutes = task_hours * 60 + task_minutes
    a_hours = available_hours * 60
    return a_hours >= total_minutes
def schedule_summary(task_name, hours, minutes):
    tot_minutes = hours_to_minutes(hours)
    tot_seconds = minutes_to_seconds(minutes)
    print(f"Task: {task_name}")
    print(f"  Duration: {hours} hours, {minutes} minutes")
    print(f"  Total Minutes: {tot_minutes + minutes}")
    print(f"  Total Seconds: {tot_seconds:.f}\n")
hours = 2.5

hour2 = 1
minutes2 = 45
seconds2 = 30

total_minutes1 = 200

hour4 = 3
minutes4 = 20
hour = 3.5

task_name1 = "Study"
hours1 = 2
minutes1 = 30

task_name2 = "Exercise"
hours2 = 0
minutes2 = 45

print("TIME CONVERTER AND SCHEDULER")
print("=" * 40)
print(f"Converting {hours} hours to minutes: {hours_to_minutes(hours)} minutes\n")
print(f"Total seconds for {hour2} hour, {minutes2} minutes, {seconds2} seconds: {total_seconds(hours2, minutes2, seconds2)} seconds\n")
print(f"Formatting {total_minutes1} minutes: {format_time(total_minutes1)}\n")
print(f"Can a {hour4} hour {minutes4} minute task fit in {hour} hours?")
print(f"  {"Yes, the task fits!" if can_fit_task(hour, hour4, minutes4) else "No, task doesn't fits!"}\n")
print(f"SCHEDULE SUMMARIES:")
print("-" * 30)

print(f"{schedule_summary(task_name1, hours1, minutes1)}")
print(f"{schedule_summary(task_name2, hours2, minutes2)}")