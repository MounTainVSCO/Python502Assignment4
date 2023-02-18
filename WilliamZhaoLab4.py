##
# Student Name: William Zhao
# Course: CIS 502 Applied Python Programming
# Lab # 4 - Functions, Passing Multiple Arguments
# Application: Your Course Grade Calculator
# Description: The program calculates the average, variance, and 
#              standard deviation of a list of lab scores entered by the user, 
#              and determines if replacing the lowest score with the average 
#              would result in a higher overall lab score.
# Version: Python 3.8
# Solution File: WilliamZhaoLab4.py
# Date: 02/18/23
##

# Program Source

import statistics

ROUND_DECIMAL = 2
MIN_SCORE = 0

def calculate_average(*scores):
    """
    Calculates the average of the scores passed as arguments.
    """
    score_iter = iter(scores)
    total = next(score_iter, 0)
    count = 1
    for score in score_iter:
        total += score
        count += 1
    return round(total/count, ROUND_DECIMAL)

def descriptive_stats(values=[]):
    """
    Calculates the variance and std given a list of values
    """
    try:
        variance = round(statistics.variance(values), ROUND_DECIMAL)
        standard_deviation = round(statistics.stdev(values), ROUND_DECIMAL)
    except statistics.StatisticsError:
        return None, None
    return round(variance, ROUND_DECIMAL), round(standard_deviation, ROUND_DECIMAL)

def get_lab_scores():
    """
    Reads in lab scores from the user and performs various calculations.
    """
    lab_scores = []
    while True:
        try:
            score = float(input("Enter a lab score (0-20): "))
            if score not in range(MIN_SCORE, 21) and score != float:
                raise ValueError("Score must a number in the range [0 - 20]")
            else:
                lab_scores.append(score)
        except ValueError as e:
            print(e)
            continue
        while True:
            choice = input("Do you want to enter another score (Y/N)? ")
            if choice.upper() == 'Y' or choice.upper() == 'N':
                break
            else:
                print("Please enter either 'Y' or 'N'.")
        if choice.upper() == 'N':
            break
    return lab_scores

def bump_up(avg_s, min_s):
    """
    Checks for bump given average and minimum score
    """
    if avg_s > min_s:
        bump = round((lambda x, y: x-y)(avg_s, min_s), ROUND_DECIMAL)
        return bump 

def main():
    scores = get_lab_scores()
    variance, std = descriptive_stats(scores)
    average_score = calculate_average(*scores)
    min_score = min(scores)

    print(f"Lab Scores entered: {scores}")
    print(f"Average Score: {average_score}")
    print(f"Bump up: {bump_up(average_score, min_score)}")
    print(f"Variance of scores: {variance}")
    print(f"Standard Deviation of scores {std}")


if __name__ == "__main__":
    main()

# Test Run Validation
"""
Enter a lab score (0-20): 100
Score must a number in the range [0 - 20]
Enter a lab score (0-20): 15
Do you want to enter another score (Y/N)? Hello, World 
Please enter either 'Y' or 'N'.
Do you want to enter another score (Y/N)? Y
Enter a lab score (0-20): 17
Do you want to enter another score (Y/N)? Y
Enter a lab score (0-20): 19
Do you want to enter another score (Y/N)? Y
Enter a lab score (0-20): 20
Do you want to enter another score (Y/N)? N

Lab Scores entered: [15.0, 17.0, 19.0, 20.0]   
Average Score: 17.75
Bump up: 2.75
Variance of scores: 4.92
Standard Deviation of scores 2.22
"""

"""
Enter a lab score (0-20): 20
Do you want to enter another score (Y/N)? Y
Enter a lab score (0-20): 20
Do you want to enter another score (Y/N)? Y
Enter a lab score (0-20): 5
Do you want to enter another score (Y/N)? N

Lab Scores entered: [20.0, 20.0, 5.0]
Average Score: 15.0
Bump up: 10.0
Variance of scores: 75.0
Standard Deviation of scores 8.66
"""