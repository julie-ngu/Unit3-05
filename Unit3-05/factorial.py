# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program calculates the factorial of an integer that the user inputs

import ui

def calculate_button_touch_up_inside(sender):
    #calculates factorial of inputted integer
    
    # input
    inputted_number = int(view['input_integer_textfield'].text)
    
    # process
    if inputted_number < 0:
        view['answer_label'].text = "Please input a positive integer."
    elif inputted_number == 0:
        view['answer_label'].text = "1"
    else:
        factorial = counter = 1
        while (counter < inputted_number):
            counter = (counter + 1)
            factorial = counter * factorial
            #output
            view['answer_label'].text = "The answer is " + str(factorial) + "."

view = ui.load_view()
view.present('full_view')
