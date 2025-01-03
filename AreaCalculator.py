import math
###
https://www.codedex.io/@SahilChess/build/area-calculator
###

while True:
    print("""================== Area Calculator 📐 ==================  
    1) Triangle 
    2) Rectangle 
    3) Square 
    4) Circle 
    5) Quit """)

    choose = int(input("Choose an option: "))

    if choose == 1:
        tribase = float(input("Enter the base of the triangle: "))
        trih = float(input("Enter the height of the triangle: "))
        print("The area of the triangle is: ", (0.5 * tribase * trih))
    elif choose == 2:
        recw = float(input("Enter the width of the rectangle: "))
        rech = float(input("Enter the height of the rectangle: "))
        print("The area of the rectangle is: ", (recw*rech ))
    elif choose == 3:
        sqs = float(input("Enter the side of the square: "))
        print("The area of the square is: ", (sqs**2))
    elif choose == 4:
        circr = float(input("Enter the radius of the circle: "))
        print("The area of the circle is: ", (math.pi*circr)**2)
    elif choose == 5:
        print("Quit option chosen.")
        break
    else:
        print("Invalid option chosen. Please enter a number between 1 and 5.")









