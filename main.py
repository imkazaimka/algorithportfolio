"""
Programmer: Imronbek Shoniyozov

Program: Sorting, filtering, and aggregation functions

This program uses several Python methods which was not during the class , so here are how they work:

- isinstance(): Checks if an object is an instance of a specified class or subclass.

- append(): Adds an item to the end of a list.

- join(): Joins elements of an iterable (like a list or tuple) into a single string, separated by a specified separator.

- ljust(): Returns a left-justified version of a string, padding it with spaces (or another specified character) on the right to the specified width.

- strip(): Removes leading and trailing whitespaces (or specified characters) from a string.

Examples:

- isinstance() example:
  x = 5
  print(isinstance(x, int))  # True, because x is an integer

- append() example:
  my_list = [1, 2, 3]
  my_list.append(4)
  print(my_list)  # [1, 2, 3, 4]

- join() example:
  words = ['hello', 'world']
  joined_str = ' '.join(words)
  print(joined_str)  # "hello world"

- ljust() example:
  text = 'hello'
  padded_text = text.ljust(10, '-')
  print(padded_text)  # "hello-----"

- strip() example:
  text_with_spaces = '   hello world   '
  clean_text = text_with_spaces.strip()
  print(clean_text)  # "hello world"
"""

#Extended dataset to get 100 :)

dataset = [
    {"name": "James", "class": "FC01", "exam score": 75, "coursework score": 45, "nationality": "British"},
    {"name": "Natasha", "class": "FC02", "exam score": 95, "coursework score": 85, "nationality": "Russian"},
    {"name": "Kumail", "class": "FC02", "exam score": 85, "coursework score": 75, "nationality": "Pakistani"},
    {"name": "Tariq", "class": "FC01", "exam score": 75, "coursework score": 55, "nationality": "Egyptian"},
    {"name": "Qimeng", "class": "FC01", "exam score": 80, "coursework score": 80, "nationality": "Chinese"},
    {"name": "Ming", "class": "FC02", "exam score": 90, "coursework score": 75, "nationality": "Chinese"},
    {"name": "Ahmed", "class": "FC03", "exam score": 65, "coursework score": 50, "nationality": "Egyptian"},
    {"name": "Sofia", "class": "FC03", "exam score": 78, "coursework score": 72, "nationality": "Spanish"},
    {"name": "Omar", "class": "FC02", "exam score": 89, "coursework score": 85, "nationality": "Moroccan"},
    {"name": "Aisha", "class": "FC01", "exam score": 92, "coursework score": 90, "nationality": "Nigerian"},
    {"name": "Liam", "class": "FC03", "exam score": 81, "coursework score": 77, "nationality": "Canadian"},
    {"name": "Emma", "class": "FC02", "exam score": 87, "coursework score": 78, "nationality": "American"},
    {"name": "Lucas", "class": "FC01", "exam score": 70, "coursework score": 65, "nationality": "Brazilian"},
    {"name": "Amelia", "class": "FC03", "exam score": 83, "coursework score": 80, "nationality": "Australian"},
    {"name": "Noah", "class": "FC01", "exam score": 77, "coursework score": 68, "nationality": "British"},
    {"name": "Ava", "class": "FC02", "exam score": 88, "coursework score": 84, "nationality": "Canadian"},
    {"name": "Ethan", "class": "FC03", "exam score": 76, "coursework score": 74, "nationality": "Irish"},
    {"name": "Isabella", "class": "FC02", "exam score": 85, "coursework score": 70, "nationality": "Italian"},
    {"name": "William", "class": "FC01", "exam score": 68, "coursework score": 60, "nationality": "Australian"},
    {"name": "Mia", "class": "FC03", "exam score": 91, "coursework score": 89, "nationality": "American"},
    {"name": "Olivia", "class": "FC02", "exam score": 74, "coursework score": 65, "nationality": "British"},
    {"name": "Benjamin", "class": "FC01", "exam score": 66, "coursework score": 59, "nationality": "Dutch"},
    {"name": "Sophia", "class": "FC03", "exam score": 82, "coursework score": 76, "nationality": "French"},
    {"name": "Elijah", "class": "FC02", "exam score": 90, "coursework score": 85, "nationality": "Kenyan"},
    {"name": "Charlotte", "class": "FC01", "exam score": 79, "coursework score": 73, "nationality": "German"},
    {"name": "Logan", "class": "FC03", "exam score": 75, "coursework score": 67, "nationality": "Irish"},
    {"name": "Abigail", "class": "FC02", "exam score": 93, "coursework score": 86, "nationality": "American"},
    {"name": "Jack", "class": "FC01", "exam score": 84, "coursework score": 79, "nationality": "Canadian"},
    {"name": "Emily", "class": "FC03", "exam score": 78, "coursework score": 72, "nationality": "British"},
    {"name": "Oliver", "class": "FC02", "exam score": 86, "coursework score": 81, "nationality": "Irish"},
    {"name": "Grace", "class": "FC01", "exam score": 71, "coursework score": 68, "nationality": "French"},
    {"name": "Henry", "class": "FC03", "exam score": 80, "coursework score": 75, "nationality": "American"},
    {"name": "Ella", "class": "FC02", "exam score": 83, "coursework score": 77, "nationality": "Australian"},
    {"name": "Thomas", "class": "FC01", "exam score": 67, "coursework score": 64, "nationality": "British"},
    {"name": "Hannah", "class": "FC03", "exam score": 89, "coursework score": 84, "nationality": "Canadian"},
    {"name": "Isaac", "class": "FC02", "exam score": 73, "coursework score": 69, "nationality": "German"},
    {"name": "Chloe", "class": "FC01", "exam score": 88, "coursework score": 83, "nationality": "British"},
    {"name": "Alexander", "class": "FC03", "exam score": 76, "coursework score": 71, "nationality": "Greek"},
    {"name": "Zoey", "class": "FC02", "exam score": 94, "coursework score": 87, "nationality": "Canadian"},
    {"name": "Ansor", "class" : "FC03" , "exam score": 62 , "coursework score": 90 , "nationality" : "Turkbek"}
]





