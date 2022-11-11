#!/usr/bin/env python3
# Created by: Patrice Pat-Odita
# Created on: Nov 10, 2022
#!/usr/bin/env python3
# This program asks the user how many numbers they want to add up.
# It then uses a while loop to calculate and display
# the sum of the numbers. A continue statement is also used.


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0
    answer = ""

    while True:
        # get user number as a string
        user_num_a_string = input("How many numbers would you like to add?: ")
        print("")

        try:
            # converts the first user input to integer
            user_num_a_int = int(user_num_a_string)

            if user_num_a_int >= 0:
                # calculate the sum of the entered numbers
                while loop_counter < user_num_a_int:
                    # gets input from user
                    user_num_b_string = input("Enter a whole number: ")

                    try:
                        # converts entered number from string to integer
                        user_num_b_int = int(user_num_b_string)
                        # joins the strings

                        if user_num_b_int < 0:
                            print(
                                "{} is < 0 and cannot be added".format(user_num_b_int)
                            )
                            print("")
                            continue

                        print("{} added to the sum.".format(user_num_b_int))
                        print("")
                        sum = sum + user_num_b_int
                        loop_counter = loop_counter + 1
                        answer += str(user_num_b_int) + " + "
                    except Exception:
                        print("{} is not a number.".format(user_num_b_string))
                        print("")
                        continue
                if loop_counter == user_num_a_int:
                    print("{}0 = {} ".format(answer, sum))
                    print("The sum is {}.".format(sum))
                    break
            else:
                print("Please enter a whole number!")
                print("")
        except Exception:
            print("{} is not a number.".format(user_num_a_string))
            print("")


if __name__ == "__main__":
    main()
