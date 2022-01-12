"""
            2.count (up or down).
Ask which direction the user wants to count (up or down).
 If they select up,
 then ask them for the top number and then count from 1 to that number.
 If they select down, ask them to enter a number below 20
 and then count down from 20 to that number.
 If they entered something other than up or down,
 display the message “I don’t understand”.

"""
direction = input("which direction you wants to count ? \n\t\t(1.UP or 2.Down)\n\r")
direction.lower()
if direction == "up" or direction == "1" or direction == "u":
    num = int(input("Enter Top number : "))
    index = 1
    while index.__le__(num):
        print(index, end=" - ")
        index += 1
elif direction == "down" or direction == "2" or direction == "d":
    num = int(input("Enter number below 20 : "))
    index = 20
    while index.__ge__(num):
        print(index, end=" - ")
        index -= 1
else:
    print("\t\tI don’t understand .")

print("\n\t\t Thank you ^_^")