#Get key , becouse we can not use lambda
def get_key(item ,key):
    
    return item.get(key, None)





def filter_data(data, key, value, condition="equal"):
    """
    Filters the data based on a key-value pair or a numeric condition.
    It will return items that contain the given key and match the given condition.

    Arguments:
    data : list of dictionaries
    key : string, the key to filter by (e.g., 'class')
    value : the value to filter for (e.g., 'FC01')
    condition : string, specifies the condition ('equal', 'greater')

    Returns:
    filtered : list of dictionaries, containing only items that match the filter
    """
    if not isinstance(data, list):
        raise ValueError("Data must be a list of dictionaries.")

    filtered = []
    for item in data:
        if isinstance(item, dict) and key in item:
            item_value = item[key]

            # Convert both values to strings for comparison if not numeric
            if isinstance(item_value, (int, float)):
                if condition == "greater" and item_value > float(value):
                    filtered.append(item)
                elif condition == "equal" and item_value == float(value):
                    filtered.append(item)
            else:
                if condition == "equal" and str(item_value) == str(value):
                    filtered.append(item)
    return filtered







def aggregate_data(data, key):


    """
    Aggregates data by calculating statistics for a specific numeric key.
    It calculates the count, min, max, mean, median, and quartiles.
    
    Arguments:
    data : list of dictionaries
    key : string, the key to aggregate by (e.g., 'exam score')
    
    Returns:
    stats : dictionary, containing the statistics (count, min, max, mean, median, Q1, Q3)
    """


    if not isinstance(data, list):

        raise ValueError("Data must be a list of dictionaries.")


    # Extract the values of the given key from each dictionary in the data
    values = [item[key] for item in data if isinstance(item, dict) and key in item and isinstance(item[key], (int, float))]


    if not values:

        return None  #If there is no any values for this one


    # Sorting the values to calculate median, quartiles, etc
    values.sort()


    # Calculate statistics
    count = len(values)

    minimum = values[0]

    maximum = values[-1]

    mean = sum(values) / count

    median = calculate_median(values)

    Q1 = calculate_percentile(values, 25)

    Q3 = calculate_percentile(values, 75)


    stats = {
        "count": count,
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": median,
        "Q1": Q1,
        "Q3": Q3
    }
    return stats





def calculate_median(values):

    n = len(values)

    middle = n // 2


    if n % 2 == 1:

        return values[middle]

    else:

        return (values[middle - 1] + values[middle]) / 2





def calculate_percentile(values, percentile):

    k = (percentile / 100) * (len(values) - 1)

    f = int(k)

    c = k - f


    if f + 1 < len(values):

        return values[f] + c * (values[f + 1] - values[f])

    else:

        return values[f]





# Sorting Algorithm using bubble sort
def sort_data(data, key):
    """
    Sorts the data based on a given key using the Bubble Sort algorithm.

    Arguments:
    data : list of dictionaries
    key : string, the key to sort by (e.g., 'exam score')

    Returns:
    sorted_data : list of dictionaries, sorted by the given key
    """
    
    if not isinstance(data, list):
        raise ValueError("Data must be a list of dictionaries.")
    
    n = len(data)

    for i in range(n):

        for j in range(0, n-i-1):

            # Get the value of the current item and the next item
            if get_key(data[j], key) > get_key(data[j+1], key):
                
                # Swap the items if they're in the wrong order
                data[j], data[j+1] = data[j+1], data[j]
    
    return data





def display_menu():


    """
    Displays the menu options to the user.
    """


    print("\n" + "=" * 40)
    print("          Data Processing Menu         ")
    print("=" * 40)
    print("  [1]  Filter Data")
    print("  [2]  Aggregate Data")
    print("  [3]  Sort Data")
    print("  [4]  Display Dataset")
    print("  [5]  Exit")
    print("=" * 40)
    print("Choose an option by entering the number:")





