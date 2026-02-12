def redact(original_string):
    thing = "Victim"
    new_string = ""
    for word in original_string:
        if word == "B":
            new_string += thing
        if word == "D":
            new_string += thing
        if word == "Z": 
            new_string = thing
        else:
            new_string = original_string

    return new_string

Bill_Clinton = "Bill had 45 affairs, many of which were \
    those with big billionares. \
    This list included Don, Monica, my clients \
    Don't worry about it, all of these will be oh shi-"
DJT = "Donald was a great guy with the most dalliances \
he really liked minors, a lot of them, more than me \
make sure to check the M btw, a lot of slaves there"
dsouza = "Zoe was born and raised in London, England. She studied Classics at \
the undergraduate level at Durham University and pursued her Masters degree in \
Classics and Education at Cambridge University. She has taught Latin and \
Classics for the past 8 years, with a particular interest in epic poetry, Greek \
theatre, and the timeless entertainment of Ovid and Cicero. In her previous role, \
she was a Head of Year (a mixture of Dean of Students and College Counsellor), and \
as a result has developed a keen interest in mental health in young people, as \
well as enabling students to pursue Higher Education. In her spare time, Zoe is \
enjoying exploring California with her partner and their dog and enjoys good food, \
exercise, and women's soccer. Oh and she visited my island 80 times!"
print(redact(Bill_Clinton))
print(redact(DJT))
print(redact(dsouza))