def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average
def drop_lowest(score1, score2, score3):
    lowest = min(score1, score2, score3)
    average_highest = (score1 + score2 + score3 - lowest) / 2
    return average_highest
def calculate_weighted(assignments, midterm, final):
    weighted = assignments * 0.30 + midterm * 0.30 + final * 0.40
    return weighted
def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 80:
        return 'D'
    else: 
        return 'F'
    
def needs_improvement(current_avg, target_grade):
    # minimum for target grade
    minimum_for_target_grade = 0
    if target_grade == 'A':
        minimum_for_target_grade = 90
    elif target_grade == 'B':
        minimum_for_target_grade = 80
    elif target_grade == 'C':
        minimum_for_target_grade = 70
    elif target_grade == 'D':
        minimum_for_target_grade = 60
    return current_avg < minimum_for_target_grade

score1 = 85
score2 = 78
score3 = 92
midterm = 88
final = 82
assignments = calculate_average(score1, score2, score3)
print("STUDENT GRADE CALCULATOR")
print("=" * 40)
print(f"Assignment Scores: {score1}, {score2}, {score3}")
print(f"Midterm Score: {midterm}")
print(f"Final Score: {final}")
print("-" * 40)
print(f"Regular Assignment Average: {assignments:.2f} ")
print(f"Average with Lowest Dropped: {drop_lowest(score1, score2, score3)}")
print(f"Using Better Average: {max(calculate_average(score1, score2, score3), drop_lowest(score1, score2, score3)):.2f}\n")
print(f"Weighted Course Average: {calculate_weighted(assignments, midterm, final):.2f}")
print(f"Letter Grade: {determine_grade(assignments)}\n")
print(f"Needs improvement for an 'A': {'Yes' if determine_grade != 'A' else 'No'}")
print(f"Points needed: {max((90 - calculate_weighted(assignments, midterm, final)), 0):.2f}")
print(f"Already meets or exceeds '{determine_grade(assignments)}' grade requirement")
   