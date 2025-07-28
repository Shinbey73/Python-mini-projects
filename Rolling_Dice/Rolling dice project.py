import random

def rolling_dice():
    return random.randint(1,6)

def main():
    print('\n===============WELCOME TO THE DICE ROLLING SIMULATOR!================')
    
    while True:
        print('\nDo you want to roll the dice?\n')

        try:
            
            user_input = input('Enter "y" or "n": ').lower()

            if user_input != 'y' and user_input != 'n':
                raise error

            if user_input == 'y':
                print('\nRolling the dice...')
                print('\nThe dice shows: ', rolling_dice())
            
            elif user_input == 'n':
                print('\nGoodbye!')
                break
            
        except Exception as error:
            print('\nInvalid input. Please enter "y" or "n" only!.')
            continue


if __name__ == '__main__':
    main()

