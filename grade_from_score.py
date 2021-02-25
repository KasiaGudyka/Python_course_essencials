# convertion of a 0-100 point score to a A-F grade
# asking a user to input their score
score = int(input("Give your score: "))

# defining a function that converts it to a grade
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 65 and grade <= 69:
        return "D"
    else:
        return "F"
      

# printing a result      
print ("Your grade is: " + grade_converter(score))
