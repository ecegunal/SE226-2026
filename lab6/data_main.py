from lab6.data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum,
)

raw_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

raw_list = raw_input.split(",")
cleaned_strings = strip_whitespaces(raw_list)

num_list = []
valid = True
for s in cleaned_strings:
    try:
        num_list.append(float(s))
    except ValueError:
        valid = False
        break

if not valid:
    print("Data Error: Please make sure you only enter numbers separated by commas.")
else:
    unique_list = remove_duplicates(num_list)
    print(f"Cleaned and unique data: {unique_list}")
    print("-" * 20)
    print(f"Mean: {calculate_mean(unique_list):.2f}")
    print(f"Maximum: {find_maximum(unique_list)}")
    print(f"Minimum: {find_minimum(unique_list)}")