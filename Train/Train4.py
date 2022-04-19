# Given a string of digits, you should replace any digit below 5 with '0'
# and any digit 5 and above with '1'. Return the resulting string.
#
# Note: input will never be an empty string

# Solution 1

def fake_bin(x):
    fakebin = ''
    for n in x:
        if int(n) < 5:
            fakebin += '0'
        else:
            fakebin += '1'
    return fakebin

# Solution 2

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

# Solution 3

def fake_bin(x):
    return "".join('0' if int(a) < 5 else '1' for a in x)

# Solution 4

def fake_bin(x):
    return x.translate(x.maketrans("0123456789", "0000011111"))

# Solution 5

def fake_bin(x):
    return x.translate(str.maketrans("0123456789", "0000011111"))