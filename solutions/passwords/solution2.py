import itertools
import re

# String => altijd aan elkaar
with open('output.txt', 'w+') as output_file:
    for password in itertools.product(sorted("QWERTYUIOP"), repeat=6):
        passwordstring = "".join(password)
        if re.search(r"([AEIOU])\1", passwordstring) and re.search(r"([QWRTYP])\1", passwordstring):
            if len(set(passwordstring)) == 4:
                output_file.write(passwordstring + '\n')
