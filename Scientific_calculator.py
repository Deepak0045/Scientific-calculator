from tkinter import *
import math


def click(value):
    
    ex = entryfield.get()
    answer = ''

    try:

        if value == 'C':
            
            ex = ex[0:len(ex) - 1]
            entryfield.delete(0, END)
            entryfield.insert(0, ex)
            return 
        
        elif value == 'CE':
            entryfield.delete(0, END)
        
        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == "π":
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))
        
        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2*math.pi
        
        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))
        
        elif value == 'sinh':
            answer = math.tanh(eval(ex))
        
        elif value == chr(8731):
            answer = eval(ex) ** (1/3)

        elif value == 'x\u02b8':
            entryfield.insert(END, '**')
            return
            
        elif value == 'x\u00B3':
            answer = eval(ex) ** 3
        
        elif value == 'x\u00B2':
            answer = eval(ex) ** 3

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == 'rad':
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(ex)
        
        elif value == chr(247):
            entryfield.insert(END, '/')
            return
        
        elif value == '=':
            answer = eval(ex)

        else:
            entryfield.insert(END, value)
            return


        entryfield.delete(0, END)
        entryfield.insert(0, answer)
    
    except SyntaxError:
        pass

    



root = Tk()
root.title('Scientific Calculator')
root.config(bg='#17161b')
root.geometry('680x486+600+100')

logo_img = PhotoImage(file='Images/logo.png')
logolabel = Label(root, image = logo_img, bg='#17161b')
logolabel.grid(row=0, column=0)

entryfield = Entry(root, font=('arial', 20, 'bold'), bg='white', fg='black', bd=10, relief=SUNKEN, width=30)
entryfield.grid(column=0, row=0, columnspan=8)

logo_img2 = PhotoImage(file='Images/logo.png')
logolabel2 = Label(root, image = logo_img2, bg='#17161b')
logolabel2.grid(row=0, column=7)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh", 
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", 
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e", 
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

rowvalue = 1
columnvalue = 0


for i in button_text_list:
    button = Button(root, width=5, height=2, bd = 2, relief=SUNKEN, text = i, bg = '#3697f5', fg='white',
                    font=('arial', 18, 'bold'), activebackground='#3697f5', command= lambda button = i:click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue +=1

    if columnvalue>7:
        rowvalue += 1
        columnvalue = 0



root.mainloop()