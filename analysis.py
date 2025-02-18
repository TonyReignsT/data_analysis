# I have added a feature to allow the user to search for life expectancy data by year or by country name and display the average life expectancy, maximum life expectancy, and minimum life expectancy for the year or country the user inputs.
with open("life-expectancy.csv") as expectancy_file: # will automatically close the file after the block of code is executed
    # Skip the header row
    next(expectancy_file)

    highest_expectancy = 0
    lowest_expectancy = 100
    total_expectancy = 0
    count = 0

    # To work on the highest and lowest life expectancy for the entire dataset
    highest_entity = ""
    highest_year = ""
    lowest_entity = ""
    lowest_year = ""

    # Prompt the user to choose between searching by year or by country
    search_option = input("Do you want to search by year or by country? (Enter 'year' or 'country'): ").strip().lower()

    if search_option == 'year':
        user_input_year = int(input("Enter the year of interest: "))
        print()

        # To work on the highest and lowest life expectancy for the year the user inputs
        highest_year_expectancy = 0
        lowest_year_expectancy = 100
        highest_year_entity = ""
        lowest_year_entity = ""

        for line in expectancy_file:
            data = line.split(",")
            life_expectancy = float(data[3])

            entity = data[0]
            code = data[1]
            year = data[2]

            if user_input_year == int(year):
                total_expectancy += life_expectancy
                count += 1

                # To work on the highest life expectancy for the year the user inputs
                if life_expectancy > highest_year_expectancy:
                    highest_year_expectancy = life_expectancy
                    highest_year_entity = entity

                # To work on the lowest life expectancy for the year the user inputs
                if life_expectancy < lowest_year_expectancy:
                    lowest_year_expectancy = life_expectancy
                    lowest_year_entity = entity

            if life_expectancy > highest_expectancy:
                highest_expectancy = life_expectancy
                highest_entity = entity
                highest_year = year

            if life_expectancy < lowest_expectancy:
                lowest_expectancy = life_expectancy
                lowest_entity = entity
                lowest_year = year

        # Data based on the entire dataset
        print(f"The overall max life expectancy is: {highest_expectancy:.2f} from {highest_entity} in {highest_year}")
        print(f"The overall min life expectancy is: {lowest_expectancy} from {lowest_entity} in {lowest_year}")
        print()

        # Data based on user input year
        print(f"For the year {user_input_year}:")
        if count > 0:
            print(f"The average life expectancy across all countries was: {(total_expectancy / count):.2f}")
            print(f"The maximum life expectancy was in {highest_year_entity} with {highest_year_expectancy:.2f}")
            print(f"The minimum life expectancy was in {lowest_year_entity} with {lowest_year_expectancy:.2f}")
        else:
            print(f"No data for the year {user_input_year}!")
        print()

    elif search_option == 'country':
        user_input_country = input("Enter the country of interest: ").strip()
        print()

        # To work on the highest and lowest life expectancy for the country the user inputs
        country_total_expectancy = 0
        country_count = 0
        country_highest_expectancy = 0
        country_lowest_expectancy = 100
        country_highest_year = ""
        country_lowest_year = ""

        for line in expectancy_file:
            data = line.split(",")
            life_expectancy = float(data[3])

            entity = data[0]
            code = data[1]
            year = data[2]

            if entity.lower() == user_input_country.lower():
                country_total_expectancy += life_expectancy
                country_count += 1

                if life_expectancy > country_highest_expectancy:
                    country_highest_expectancy = life_expectancy
                    country_highest_year = year

                if life_expectancy < country_lowest_expectancy:
                    country_lowest_expectancy = life_expectancy
                    country_lowest_year = year

            if life_expectancy > highest_expectancy:
                highest_expectancy = life_expectancy
                highest_entity = entity
                highest_year = year

            if life_expectancy < lowest_expectancy:
                lowest_expectancy = life_expectancy
                lowest_entity = entity
                lowest_year = year

        # Data based on the entire dataset
        print(f"The overall max life expectancy is: {highest_expectancy:.2f} from {highest_entity} in {highest_year}")
        print(f"The overall min life expectancy is: {lowest_expectancy} from {lowest_entity} in {lowest_year}")
        print()

        # Data based on user input country
        print(f"For the country {user_input_country}:")
        if country_count > 0:
            print(f"The average life expectancy was: {(country_total_expectancy / country_count):.2f}")
            print(f"The maximum life expectancy was: {country_highest_expectancy:.2f} in {country_highest_year}")
            print(f"The minimum life expectancy was: {country_lowest_expectancy:.2f} in {country_lowest_year}")
        else:
            print(f"No data for the country {user_input_country}!")
        print()

    else:
        print("Invalid option. Please enter 'year' or 'country'.")