"""
GUI Add-On for GPA Calculator
Some helpful links:
http://codeinpython.com/tutorials/learn-use-classes-tkinter/
https://pythonprogramming.net/change-show-new-frame-tkinter/
BEST ONES:
https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.htmlx
https://www.geeksforgeeks.org/python-gui-tkinter/
"""
import tkinter as tk
from gpa_calculator_class import Calculator as Calc


class MainWindow:

    def simplerCalculate(self):
        """
        Saves user inputted grades and credits in list,
        then passes list values through calculate function to calculate GPA
        """

        # retrieve responses from text boxes
        grades = [self.g1entry.get(), self.g2entry.get(), self.g3entry.get(), self.g4entry.get(),
                  self.g5entry.get()]
        credits = [self.c1entry.get(), self.c2entry.get(), self.c3entry.get(), self.c4entry.get(),
                   self.c5entry.get()]
        # makes sure each class is has both a letter grade and credit hours
        gradeEntries = 0
        creditEntries = 0
        for grade in grades:
            if grade != "":
                gradeEntries += 1
        for credit in credits:
            if credit != "" or credit == 0:
                creditEntries += 1
        print(gradeEntries)
        print(creditEntries)
        equalLength = True
        if gradeEntries != creditEntries:
            equalLength = False

        #  iterates through grade entries to capitalize them for matching to dictionary
        gradeListIndex = 0
        for grade in grades:
            if len(grade) == 0:  # prevents error when searching for blank spaces in dictionary
                grades[gradeListIndex] = "0"
            else:
                grades[gradeListIndex] = grade.upper()
            gradeListIndex += 1
        print("Grades: {}".format(grades))

        # iterates through credit entries to convert to int

        creditListIndex = 0
        for grade in credits:
            if len(grade) == 0:  # prevents error when converting blank spaces to int
                credits[creditListIndex] = 0
            else:
                credits[creditListIndex] = int(grade)
            creditListIndex += 1
        print('Credits: {}'.format(credits))

        # Calculates and rounds, checking to make sure the user input something, and that each class is filled completely
        if equalLength == True:
            try:
                gpa = Calc.calculate_button(grades[0], credits[0], grades[1], credits[1], grades[2], credits[2], grades[3],
                                            credits[3], grades[4], credits[4])
            except:
                self.errorLabel = tk.Label(root, text='Error: Must enter at least one class.', width = 40)
                self.errorLabel.grid(row=9, column=1)
                print("user failed to enter data for one class")
        else:
            self.mismatchLabel = tk.Label(root, text='Error: Must fill both grade and credits for each class.')
            self.mismatchLabel.grid(row=9, column=1)
            print("Mismatch between number of grades and credits")

        # Rounding
        roundResponse = self.roundVar.get()  # fetches result from rounding checkbox
        if roundResponse == 1:  # box is checked off
            print("user chose to round")
            gpa = round(gpa, 2)
            print("GPA: " + str(gpa))
        else:
            print("user did not round")
            gpa = gpa
            print("GPA: " + str(gpa))

        # Displays GPA
        result = "Your Semester GPA is: {}".format(str(gpa))
        self.gpa_label = tk.Label(root, text=result, font="bold", width=40)
        self.gpa_label.grid(row=9, column=1)

    def __init__(self, master):
        self.master = master
        master.title("GPA Calculator")

        self.title = tk.Label(master, text='Semester GPA Calculator')
        self.title.grid(column=1)

        self.instructions = tk.Label(master, text='Enter your information below (leave unused spaces blank)')
        self.instructions.grid(row=1, column=1)

        # label for text box
        self.labelg1 = tk.Label(master, text='Grade from Class 1')
        self.labelg1.grid(row=3, column=0)
        # entry for text box
        self.g1entry = tk.Entry(master)
        self.g1entry.grid(row=3, column=1)

        self.labelc1 = tk.Label(master, text='Credits for Class 1')
        self.labelc1.grid(row=4, column=0)
        self.c1entry = tk.Entry(master)
        self.c1entry.grid(row=4, column=1)

        self.labelg2 = tk.Label(master, text='Grade from Class 2')
        self.labelg2.grid(row=3, column=2)
        self.g2entry = tk.Entry(master)
        self.g2entry.grid(row=3, column=3)

        self.labelc2 = tk.Label(master, text='Credits for Class 2')
        self.labelc2.grid(row=4, column=2)
        self.c2entry = tk.Entry(master)
        self.c2entry.grid(row=4, column=3)

        self.labelg3 = tk.Label(master, text='Grade from Class 3')
        self.labelg3.grid(row=5, column=0)
        self.g3entry = tk.Entry(master)
        self.g3entry.grid(row=5, column=1)

        self.labelc3 = tk.Label(master, text='Credits for Class 3')
        self.labelc3.grid(row=6, column=0)
        self.c3entry = tk.Entry(master)
        self.c3entry.grid(row=6, column=1)

        self.labelg4 = tk.Label(master, text='Grade from Class 4')
        self.labelg4.grid(row=5, column=2)
        self.g4entry = tk.Entry(master)
        self.g4entry.grid(row=5, column=3)

        self.labelc4 = tk.Label(master, text='Credits for Class 4')
        self.labelc4.grid(row=6, column=2)
        self.c4entry = tk.Entry(master)
        self.c4entry.grid(row=6, column=3)

        self.labelg5 = tk.Label(master, text='Grade from Class 5 (if not overloading, leave blank)')
        self.labelg5.grid(row=7, column=1)
        self.g5entry = tk.Entry(master)
        self.g5entry.grid(row=7, column=2)

        self.labelc5 = tk.Label(master, text='Credits for Class 5 (if not overloading, leave blank)')
        self.labelc5.grid(row=8, column=1)
        self.c5entry = tk.Entry(master)
        self.c5entry.grid(row=8, column=2)

        self.roundVar = tk.IntVar() # 0 or 1
        self.roundBox = tk.Checkbutton(master, text='Round to 2 Decimals?', var=self.roundVar)
        self.roundBox.grid(row=9, column=3)
        self.calculateButton = tk.Button(master, text='Calculate', width=10, height=3,
                                         command=lambda: MainWindow.simplerCalculate(self))
        self.calculateButton.grid(row=9, column=2)


root = tk.Tk(className=" Calculator")
gui = MainWindow(root)
root.mainloop()