# Function to convert from base 2 & base 10
def b2b10(n): # Requires Integer number as arguement
    r = 0
    i = 0
    while n > 0:
        if (n % 10) > 1:
            return -1 # Not a binary number
        r += (n%10) * 2 ** i
        n = int(n/10)
        i += 1
    return r

# Function to convert from base 3 & base 10
def b3b10(n): # Requires Integer number as arguement
    r = 0
    i = 0
    while n > 0:
        if n % 3 > 2:
            return -1 # Not a ternary number
        r += (n%3) * 3 ** i
        n = int(n/10)
        i += 1
    return r

# Function to convert from base 8 & base 10
def b8b10(n): # Requires Integer number as arguement
    r = 0
    i = 0
    while n > 0:
        if n % 8 > 7:
            return -1 # Not an octal number
        r += (n%8) * 8 ** i
        n = int(n/10)
    return r

# Function to convert from base 12 & base 10
def b12b10(n): # Requires String as arguement
    r = 0
    l = len(n)
    j = 0
    for i in range(l-1, -1, -1):
        if n[i] == 'a' or n[i] == 'A':
            r += 10
        elif n[i] == 'b' or n[i] == 'B':
            r += 11
        else:
            try:
                r += int(n[i]) * 12 ** j
            except ValueError:
                return -1
        j += 1
    return r

# Function to convert from base 16 & base 10
def b16b10(n): # Requires String as arguement
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
            try:
                r += int(n[i]) * 16 ** j
            except ValueError:
                return -1
        j += 1
    return r

# Function to convert from base 10 & base 2
def b10b2(n): # Requires Integer number as arguement
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        r = str(n % 2) + r
        n = int(n/2)
        i += 1
    return int(r)

# Function to convert from base 10 & base 3
def b10b3(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        r = str(n % 3) + r
        n = int(n/3)
        i += 1
    return int(r)

# Function to convert from base 10 & base 8
def b10b8(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        r = str(n % 8) + r
        n = int(n/8)
        i += 1
    return int(r)

# Function to convert from base 10 & base 12
def b10b12(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        if n % 12 == 10:
            r = 'A' + r
        elif n % 12 == 11:
            r = 'B' + r
        else:
            r = str (n % 12) + r
        n = int(n/12)
        i += 1
    return r

# Function to convert from base 10 & base 16
def b10b16(n):
    r = '0' if n == 0 else ''
    i = 0
    while n > 0:
        if n % 16 == 10:
            r = 'A' + r
        elif n % 16 == 11:
            r = 'B' + r
        elif n % 16 == 12:
            r = 'C' + r
        elif n % 16 == 13:
            r = 'D' + r
        elif n % 16 == 14:
            r = 'E' + r
        elif n % 16 == 15:
            r = 'F' + r
        else:
            r = str(n % 16) + r
        n = int(n/16)
        i += 1
    return r