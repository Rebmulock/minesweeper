size = input('Enter area size (min. 5): ')

input_is_valid_int = False

while input_is_valid_int != True:
    try:
        size = int(size)
        
        if size <= 4:
            print('Please enter valid number')

            size = input('Enter area size: ')

        else:
            input_is_valid_int = True

    except:
        print('Please enter valid number')

        size = input('Enter area size: ')

area = [x for x in range(size**2)]
pick_from = [x for x in range(size**2)]