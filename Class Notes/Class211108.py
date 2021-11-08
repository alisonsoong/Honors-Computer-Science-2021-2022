# Alison Soong
# class 11/8/2021


# Easter program!
def Easter():

    print("This program calculates the date of Easter for a specific year")
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

    year = 0;
    while (True):
        try:
            year = eval(input("Enter a four-digit year from 1900-2099: "))
            if (1900<=year<=2099):
                break
            else:
                print("You did not enter a four-digit number in the range 1900-2099") 
        except SyntaxError:
            print("You did not enter a number. Please enter a four-digit year from 1900-2099")
        except NameError:
             print("You did not enter a number. Please enter a four-digit year from 1900-2099")
        except ValueError:
            print("You did not enter a number. Please enter a four-digit year from 1900-2099")
        except:
            print("Something went wrong. Please enter a four-digit year from 1900-2099")

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7

    day = 22 + d + e

    if (year == 1954 or
        year == 1981 or
        year == 2049 or
        year == 2076):
        day = day-7

    if 1 <= day <= 31:
        print("Easter is on March " + str(day) + ", " + str(year))
    elif day > 31:
        day = day-31
        print("Easter is on April " + str(day) + ", " + str(year))

    print("\nThanks for using this program!")
        


    

    

    
            
