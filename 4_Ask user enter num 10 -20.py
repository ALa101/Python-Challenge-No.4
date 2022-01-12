"""
            4.Ask the user to enter a number between 10 and 20
Ask the user to enter a number between 10 and 20.
 If they enter a value under 10,
  display the message “Too low” and ask them to try again.
   If they enter a value above 20,
   display the message “Too high” and ask them to try again.
    Keep repeating this until they enter a value
    that is between 10 and 20 and
     then display the message “Thank you”.

"""
Exit = True
while Exit:
    num = int(input("\t\tPleace Enter a number between 10 and 20  ^_*\n\r"))
    if num.__lt__(20) and num.__gt__(10):
        print("Thank you".center(40, "-") + "\n \t\t\t\t   ^_^")
        Exit = False
    elif num.__le__(10):
        print("Too low".center(40, "-") + "\n \t\t\t\t   ^_^")
    else:
        print("Too high".center(40, "-") + "\n \t\t\t\t   ^_^")
