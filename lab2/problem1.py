def rotate_word(s, n):
    output = ''
    for c in s:
        base = 0
        i = ord(c)
        # figure out if we're lower or upper case
        if i >= ord('A') and i <= ord('Z'):
            base = ord('A')
        elif i >= ord('a') and i <= ord('z'):
            base = ord('a')
        else:
            # continue if it's a character
            output += c
            continue

        # rotate (with wrapping) and observe the offset for lower vs upper case
        output += chr(base + (i - base + n) % 26)
    return output

print(rotate_word('asdf', 26))
print(rotate_word('hello', 13))
print(rotate_word("""V'ir urneq vg fnvq gung gur jnl gb cvpx n oneore va n oneorefubc vf gb pubbfr gur bar jvgu gur jbefg unvephg--gurl phg rnpu bguref' unve.""", 13))
