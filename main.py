import random


def main():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    number3 = random.randint(0, 100)
    
    if(number2<number1):
        if(number3<number2):
            min_value = number3
        else:
            min_value = number2
    elif(number3<number1):
        if(number2<number3):
            min_value = number2
        else:
            min_value = number3
    else:
        min_value = number1
        
    print(f'{number1}, {number2}, {number3}, minimum: {min_value}')

    ########################################
    # Do not delete the return statement
    ########################################
    return number1, number2, number3, min_value


if __name__ == '__main__':
    main()
