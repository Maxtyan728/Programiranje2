def print_string_recursive(input_string):
    if len(input_string)==0:
        return #ako je prazno rekurzija se prekida

    print(input_string[0], end='')
    print_string_recursive(input_string[1:])
    
