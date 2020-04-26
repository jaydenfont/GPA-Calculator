# jaydenfont-gpacalculator
GPA Calculator using Tkinter API

Screenshots: 

![Image description](https://github.com/jaydenfont/jaydenfont-gpacalculator/blob/master/EmptyGui.png)
![Image description](https://github.com/jaydenfont/jaydenfont-gpacalculator/blob/master/FilledGuiNoRound.png)
![Image description](https://github.com/jaydenfont/jaydenfont-gpacalculator/blob/master/FilledGuiRound.png)

Directions:

    Run the gui file to bring up the program
    Enter letter grade values (upper or lowercase, include + or - if needed) and the number of credits the class is worth
    Check the round box if you want to round to 2 decimal places
    Hit calculate to get your Semester GPA

How it works:

    The Tkinter API is used to make the GUI.
    The main window is created in the __init__() method. Its attributes are organized in a grid format. There are entry
    fields for 5 classes (to account for schedule overloading). The user enters their letter grade and credits for each
    class into the Entry() fields, which is saved to a variable. When the user hits the calculate button, it fetches the
    inputs using the .get() method, and stores them into lists (one for the letter grades and one for the credits).
    The letter grades are converted to uppercase and empty values are converted to "0" (string). Credits are converted
    to integers and empty values are stored as "0" (integer). The calculate_button function from the class file takes
    the letter grades and credits as arguments. The values are then matched to the letter_values dictionary
    in the class file, which has the honor points associated with each letter grade (0 is included so that the
    calculation can work with empty spaces). The function returns the GPA as calculated according to the formula
    provided by BU. There is a checkbox on the GUI for the user to select the option to round to 2 decimal places. If
    checked, the value of roundVar == 1, and the GPA is rounded. Otherwise, it is left as is and is displayed in a Label().

Things to work on:

    Completed:
        automatically make letter grades uppercase if user inputs lowercase
            done
        fix the way it deals with empty fields to make code look nicer!!
            done,
            see the "fetch input" task
        fix rounding bug where non-rounded numbers don't get removed!!
            done, setting width of the text to around 40 allows old text to be overwritten
        shorten code to fetch user input in gpa_gui.calculate()
            done,
            wrote new function that stores input as a list, then iterates over list to modify values as needed.
            then, the list indices are passed into the CalculateButton() function
    To Do:
        add option to calculate cumulative gpa
        have first window ask if user is overloading, then transition to next window which has appropriate number of fields
        

