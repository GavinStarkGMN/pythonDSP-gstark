def mytolower(s):
    output = []
    for c in s:
        i = ord(c)
        if i >= ord('A') and i <= ord('Z'):
            output.append(chr(i+32))
        else:
            output.append(c)
    return output
