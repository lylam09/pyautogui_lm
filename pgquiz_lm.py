import pyautogui as pg
import time
import webbrowser 

points = 0

# Question
answer = pg.prompt(
"""
Which would you rather do?

a) Eat sandwiches and play video games
b) Cook and clean 
c) Read fashion magazines 


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3 

# Question
answer = pg.prompt(
"""
Who would you rather date?

a) No one, commitment is for losers
b) My former best friend
c) A smart guy who I've known forever 

"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
What would you rather eat for dinner?

a) meatball sandiwch 
b) something veggie
c) something posh 


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
What is your job?

a) An actor, you may know me from the famous soap opera, Days of Our Lives 
b) Chef
c) I used to work at a coffee shop but now I work in fashion 


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question
answer = pg.prompt(
"""
What is your job?

a) An actor, you may know me from the famous soap opera, Days of Our Lives 
b) Chef
c) I used to work at a coffee shop but now I work in fashion 


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# END OF SURVEY

pg.alert("You are ...")

# Joey
if points < 4:
    pg.alert("Joey Tribbiani")
    webbrowser.open("https://www.youtube.com/watch?v=43wkqM27z2E")
# Monica
if points >= 4 and points < 7:
    pg.alert("Monica Geller")
    webbrowser.open("https://www.youtube.com/watch?v=_MxOfcrgOdE")
# Rachel 
if points >= 7 and points < 10:
    pg.alert("Rachel Green")
    webbrowser("https://media.tenor.com/images/d2cdbc9a64857acdfa4b1b4385a57073/tenor.gif")


