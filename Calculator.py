## A fully functioning non-scientific calculator
from tkinter import *

## Python backend
# The display variable
calculation = ''

# What happens when each button is pressed
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
    calculation.append(display['text']) 
    for i in calculation():
        print(str(i)) 


## Tkinter Display
# Setup the window 
the_window = Tk()
the_window.title("Calculator") 
calc_font = ('Arial', 26)

# Create the display
display = Label(the_window, text = '0',
                height = 2, width = 4,
                font = calc_font)
display.grid(row = 0, column = 3)

# Set some variables for easy grid adjustment 
x_button_padding = 10
y_button_padding = 10

# Create the number buttons
number_1 = Button(the_window, text = "1",
                  height = 2, width = 4,
                  font = calc_font, command = no_1) 
number_1.grid(row = 1, column = 0,
              padx = x_button_padding, pady = y_button_padding) 

number_2 = Button(the_window, text = "2",
                  height = 2, width = 4,
                  font = calc_font, command = no_2)
number_2.grid(row = 1, column = 1,
              padx = x_button_padding, pady = y_button_padding) 

number_3 = Button(the_window, text = "3",
                  height = 2, width = 4,
                  font = calc_font, command = no_3) 
number_3.grid(row = 1, column = 2,
              padx = x_button_padding, pady = y_button_padding)

number_4 = Button(the_window, text = "4",
                  height = 2, width = 4,
                  font = calc_font, command = no_4) 
number_4.grid(row = 2, column = 0,
              padx = x_button_padding, pady = y_button_padding)

number_5 = Button(the_window, text = "5",
                  height = 2, width = 4,
                  font = calc_font, command = no_5) 
number_5.grid(row = 2, column = 1,
              padx = x_button_padding, pady = y_button_padding)

number_6 = Button(the_window, text = "6",
                  height = 2, width = 4,
                  font = calc_font, command = no_6) 
number_6.grid(row = 2, column = 2,
              padx = x_button_padding, pady = y_button_padding)

number_7 = Button(the_window, text = "7",
                  height = 2, width = 4,
                  font = calc_font, command = no_7) 
number_7.grid(row = 3, column = 0,
              padx = x_button_padding, pady = y_button_padding)

number_8 = Button(the_window, text = "8",
                  height = 2, width = 4,
                  font = calc_font, command = no_8) 
number_8.grid(row = 3, column = 1,
              padx = x_button_padding, pady = y_button_padding)

number_9 = Button(the_window, text = "9",
                  height = 2, width = 4,
                  font = calc_font, command = no_9) 
number_9.grid(row = 3, column = 2,
              padx = x_button_padding, pady = y_button_padding)

number_0 = Button(the_window, text = '0',
                  height = 2, width = 4,
                  font = calc_font, command = no_0) 
number_0.grid(row = 4, column = 1,
              padx = x_button_padding, pady = y_button_padding)

# Create the symbols (+, -, *, /, =, c,)
plus = Button(the_window, text = '+',
              height = 2, width = 4,
              font = calc_font, command = addition)
plus.grid(row = 1, column = 3,
          padx = x_button_padding, pady = y_button_padding)

minus = Button(the_window, text = '-',
              height = 2, width = 4,
              font = calc_font, command = subtraction)
minus.grid(row = 2, column = 3,
           padx = x_button_padding, pady = y_button_padding)

multiply = Button(the_window, text = '*',
              height = 2, width = 4,
              font = calc_font, command = multiplication)
multiply.grid(row = 3, column = 3,
              padx = x_button_padding, pady = y_button_padding)

divide = Button(the_window, text = '/',
              height = 2, width = 4,
              font = calc_font, command = dividation) 
divide.grid(row = 4, column = 3,
            padx = x_button_padding, pady = y_button_padding)

equate = Button(the_window, text = '=',
              height = 2, width = 4,
              font = calc_font, command = equation)
equate.grid(row = 4, column = 2,
            padx = x_button_padding, pady = y_button_padding)

reset = Button(the_window, text = 'c',
               height = 2, width = 4,
               font = calc_font, command = clear)
reset.grid(row = 4, column = 0,
           padx = x_button_padding, pady = y_button_padding)

# Start the events loop 
mainloop()











