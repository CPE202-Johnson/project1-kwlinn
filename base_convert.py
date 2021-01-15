#integer -> string

def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    convert_string = "0123456789ABCDEF"
    if num < b:
        return convert_string[num]
    return convert(num // b, b) + convert_string[num % b]
      