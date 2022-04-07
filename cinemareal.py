confirm = "N"
dorm = "Y"
while confirm == "N":
    while dorm == "Y":
        def welcomeandquestions():
            #Welcoming message
            print("Welcome to our cozy cinema")

            #asking user for their information
            user_name= input("May I have your name ")
            user_phone= ''

            #validating phone number
            
            while not user_phone.isnumeric():
                user_phone= input("what is the valid phone number that you ordered the movie? ")
                if not user_phone.isnumeric():
                    print("bad phonenumber") 
        welcomeandquestions()  

        #movie selections
        print ("1 = The lost city")
        print ("2 = Death on the Nile")
        print ("3 = Turning red")
        def movies (movie):
            movie = movie.lower()
            match movie:
                case '1':
                    return 'The lost city'
                case '2':
                    return 'Death on the Nile'
                case '3':
                    return 'Turning red'
                case _:
                    return 'Unidentified movie'
        
        movie = input("Which movie? ")
        print (movies(movie))

        while (movies(movie)) == 'Unidentified movie':
            if (movies(movie)) != 'Unidentified movie':
                print("thank you for the information")
                break
            else:
                print(" ")
                print("There is a mistake we only have these 3 movies")
                print ("1 = The lost city")
                print ("2 = Death on the Nile")
                print ("3 = Turning red")
                movie = input("Which movie would you like to watch? ")
                print (movies(movie))

    
        #Choosing at what time to watch

        print ("1 = Morning")
        print ("2 = Noon")
        print ("3 = Evening")
        def times (time):
            mtime = time.lower()
            match time:
                case '1':
                    return 'Morning'
                case '2':
                    return 'Noon'
                case '3':
                    return 'Evening'
                case _:
                    return 'Invalid time'
                                
        time = input("What time would you like to watch? ")
        print (times(time))

        while (times(time)) == 'Invalid time':
            if (times(time)) != 'Invalid time':
                print("Thank you for information")
                break
            else:
                print(" ")
                print("We dont have the movie at that time.")
                print ("9 = Morning")
                print ("4 = Noon")
                print ("7 = Evening")
                time = input("What Time? ")
                print (times(time))

        #booking available seat
        available_seats = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)', ]
        print (available_seats)
        def seats (seat):
            seat = seat.lower()
            match seat:
                case '1':
                    return 0
                case '2':
                    return 1
                case '3':
                    return 2
                case '4':
                    return 3
                case '5':
                    return 4
                case '6':
                    return 5
                case '7':
                    return 6
                case '8':
                    return 7
                case '9':
                    return 8
                case '10':
                    return 9
                case _:
                    return 'Invalid seat'
                    
        #seat validation            
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
                    print (available_seats)
                    seat = input("Which Seat? ")
                    print(" ")
                    
        available_seats[seats(seat)] = "(X)"
        print(available_seats)

        #confirmation of the booking
        print('confirm order: movies: ', (movies(movie)), ", time:", (times(time)), ", seats:", (available_seats), )
        confirm = input("confirm? Y/N ")
        
        if confirm == "Y":
            print("Your seat has been confirmed\n")
            """ dorm = input("book seat? Y/N ")
            if dorm == "N":"""
            break
        elif confirm == "N":
            while confirm == 'N':
                print()
                dorm = input("book again? Y/N ")
                if dorm == "N":
                    confirm == "Y"
                    print("thank you")
                    break
                elif dorm == "Y":
                    break
                else:
                    print("invalid input")
        else: 
            print("Invalid input")
            confirm = input("confirm? Y/N ")
