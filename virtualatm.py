"""
Virtual ATM Machine
"""
import sys
def  main():
    """
    Our main function: ATM MACHINE.
    """
    counter = 0
    while counter >= 0:
        pin = input('Please enter your four digit pin: ')
        if pin == ('1234'):
            print('Your account balance is: $0. Goodbye')
            sys.exit()
        elif pin != ('1234'):
            print('Invalid PIN')
            counter += 1
            if counter == 3:
                print('Account locked. The police is on its way.')
                break






if __name__ == '__main__':
    main()
