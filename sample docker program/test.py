# Function to check if a student has passed based on a given score
def has_passed(score):
    return score >= 70

def display_result(passed):
    if passed:
        return "You have passed"
    else:
        return "You have not passed"

# Main program
if __name__ == '__main__':
    number = 70
