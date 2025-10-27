#problem: Grade analysis
score1 = 85
score2 =92
score3 = 78

highest = max(score1, score2, score3)
lowest = min(score1, score2, score3)
average = sum((score1, score2, score3)) / 3
round_average = round(average, 2)
absolute = abs(highest - lowest)

weighted1 = pow(score1, 2)
weighted2 = pow(score2, 2)
weighted3 = pow(score3, 2)
total = weighted1 + weighted2 + weighted3

print("Grade analysis: ")
print(f"Scores: {score1}, {score2}, {score3}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {round_average}")
print(f"Range: {absolute}")
print(f"Weighted total (squared): {total}")



#Problem: Grometric calculator

def area_of_rectangle(width, height):
    return width * height
def perimemter_of_rectangle(width, height): 
    return 2 * (width + height)
def volume_of_triangular_prism(base, height_triangle, prism_length):
    return base * height_triangle * prism_length / 2