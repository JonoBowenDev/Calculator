## A fully functioning non-scientific calculator
from tkinter import *

### Python backend ###

# The calculation, created by the user's input
calculation = ''

# What happens when each button is pressed
# The number buttons 
def no_1():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/': 
        display['text'] = '1'
    else:
        display['text'] = display['text'] + '1'
def no_2():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/':
        display['text'] = '2'
    else:
        display['text'] = display['text'] + '2'
def no_3():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/':
        display['text'] = '3'
    else:
        display['text'] = display['text'] + '3'
def no_4():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/':
        display['text'] = '4'
    else:
        display['text'] = display['text'] + '4'
def no_5():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/':
        display['text'] = '5'
    else:
        display['text'] = display['text'] + '5'
def no_6():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/':
        display['text'] = '6'
    else:
        display['text'] = display['text'] + '6'
def no_7():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/':
        display['text'] = '7'
    else:
        display['text'] = display['text'] + '7'
def no_8():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/':
        display['text'] = '8'
    else:
        display['text'] = display['text'] + '8'
def no_9():
    if display['text'] == '0' or display['text'] == '+' or display['text'] == '-' or display['text'] == '*' or display['text'] == '/':
        display['text'] = '9'
    else:
        display['text'] = display['text'] + '9'
def no_0():
    display['text'] = display['text'] + '0'
def clear():
    display['text'] = '0'
    calculation = []

# The +, -, %, x and = buttons 
def addition():
    calculation.append(display['text'])
    calculation.append('+')
    display['text'] = '+' 
def subtraction():
    calculation.append(display['text'])
    calculation.append('-')
    display['text'] = '-'
def dividation():
    calculation.append(display['text'])
    calculation.append('/')
    display['text'] = '/'
def multiplication(): 
    calculation.append(display['text'])
    calculation.append('*')
    display['text'] = '*'
def equation():
    pass  


### Tkinter Display  ###

# Set cosmetic variables for easy adjustment
calculator_colour = 'white smoke'
display_colour = 'white smoke'
button_colour = 'snow'
button_style = 'ridge'

# Setup the window 
the_window = Tk()
the_window.title("Calculator")
the_window.configure(background = calculator_colour) 
calc_font = ('Arial', 26)

# Create the display
display = Label(the_window, text = '0',
                height = 2, width = 4,
                font = calc_font, background = display_colour) 
display.grid(row = 0, column = 3)

# Create a function for easy button making
def create_calc_button(digit, row_no, column_no, x_padding,
                       y_padding, command_name):
    number_digit = Button(the_window, text = str(digit),
                          height = 2, width = 4,
                          font = calc_font, command = command_name,
                          background = button_colour, relief = button_style)    
    number_digit.grid(row = row_no, column = column_no,
                      padx = x_padding, pady = y_padding)

# Create the number buttons
# Number 1
create_calc_button(1, 1, 0, 10, 10, no_1)
# Number 2
create_calc_button(2, 1, 1, 10, 10, no_2)
# Number 3
create_calc_button(3, 1, 2, 10, 10, no_3)
# Number 4
create_calc_button(4, 2, 0, 10, 10, no_4)
# Number 5
create_calc_button(5, 2, 1, 10, 10, no_5)
# Number 6
create_calc_button(6, 2, 2, 10, 10, no_6)
# Number 7
create_calc_button(7, 3, 0, 10, 10, no_7)
# Number 8
create_calc_button(8, 3, 1, 10, 10, no_8) 
# Number 9
create_calc_button(9, 3, 2, 10, 10, no_9)
# Number 0
create_calc_button(0, 4, 1, 10, 10, no_0) 


# Create the other buttons (+, -, *, /, =, c,)
plus = Button(the_window, text = '+',
              height = 2, width = 4,
              font = calc_font, command = addition,
              background = button_colour, relief = button_style)
plus.grid(row = 1, column = 3,
          padx = 10, pady = 10)

minus = Button(the_window, text = '-',
              height = 2, width = 4,
              font = calc_font, command = subtraction,
              background = button_colour, relief = button_style) 
minus.grid(row = 2, column = 3,
           padx = 10, pady = 10)

multiply = Button(the_window, text = '*',
              height = 2, width = 4,
              font = calc_font, command = multiplication,
              background = button_colour, relief = button_style)  
multiply.grid(row = 3, column = 3,
              padx = 10, pady = 10)

divide = Button(the_window, text = '/',
              height = 2, width = 4,
              font = calc_font, command = dividation,
              background = button_colour, relief = button_style) 
divide.grid(row = 4, column = 3,
            padx = 10, pady = 10)

equate = Button(the_window, text = '=',
              height = 2, width = 4,
              font = calc_font, command = equation,
              background = button_colour, relief = button_style) 
equate.grid(row = 4, column = 2,
            padx = 10, pady = 10)

reset = Button(the_window, text = 'c',
               height = 2, width = 4,
               font = calc_font, command = clear,
               background = button_colour, relief = button_style) 
reset.grid(row = 4, column = 0,
           padx = 10, pady = 10)

# Start the events loop 
mainloop()














