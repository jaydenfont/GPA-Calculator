"""
GPA Calculator (BU Edition)
Contains 2 sets of methods, one set to act on a user-defined object,
and another to prompt the user step-by-step to enter the informaton.
"""


class Calculator:

    letter_values = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D': 1.0,
        'F': 0.0,
        '0': 0.0  # in case there is no fifth class, this will ensure the calculation is not affected
    }

    buID = "U91735366"

    def __init__(self, g1, c1, g2, c2, g3, c3, g4, c4, g5, c5):  # g = letter grade, c = credit for class

        self.g1 = g1
        self.c1 = c1
        self.g2 = g2
        self.c2 = c2
        self.g3 = g3
        self.c3 = c3
        self.g4 = g4
        self.c4 = c4
        self.g5 = g5
        self.c5 = c5

    def calculate_button(g1, c1, g2, c2, g3, c3, g4, c4, g5, c5):
        # used for GUI
        # fetches matching honor points for letter and then calculates gpa
        total_pts = (Calculator.letter_values.get(g1) * c1) + (Calculator.letter_values.get(g2) * c2) + (
                    Calculator.letter_values.get(g3) * c3) + (Calculator.letter_values.get(g4) * c4) + (
                                Calculator.letter_values.get(g5) * c5)
        total_credits = c1 + c2 + c3 + c4 + c5
        gpa = total_pts / total_credits
        return gpa

    '''
    Everything below this point is not needed for the GUI to work, they are just old functions from previous versions
    '''

    def calculate_prompt():

        total_pts = 0
        total_credits = 0
        course_num = int(input('How many classes are you currently taking? '))
        for n in range(course_num):  # loops through the number of courses you inputed
            grade = input('What was your letter grade for class {}?: '.format(n + 1))
            grade = Calculator.letter_values.get(grade)
            credit = float(input("How many credits is the class?: "))
            pts = grade * credit  # calculates honor points from one class
            total_pts += pts  # adds previous points to running total
            total_credits += credit  # adds inputed credits to running total
        gpa = total_pts / total_credits  # calculates GPA

        return gpa, total_credits, total_pts

    def calculate_obj(self):  # will work with values passed into object, not done

        total_pts = 0
        total_credits = 0
        # grade * credits

        total_pts = (Calculator.letter_values.get(self.g1) * self.c1) + (
                    Calculator.letter_values.get(self.g2) * self.c2) + (
                                Calculator.letter_values.get(self.g3) * self.c3) + (
                                Calculator.letter_values.get(self.g4) * self.c4) + (
                                Calculator.letter_values.get(self.g5) * self.c5)

        total_credits = self.c1 + self.c2 + self.c3 + self.c4 + self.c5  # adds inputed credits to running total
        gpa = total_pts / total_credits  # calculates GPA
        print("Here are your total honor points:" + str(total_pts))
        print('Here are you total credits: ' + str(total_credits))
        return gpa, total_credits, total_pts

    def round_obj(self, gpa, total_credits, total_pts):

        round_prompt = input('Round to 2 decimals? Y/N: ')

        if round_prompt == 'Y' or round_prompt == 'y':
            gpa = roundFunction(gpa, 2)  # rounds to 2 decimals
            print(gpa)
            return total_credits, total_pts
        else:
            print(gpa)
            return total_credits, total_pts

    def roundFunction(gpa, total_credits, total_pts):  # parameters from .calc_with_credits()

        print("Here are your total honor points:" + str(total_pts))
        print('Here are you total credits: ' + str(total_credits))
        round_prompt = input('Round to 2 decimals? Y/N: ')

        if round_prompt == 'Y' or round_prompt == 'y':
            gpa = roundFunction(gpa, 2)  # rounds to 2 decimals
            print(gpa)
            return total_credits, total_pts
        else:
            print(gpa)
            return total_credits, total_pts

    def cumulative(total_credits, total_pts):  # parameters from .round()

        old_points = 61.2 + 56.0 + 60.1
        old_credits = 16 + 16 + 17

        cumulative_prompt = input('Cumulative? (Jay only): Y/N: ')

        if cumulative_prompt == 'Y' or cumulative_prompt == 'y':

            isJay = input("Enter BUID: ")

            if isJay == Calculator.buID:

                print(
                    'Note: must update honor points and credits after each semester.\nSee "Classes" Tab under Student Link')
                cumm_points = total_pts + old_points
                cumm_credits = old_credits + total_credits
                cgpa = cumm_points / cumm_credits
                round_prompt = input('Round to 2 decimals? Y/N: ')
                if round_prompt == 'Y' or round_prompt == 'y':
                    print('Cumulative GPA: {}'.format(roundFunction(cgpa, 2)))  # rounds to 2 decimals
                else:
                    print('Cumulative GPA: {}'.format(cgpa))
            else:
                print('Invalid')
        else:
            return print('Okay')

    def cumulative_obj(self, total_credits, total_pts):  # parameters from .round()

        old_points = 61.2 + 56.0 + 60.1
        old_credits = 16 + 16 + 17

        cumulative_prompt = input('Cumulative (up to Fall 2019)? (Jay only): Y/N: ')

        if cumulative_prompt == 'Y' or cumulative_prompt == 'y':

            isJay = input("Enter BUID: ")

            if isJay == Calculator.buID:

                print(
                    'Note: must update honor points and credits after each semester.\nSee "Classes" Tab under Student Link')
                cumm_points = total_pts + old_points
                cumm_credits = old_credits + total_credits
                cgpa = cumm_points / cumm_credits
                round_prompt = input('Round to 2 decimals? Y/N: ')
                if round_prompt == 'Y' or round_prompt == 'y':
                    print('Cumulative GPA: {}'.format(roundFunction(cgpa, 2)))  # rounds to 2 decimals
                else:
                    print('Cumulative GPA: {}'.format(cgpa))
            else:
                print('Invalid')
        else:
            return print('Okay')

    def exitFromWindow():
        input('Press enter to exit')

