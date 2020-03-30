
"""
GPA Calculator (BU Edition)
Test File

Execution:
Functions are encapsulated.
f3(*f2(*f1)), the * transfers all returned values from inner function to outer function
Order of execution: f1, f2, f3  
 
Functions with .obj act on an object,s
others work by prompting the user.
If there is less than 5 classes, put 0 for g and c
       
"""
from gpa_calculator_class import Calculator as C

print('This program will calculate your semester GPA.\nIf you enter your past honor points and credits into the source code,\nit can also give you your cumulative GPA.\nFill out the information below:\n(This uses the Boston University system to calcuate GPA.\nThe calculations are outlined on BU\'s website.)')

# Object Oriented ###################################################################
 
print("\n\n\nThis will automatically input data based on the object defined in this file" )
jay = C("A-", 5, "B", 4, "A-", 4, "A-", 4, 0, 0)

jay.cumulative_obj(*jay.round_obj(*jay.calculate_obj()))

# Prompting user ####################################################################

print("\n\n\nThis will prompt the user to put in their information as requested.")
C.cumulative(*C.round(*C.calculate_prompt()))

# Ends Program when user hits exit

C.exit()
