import tkinter as tk

def b2b10(n):
    r = 0
    i = 0
    while n > 0:
        r += (n%10) * 2 ** i
        n = int(n/10)
        i += 1
    return r

def b3b10(n):
    r = 0
    i = 0
    while n > 0:
        r += (n%3) * 3 ** i
        n = int(n/10)
        i += 1
    return r

def b8b10(n):
    r = 0
    i = 0
    while n > 0:
        r += (n%8) * 8 ** i
        n = int(n/10)
    return r

def b12b10(n):
    r = 0
    l = len(n)
    j = 0
    for i in range(l-1, -1, -1):
        if n[i] == 'a' or n[i] == 'A':
            r += 10
        elif n[i] == 'b' or n[i] == 'B':
            r += 11
        else:
            r += int(n[i]) * 12 ** j
        j += 1
    return r

def b16b10(n):
    r = 0
    l = len(n)
    j = 0
    for i in range(l-1, -1, -1):
        if n[i] == 'a' or n[i] == 'A':
            r += 10
        elif n[i] == 'b' or n[i] == 'B':
            r += 11
        elif n[i] == 'c' or n[i] == 'C':
            r += 12
        elif n[i] == 'd' or n[i] == 'D':
            r += 13
        elif n[i] == 'e' or n[i] == 'B':
            r += 14
        elif n[i] == 'f' or n[i] == 'F':
            r += 15
        else:
            r += int(n[i]) * 16 ** j
        j += 1
    return r

def b10b2(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        r = r  + str(n % 2)
        n = int(n/2)
        i += 1
    r = r[::-1]
    return int(r)

def b10b3(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        
        r = r  + str(n % 3)
        n = int(n/3)
        i += 1
    r = r[::-1]
    return int(r)

def b10b8(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        r = r  + str(n % 8)
        n = int(n/8)
        i += 1
    r = r[::-1]
    return int(r)

def b10b12(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        if n % 12 == 10:
            r = r + 'A'
        elif n % 12 == 11:
            r = r + 'B'
        else:
            r = r + str(n % 12)
        n = int(n/12)
        i += 1
    r = r[::-1]
    return r

def b10b16(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        if n % 16 == 10:
            r = r + 'A'
        elif n % 16 == 11:
            r = r + 'B'
        elif n % 16 == 12:
            r = r + 'C'
        elif n % 16 == 13:
            r = r + 'D'
        elif n % 16 == 14:
            r = r + 'E'
        elif n % 16 == 15:
            r = r + 'F'
        else:
            r = r + str(n % 16)
        n = int(n/16)
        i += 1
    r = r[::-1]
    return r

win = tk.Tk()
cvs = tk.Canvas(win, width = 260, height = 200)
cvs.pack()

lbl2 = tk.Label(win, text = 'Binary(Base2)')
cvs.create_window(60, 30, window = lbl2)

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

ent2 = tk.Entry(win)
ent2.bind('<Return>', b2)
cvs.create_window(190, 30, window = ent2)

lbl3 = tk.Label(win, text = 'Ternary(Base 3)')
cvs.create_window(60, 60, window = lbl3)

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

ent3 = tk.Entry(win)
ent3.bind('<Return>', b3)
cvs.create_window(190, 60, window=ent3)

lbl8 = tk.Label(win, text = 'Octal(Base 8)')
cvs.create_window(60, 90, window = lbl8)

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

ent8 = tk.Entry(win)
ent8.bind('<Return>', b8)
cvs.create_window(190, 90, window=ent8)

lbl10 = tk.Label(win, text = 'Decimal(Base 10)')
cvs.create_window(60, 120, window = lbl10)

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

ent10 = tk.Entry(win)
ent10.bind('<Return>', b10)
cvs.create_window(190, 120, window=ent10)

lbl12 = tk.Label(win, text = 'Duodecimal(Base 12)')
cvs.create_window(60, 150, window = lbl12)

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

ent12 = tk.Entry(win)
ent12.bind('<Return>', b12)
cvs.create_window(190, 150, window=ent12)

lbl16 = tk.Label(win, text = 'Hexadecimal(Base 16)')
cvs.create_window(60, 180, window = lbl16)

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
    
ent16 = tk.Entry(win)
ent16.bind('<Return>', b16)
cvs.create_window(190, 180, window=ent16)

win.mainloop()