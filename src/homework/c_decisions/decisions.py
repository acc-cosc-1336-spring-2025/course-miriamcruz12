#
def get_options_ratio(option, total): 

    ratio = option/total
    
    return ratio

def get_faculty_rating(ratio):

    faculty_rating = ""

    if(ratio >= .9 and ratio < 1):
        faculty_rating = "Excellent"
    elif(ratio > .8):
        faculty_rating = "Very Good"
    elif(ratio > .7):
        faculty_rating = "Good"
    elif(ratio > .6):
        faculty_rating = "Needs Improvement"
    elif(ratio > 0 and ratio <= .59):
        faculty_rating = "Unacceptable"

        return faculty_rating
    
