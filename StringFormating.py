while True:
    print("Enter 'x' for exit.")
    string = input('Please Enter any string: ')
    if string == 'x':
        break
    else:
        new_string = string.replace(" ","")
        print("\n New String after removing all spaces: ")
        print(new_string, '\n')
        
