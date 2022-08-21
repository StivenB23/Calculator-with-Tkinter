from tkinter import * 
ventana = Tk();
i=0
ventana.title("Calculadora")
ventana.configure(background="white")
# Input 
box_text= Entry(ventana,bg="#E6EFF4",bd=0, font=("sans-serif 20"), width=17)
box_text.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# functions
def click_boton(value):
    global i
    box_text.insert(i, value)
    i += 1

def delete_number():
    box_text.delete(0, END)
    i=0
    
def operation():
    equation = box_text.get()
    result = eval(equation)
    box_text.delete(0, END)
    box_text.insert(0,result)
    i=0
# buttons

button1 = Button(ventana,bd=0, activeforeground="#31A5F0",text = "1", width=5, height=2, command=lambda: click_boton(1))
button2 = Button(ventana,activeforeground="#31A5F0", text = "2",bd=0, width=5, height=2, command=lambda: click_boton(2))
button3 = Button(ventana,activeforeground="#31A5F0", text = "3",bd=0, width=5, height=2, command=lambda: click_boton(3))
button4 = Button(ventana,activeforeground="#31A5F0", text = "4",bd=0, width=5, height=2, command=lambda: click_boton(4))
button5 = Button(ventana,activeforeground="#31A5F0", text = "5",bd=0, width=5, height=2, command=lambda: click_boton(5))
button6 = Button(ventana,activeforeground="#31A5F0", text = "6",bd=0, width=5, height=2, command=lambda: click_boton(6))
button7 = Button(ventana,activeforeground="#31A5F0", text = "7",bd=0, width=5, height=2, command=lambda: click_boton(7))
button8 = Button(ventana,activeforeground="#31A5F0", text = "8",bd=0, width=5, height=2, command=lambda: click_boton(8))
button9 = Button(ventana,activeforeground="#31A5F0", text = "9",bd=0, width=5, height=2, command=lambda: click_boton(9))
button0 = Button(ventana,activeforeground="#31A5F0", text = "0",bd=0, width=16, height=2, command=lambda: click_boton(0))

button_delete = Button(ventana,activeforeground="#31A5F0", text = "AC",bd=0, bg="#31A5F0", width=5, height=2, command=lambda:delete_number())
button_parenthesis_start = Button(ventana,activeforeground="#31A5F0",bd=0, text = "(", width=5, height=2, command=lambda: click_boton("("))
button_parenthesis_end = Button(ventana,activeforeground="#31A5F0",bd=0, text = ")", width=5, height=2, command=lambda: click_boton(")"))
button_point = Button(ventana,bd=0,activeforeground="#31A5F0", text = ".", width=5, height=2, command=lambda: click_boton("."))

button_division = Button(ventana,activeforeground="#31A5F0",bd=0, text = "/", width=5, height=2, command=lambda: click_boton("/"))
button_multiplication = Button(ventana,activeforeground="#31A5F0",bd=0, text = "x", width=5, height=2, command=lambda: click_boton("*"))
button_plus = Button(ventana,bd=0,activeforeground="#31A5F0", text = "+", width=5, height=2, command=lambda: click_boton("+"))
button_minus = Button(ventana,bd=0,activeforeground="#31A5F0", text = "-", width=5, height=2, command=lambda: click_boton("-"))
button_equal = Button(ventana,bd=0,activeforeground="#31A5F0", text = "=", width=5, height=2, command=lambda: operation())

# Add buttons in window
# Actions delete, parenthesis 
button_delete.grid(row=1, column=0, padx=5, pady=5)
button_parenthesis_start.grid(row=1, column=1, padx=5, pady=5)
button_parenthesis_end.grid(row=1, column=2, padx=5, pady=5)
button_division.grid(row=1, column=3, padx=5, pady=5)

# numbers
button7.grid(row=2, column=0, padx=5, pady=5);
button8.grid(row=2, column=1, padx=5, pady=5);
button9.grid(row=2, column=2, padx=5, pady=5);
button_multiplication.grid(row=2, column=3, padx=5, pady=5)

button4.grid(row=3, column=0, padx=5, pady=5);
button5.grid(row=3, column=1, padx=5, pady=5);
button6.grid(row=3, column=2, padx=5, pady=5);
button_plus.grid(row=3, column=3, padx=5, pady=5)

button1.grid(row=4, column=0, padx=5, pady=5);
button2.grid(row=4, column=1, padx=5, pady=5);
button3.grid(row=4, column=2, padx=5, pady=5);
button_minus.grid(row=4, column=3, padx=5, pady=5)

button0.grid(row=5, column=0, columnspan=2,padx=5, pady=5);
button_point.grid(row=5, column=2, padx=5, pady=5);
button_equal.grid(row=5, column=3, padx=5, pady=5);
ventana.mainloop();