def display_table(data):


    """
    Displays the data in a nicely formatted table.
    
    Arguments:
    data : list of dictionaries, the data to display
    """


    if not data:
        print("No data to display.")
        return


    # Get headers from the first row
    headers = data[0].keys()


    # Calculate column widths

    column_widths = {header: max(len(header), max(len(str(row.get(header, ""))) for row in data)) for header in headers}


    # Generate the header row, formatted with appropriate column widths
    # 'header.ljust(column_widths[header])' ensures each header is left-aligned and padded to the specified width
    # 'column_widths[header]' is the maximum width for each column, ensuring consistent column width across the table

    header_row = " | ".join(header.ljust(column_widths[header]) for header in headers)


    # Generate the separator line with hyphens, where the number of hyphens is determined by the column width
    # '-'.repeat(column_widths[header]) ensures each column has a separator matching its width
    # '-+-' is used to separate the columns' hyphen strings to match the table structure

    separator = "-+-".join("-" * column_widths[header] for header in headers)


    print(header_row)
    print(separator)


    # Print each row of data
    for row in data:
        row_str = " | ".join(str(row.get(header, "")).ljust(column_widths[header]) for header in headers)
        print(row_str)





def display_statistics(stats, key):


    """
    Displays the statistics for the given key (e.g., exam score).
    
    Arguments:
    stats : dictionary, containing the statistics (count, min, max, etc.)
    key : string, the key for which the statistics were calculated
    """


    if stats:
        # Statistics display
        print(f"\nStatistics for '{key}':")
        print(f"- Count: {stats['count']}")
        print(f"- Min: {stats['min']}")
        print(f"- Q1 (25th percentile): {stats['Q1']}")
        print(f"- Median (50th percentile): {stats['median']}")
        print(f"- Q3 (75th percentile): {stats['Q3']}")
        print(f"- Max: {stats['max']}")
        print(f"- Mean: {stats['mean']:.2f}")
    else:
        print(f"No valid data found for key '{key}'.")





def main():
    """
    Main function to run the data processing program.
    """

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":  # Filter Data
            print("\nChoose a key to filter by:")
            print("  [1] Name")
            print("  [2] Class")
            print("  [3] Nationality")
            print("  [4] Exam Score (greater than a value)")
            print("  [5] Coursework Score (greater than a value)")
            key_choice = input("Enter the number corresponding to your choice: ")

            if key_choice == "1":
                key = "name"
                value = input(f"Enter the value to filter for '{key}': ").strip()
                filtered_data = filter_data(dataset, key, value, condition="equal")
            elif key_choice == "2":
                key = "class"
                value = input(f"Enter the value to filter for '{key}': ").strip()
                filtered_data = filter_data(dataset, key, value, condition="equal")
            elif key_choice == "3":
                key = "nationality"
                value = input(f"Enter the value to filter for '{key}': ").strip()
                filtered_data = filter_data(dataset, key, value, condition="equal")
            elif key_choice == "4":
                key = "exam score"
                value = input(f"Enter the minimum value for '{key}': ").strip()
                filtered_data = filter_data(dataset, key, value, condition="greater")
            elif key_choice == "5":
                key = "coursework score"
                value = input(f"Enter the minimum value for '{key}': ").strip()
                filtered_data = filter_data(dataset, key, value, condition="greater")
            else:
                print("Invalid choice. Please try again.")
                continue

            print("\nFiltered Data:")
            display_table(filtered_data)


        elif choice == "2":  # Aggregate Data
            print("\nChoose a key to aggregate:")
            print("  [1] Exam Score")
            print("  [2] Coursework Score")
            key_choice = input("Enter the number corresponding to your choice: ")

            if key_choice == "1":
                key = "exam score"
            elif key_choice == "2":
                key = "coursework score"
            else:
                print("Invalid choice. Please try again.")
                continue

            stats = aggregate_data(dataset, key)
            display_statistics(stats, key)

        elif choice == "3":  # Sort Data
            print("\nChoose a key to sort by:")
            print("  [1] Name")
            print("  [2] Class ")
            print("  [3] Exam Score")
            print("  [4] Coursework Score")
            print("  [5] Nationality")
            key_choice = input("Enter the number corresponding to your choice: ")

            if key_choice == "1":
                key = "name"
            elif key_choice == "2":
                key = "class"
            elif key_choice == "3":
                key = "exam score"
            elif key_choice == "4":
                key = "coursework score"
            elif key_choice == "5":
                key = "nationality"
            else:
                print("Invalid choice. Please try again.")
                continue

            sorted_data = sort_data(dataset, key)
            print("\nSorted Data:")
            display_table(sorted_data)

        elif choice == "4":  # Display Dataset
            print("\nCurrent Dataset:")
            display_table(dataset)

        elif choice == "5":  # Exit Program
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")




# This is made to make it easier to deploy the project somewhere , it is a very good practice to sort everything to functions
if __name__ == "__main__":
    main()
