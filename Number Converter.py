import tkinter as tk
from BaseConverter import *

# Main window
win = tk.Tk()
cvs = tk.Canvas(win, width = 260, height = 200)
cvs.pack()

# Label for Binary
lbl2 = tk.Label(win, text = 'Binary(Base2)')
cvs.create_window(60, 30, window = lbl2)

# Function fro entry in binary number
def b2(event):
    n10 = b2b10(int(ent2.get()))
    ent10.delete(0, tk.END)
    ent10.insert(0, str(n10))
    
    n3 = b10b3(n10)
    ent3.delete(0, tk.END)
    ent3.insert(0, str(n3))
    
    n8 = b10b8(n10)
    ent8.delete(0, tk.END)
    ent8.insert(0, str(n8))
    
    n12 = b10b12(n10)
    ent12.delete(0, tk.END)
    ent12.insert(0, str(n12))
    
    n16 = b10b16(n10)
    ent16.delete(0, tk.END)
    ent16.insert(0, str(n16))

# Entry window for Binary
ent2 = tk.Entry(win)
ent2.bind('<Return>', b2)
cvs.create_window(190, 30, window = ent2)

# Label for Ternary
lbl3 = tk.Label(win, text = 'Ternary(Base 3)')
cvs.create_window(60, 60, window = lbl3)

# Function fro entry in ternary number
def b3(event):
    n10 = b3b10(int(ent3.get()))
    ent10.delete(0, tk.END)
    ent10.insert(0, str(n10))
    
    n2 = b10b2(n10)
    ent2.delete(0, tk.END)
    ent2.insert(0, str(n2))
    
    n8 = b10b8(n10)
    ent8.delete(0, tk.END)
    ent8.insert(0, str(n8))
    
    n12 = b10b12(n10)
    ent12.delete(0, tk.END)
    ent12.insert(0, str(n12))
    
    n16 = b10b16(n10)
    ent16.delete(0, tk.END)
    ent16.insert(0, str(n16))

# Entry window for Ternary
ent3 = tk.Entry(win)
ent3.bind('<Return>', b3)
cvs.create_window(190, 60, window=ent3)

# Label for Octal
lbl8 = tk.Label(win, text = 'Octal(Base 8)')
cvs.create_window(60, 90, window = lbl8)

# Function fro entry in octal number
def b8(event):
    n10 = b8b10(int(ent8.get()))
    ent10.delete(0, tk.END)
    ent10.insert(0, str(n10))
    
    n2 = b10b2(n10)
    ent2.delete(0, tk.END)
    ent2.insert(0, str(n2))
    
    n3 = b10b3(n10)
    ent3.delete(0, tk.END)
    ent3.insert(0, str(n3))
    
    n12 = b10b12(n10)
    ent12.delete(0, tk.END)
    ent12.insert(0, str(n12))
    
    n16 = b10b16(n10)
    ent16.delete(0, tk.END)
    ent16.insert(0, str(n16))

# Entry window for Octal
ent8 = tk.Entry(win)
ent8.bind('<Return>', b8)
cvs.create_window(190, 90, window=ent8)

# Label for Decimal
lbl10 = tk.Label(win, text = 'Decimal(Base 10)')
cvs.create_window(60, 120, window = lbl10)

# Function fro entry in decimal number
def b10(event):
    n10 = int(int(ent10.get()))

    n2 = b10b2(n10)
    ent2.delete(0, tk.END)
    ent2.insert(0, str(n2))

    n3 = b10b3(n10)
    ent3.delete(0, tk.END)
    ent3.insert(0, str(n3))
    
    n8 = b10b8(n10)
    ent8.delete(0, tk.END)
    ent8.insert(0, str(n8))
    
    n12 = b10b12(n10)
    ent12.delete(0, tk.END)
    ent12.insert(0, str(n12))
    
    n16 = b10b16(n10)
    ent16.delete(0, tk.END)
    ent16.insert(0, str(n16))

# Entry window for Decimal
ent10 = tk.Entry(win)
ent10.bind('<Return>', b10)
cvs.create_window(190, 120, window=ent10)

# Label foe Duodecimal
lbl12 = tk.Label(win, text = 'Duodecimal(Base 12)')
cvs.create_window(60, 150, window = lbl12)

# Function fro entry in duodecimal number
def b12(event):
    n10 = b12b10(ent12.get())
    ent10.delete(0, tk.END)
    ent10.insert(0, str(n10))
    
    n2 = b10b2(n10)
    ent2.delete(0, tk.END)
    ent2.insert(0, str(n2))
    
    n3 = b10b3(n10)
    ent3.delete(0, tk.END)
    ent3.insert(0, str(n3))
    
    n8 = b10b8(n10)
    ent8.delete(0, tk.END)
    ent8.insert(0, str(n8))
    
    n16 = b10b16(n10)
    ent16.delete(0, tk.END)
    ent16.insert(0, str(n16))

# Entry window for Duodecimal
ent12 = tk.Entry(win)
ent12.bind('<Return>', b12)
cvs.create_window(190, 150, window=ent12)

# Label for Hexadecimal
lbl16 = tk.Label(win, text = 'Hexadecimal(Base 16)')
cvs.create_window(60, 180, window = lbl16)

# Function fro entry in hexadecimal number
def b16(event):
    n10 = b16b10(ent16.get())
    ent10.delete(0, tk.END)
    ent10.insert(0, str(n10))
    
    n2 = b10b2(n10)
    ent2.delete(0, tk.END)
    ent2.insert(0, str(n2))

    n3 = b10b3(n10)
    ent3.delete(0, tk.END)
    ent3.insert(0, str(n3))
    
    n8 = b10b8(n10)
    ent8.delete(0, tk.END)
    ent8.insert(0, str(n8))
    
    n12 = b10b12(n10)
    ent12.delete(0, tk.END)
    ent12.insert(0, str(n12))

# Entry window for Hexadecimal
ent16 = tk.Entry(win)
ent16.bind('<Return>', b16)
cvs.create_window(190, 180, window=ent16)

win.mainloop()