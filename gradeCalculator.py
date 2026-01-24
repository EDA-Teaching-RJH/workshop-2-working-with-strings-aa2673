def main():
    while True:
        try:
            mark = int(input("What was your mark out of 100?"))
        except ValueError:
            print("Please enter your mark in numerical form")
            continue
        if mark >= 0 and mark <= 100:
            if mark >= 0 and mark < 60:
                print("Your grade is an F")
                break
            elif mark >= 60 and mark < 70:
                print("Your grade is a D")
                break
            elif mark >= 70 and mark < 80:
                print("Your grade is a C")
                break
            elif mark >= 80 and mark < 90:
                print("Your grade is a B")
                break
            else:
                print("Your grade is an A")
                break
        else:
            print("That isn't a valid mark")
            






main()