from tkinter import *
import math

# Define the click function to handle button press actions
def click(value):
    # Get the current expression in the entry field
    ex = entryfield.get()
    answer = ''  # Initialize an answer variable to store results

    try:
        # Handle each button press based on its label
        if value == 'C':
            # Clear the last character in the entry field
            ex = ex[0:len(ex) - 1]
            entryfield.delete(0, END)
            entryfield.insert(0, ex)
            return 
        
        elif value == 'CE':
            # Clear the entire entry field
            entryfield.delete(0, END)
        
        elif value == '√':
            # Calculate the square root of the expression
            answer = math.sqrt(eval(ex))

        elif value == "π":
            # Insert the value of π (pi)
            answer = math.pi

        elif value == 'cosθ':
            # Calculate the cosine of the expression in degrees
            answer = math.cos(math.radians(eval(ex)))
        
        elif value == 'tanθ':
            # Calculate the tangent of the expression in degrees
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            # Calculate the sine of the expression in degrees
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            # Multiply pi by 2
            answer = 2 * math.pi
        
        elif value == 'cosh':
            # Calculate the hyperbolic cosine
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            # Calculate the hyperbolic tangent
            answer = math.tanh(eval(ex))
        
        elif value == 'sinh':
            # Calculate the hyperbolic sine
            answer = math.sinh(eval(ex))
        
        elif value == chr(8731):  # Unicode for the cube root symbol (∛)
            # Calculate the cube root
            answer = eval(ex) ** (1/3)

        elif value == 'x\u02b8':  # Unicode for superscript symbol
            # Insert exponentiation symbol (**) for power input
            entryfield.insert(END, '**')
            return
            
        elif value == 'x\u00B3':  # Unicode for superscript 3
            # Calculate the cube of the expression
            answer = eval(ex) ** 3
        
        elif value == 'x\u00B2':  # Unicode for superscript 2
            # Calculate the square of the expression
            answer = eval(ex) ** 2

        elif value == 'ln':
            # Calculate the natural logarithm
            answer = math.log(eval(ex))

        elif value == 'deg':
            # Convert radians to degrees
            answer = math.degrees(eval(ex))

        elif value == 'rad':
            # Convert degrees to radians
            answer = math.radians(eval(ex))

        elif value == 'e':
            # Insert the value of e (Euler's number)
            answer = math.e

        elif value == 'log₁₀':
            # Calculate the base-10 logarithm
            answer = math.log10(eval(ex))

        elif value == 'x!':
            # Calculate the factorial (converting to int as factorial requires integers)
            answer = math.factorial(int(ex))
        
        elif value == chr(247):  # Unicode for division symbol (÷)
            # Insert division operator
            entryfield.insert(END, '/')
            return
        
        elif value == '=':
            # Evaluate the expression in the entry field
            answer = eval(ex)

        else:
            # If the value is a number or operator, insert it into the entry field
            entryfield.insert(END, value)
            return

        # Display the answer in the entry field
        entryfield.delete(0, END)
        entryfield.insert(0, answer)
    
    except SyntaxError:
        # Handle any syntax errors in the evaluation
        pass


# Initialize the main window
root = Tk()
root.title('Scientific Calculator')
root.config(bg='#17161b')  # Background color
root.geometry('680x486+600+100')  # Set window size and position

# Load and display logo images
logo_img = PhotoImage(file='Images/logo.png')
logolabel = Label(root, image=logo_img, bg='#17161b')
logolabel.grid(row=0, column=0)

# Entry field for displaying expressions and results
entryfield = Entry(root, font=('arial', 20, 'bold'), bg='white', fg='black', bd=10, relief=SUNKEN, width=30)
entryfield.grid(column=0, row=0, columnspan=8)

logo_img2 = PhotoImage(file='Images/logo.png')
logolabel2 = Label(root, image=logo_img2, bg='#17161b')
logolabel2.grid(row=0, column=7)

# List of button labels for the calculator
button_text_list = [
    "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh", 
    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", 
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e", 
    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"
]

# Initialize button placement values
rowvalue = 1
columnvalue = 0

# Create and place each button in the grid
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='#3697f5', fg='white',
                    font=('arial', 18, 'bold'), activebackground='#3697f5', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    
    # Move to the next column; reset to the next row if max columns reached
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

# Run the application
root.mainloop()
