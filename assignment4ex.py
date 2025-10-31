def calculate_energy_expended(activity_type, duration_minutes, intensity): 
    if activity_type == "running":
        if intensity == "low":
            calories = 10
        elif intensity == "medium":
            calories = 14    
        elif intensity == "high":
            calories = 18
        else:
            calories = 0
    elif activity_type == "cycling":
        if intensity == "low":
            calories = 7
        elif intensity == "medium":
            calories = 11    
        elif intensity == "high":
            calories = 15
        else:
            calories = 0
    elif activity_type == "swimming":
        if intensity == "low":
            calories = 9
        elif intensity == "medium":
            calories = 13    
        elif intensity == "high":
            calories = 17
        else:
            calories = 0
    return calories * duration_minutes 

def calculate_performance_intensity(age, baseline_hr, training_hr):
    max_hr = 220 - age
    heart_rate_reserve = max_hr - baseline_hr
    intensity_per = (training_hr - baseline_hr) / heart_rate_reserve * 100
    return intensity_per

def determine_effort_level(intensity_percent):
    if intensity_percent > 85:
        return "Peak Power Level"
    elif intensity_percent > 70:
        return "Threshold Level"
    elif intensity_percent > 60:
        return "Aerobic Level"
    elif intensity_percent > 50:
        return "Endurance Level"
    else:
        return "Recovery Level"
    
def calculate_training_points(energy, duration, effort_level):
    base_points = energy * 0.1 + duration * 2
    if effort_level == "Peak Power Level":
        level_bonus = 1.8
    elif effort_level == "Threshold Level":
        level_bonus = 1.5
    elif effort_level == "Aerobic Level":
        level_bonus = 1.2
    elif effort_level == "Endurance Level":
        level_bonus = 1.0
    elif effort_level == "Recovery Level":
        level_bonus = 0.5
    final_points = base_points + level_bonus
    return round(final_points, 1)

def requires_recovery(training_days, total_minutes, avg_intensity):
    if training_days >= 6:
        return True
    elif total_minutes > 450 and avg_intensity > 70:
        return True
    elif training_days >= 4 and avg_intensity > 80:
        return True
    else:
        return False

def generate_training_summary(athlete, activity_type, duration, intensity, age, baseline_hr, training_hr, training_days):
    intensity_percent = calculate_performance_intensity(age, baseline_hr, training_hr)
    energy_expended = calculate_energy_expended(activity_type, duration, intensity)
    effort_level = determine_effort_level(intensity_percent)
    calculate_points = calculate_training_points(energy_expended, duration, effort_level)
    recovery_needed = requires_recovery(training_days, duration, intensity_percent)

    print("=" * 40)
    print(f"Training Summary for: {athlete}")
    print("-" * 40)
    print(f"Activity Type: {activity_type}")
    print(f"Duration: {duration} minutes")
    print(f"Intensity Level: {intensity}")
    print(f"Energy Expended: {energy_expended}")
    print("Performance Analysis:")
    print(f"  Age: {age}, Baseline HR: {baseline_hr}, Training HR: {training_hr}")
    print(f"Intensity: {intensity_percent:.1f}%")  
    print(f"Effort Level: {effort_level}")  
    print(f"Training Points: {calculate_points}")
    print(f"Consecutive Training Days: {training_days}")
    print(f"Recovery Day Required: {'Yes' if recovery_needed else 'No'}\n")
    
print("SPORTS TRAINING ANALYZER")
athlete = "Sam"
activity_type = "running"
duration = 45
intensity = "high"
age = 28
baseline_hr = 65
training_hr = 155
training_days = 3
generate_training_summary(athlete, activity_type, duration, intensity, age, baseline_hr, training_hr, training_days)

athlete2 = "Morgan"
activity_type2 = "cycling"
duration2 = 60
intensity2 = "medium"
age2 = 35
baseline_hr2 = 70
training_hr2 = 140
training_days2 = 5
generate_training_summary(athlete2, activity_type2, duration2, intensity2, age2, baseline_hr2, training_hr2, training_days2)

athlete3 = "Taylor"
activity_type3 = "swimming"
duration3 = 30
intensity3 = "low"
age3 = 42
baseline_hr3 = 68
training_hr3 = 95
training_days3 = 7
generate_training_summary(athlete3, activity_type3, duration3, intensity3, age3, baseline_hr3, training_hr3, training_days3)