confirm = "N"
doot = "Y"
while confirm == "N":
    while doot == "Y":
        def welcomeandquestions():
            # Welcoming message
            print("Welcome to our cozy cinema")

            # asking user for their information
            user_name = input("May I have your name ")
            user_phone = ''

            # validating phone number

            while not user_phone.isnumeric():
                user_phone = input(
                    "what is the valid phone number that you ordered the movie? ")
                if not user_phone.isnumeric():
                    print("bad phonenumber")
        welcomeandquestions()

        # movie selections
        print("1 = The lost city")
        print("2 = Death on the Nile")
        print("3 = Turning red")

        def movies(movie):
            movie = movie.lower()
            """match movie:
                case '1':
                    return 'The lost city'
                case '2':
                    return 'Death on the Nile'
                case '3':
                    return 'Turning red'
                case _:
                    return 'Unidentified movie'"""
            if movie=='1':
                return 'The lost city'
            elif movie=='2':
                return 'Death on the Nile'
            elif movie=='3':
                return 'Turning red'
            else:
                return 'Unidentified movie'
                
        movie = input("Which movie? ")
        print(movies(movie))

        while (movies(movie)) == 'Unidentified movie':
            if (movies(movie)) != 'Unidentified movie':
                print("thank you for the information")
                break
            else:
                print(" ")
                print("There is a mistake we only have these 3 movies")
                print("1 = The lost city")
                print("2 = Death on the Nile")
                print("3 = Turning red")
                movie = input("Which movie would you like to watch? ")
                print(movies(movie))

        # Choosing at what time to watch

        print("1 = Morning")
        print("2 = Noon")
        print("3 = Evening")

        def times(time):
            mtime = time.lower()
            """match time:
                case '1':
                    return 'Morning'
                case '2':
                    return 'Noon'
                case '3':
                    return 'Evening'
                case _:
                    return 'Invalid time'"""
            if time=='1':
                return 'Morning'
            elif time=='2':
                return 'Noon'
            elif time=='3':
                return 'Evening'
            else:
                return 'Invalid time'

        time = input("What time would you like to watch? ")
        print(times(time))

        while (times(time)) == 'Invalid time':
            if (times(time)) != 'Invalid time':
                print("Thank you for information")
                break
            else:
                print(" ")
                print("We dont have the movie at that time.")
                print("1 = Morning")
                print("2 = Noon")
                print("3 = Evening")
                time = input("What Time? ")
                print(times(time))

        # booking available seat
        available_seats = ['(1)', '(2)', '(3)', '(4)', '(5)',
                           '(6)', '(7)', '(8)', '(9)', '(10)', ]
        print(available_seats)

        def seats(seat):
            try:
                seat = int(seat)
                return seat-1
            except:
                return "Invalid seat"

        # seat validation
        seat = input("Which Seat? ")
        if (seats(seat)) == 'Invalid seat':
            while (seats(seat)) == 'Invalid seat':
                seat = input("Which Seat? ")
                if (seats(seat)) != 'Invalid seat':
                    available_seats[seats(seat)] = "(X)"
                    break
                else:
                    print(" ")
                    print("error, input not accepted.")
                    print(" ")
                    print(available_seats)
                    seat = input("Which Seat? ")
                    print(" ")

        available_seats[seats(seat)] = "(X)"
        print(available_seats)

        # confirmation of booking
        print('confirm order: movies: ', (movies(movie)), ", time:",
              (times(time)), ", seats:", (available_seats), )
        confirm = input("confirm? Y/N ")

        if confirm == "Y":
            print("Your seat has been confirmed\n")
            """ doot = input("book seat? Y/N ")
      if doot == "N":"""
            break
        elif confirm == "N":
            while confirm == 'N':
                print()
                doot = input("book again? Y/N ")
                if doot == "N":
                    confirm == "Y"
                    print("thank you")
                    break
                elif doot == "Y":
                    break
                else:
                    print("invalid input")
        else:
            print("Invalid input")
            confirm = input("Do you want to book again? Y/N ")
            
