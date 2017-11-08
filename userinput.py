##Program that asks user for to ENter thier name and thier age. Print out a message addresses to them that tells them the year that they will turn 100 years old.


import datetime

Name = raw_input("Enter your Name:")

Age = int(raw_input("Enter your Age:"))

print "%s is %d years old"%(Name, Age)

Present_year = datetime.datetime.now().year

No_of_years_to_turn_hundred = 100 - Age

The_year_you_will_turn_hundred = Present_year + No_of_years_to_turn_hundred

print "The year you will turn 100 years old is %d"%(The_year_you_will_turn_hundred)

 
