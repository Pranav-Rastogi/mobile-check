import re

# Takes in a single number at a time and returns True if it is in correct 
# format else returns False
def correct_contact(num):
	num = str(num)
    p = re.match(r'((\+[ -]*)?((0)|(91))([ -]*\d{10})|(\d{10}))', num.strip())

    if p:
        return p.group(0) == num

    return False
