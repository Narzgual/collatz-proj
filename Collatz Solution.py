



def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result =  3 * number + 1
        print(result)
        return result


def main():
    ##############      validating the integer input
    while True:
        try:
            number = int(input('enter an int'))
            break
        except:
            print('please enter an int')

            #######################
    while number != 1: ###### while number is not equal to 1: call the coolatz function
        number = collatz(number)  # call collatz() function on the number


if __name__ == "__main__":      ######run the program
    main()
