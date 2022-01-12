
"""
                    1.number below 50
Ask for a number below 50 and then count down from 50
to that number, making sure you show the number they entered in the output.
اطلب رقمًا أقل من 50 ثم عد تنازليًا من 50 إلى هذا الرقم ، وتأكد من إظهار الرقم الذي أدخلته في الإخراج.

"""
Exit = True
while Exit:
    num = int(input("Enter number below 50 : \r"))
    if num < 50:
        i, Exit = 50, False
        while num.__le__(i):
            print(i , end=" ")
            i -= 1
    else:
        print("Erorr, pleace Enter number brlow 50 -_-")
print("\n\t\t\t\t\tThank you ^_^")