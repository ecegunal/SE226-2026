from lab6 import geometry_utils

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

operation = input("Enter the operation you want to perform: ").strip().lower()

valid_operations = ["circle_area", "circle_perimeter", "rectangle_area", "rectangle_perimeter", "triangle_area"]

if operation not in valid_operations:
    print("Input Error: Invalid operation. Please choose a valid shape and calculation.")
else:
    try:
        if operation in ["circle_area", "circle_perimeter"]:
            radius = float(input("Enter radius: "))
            if operation == "circle_area":
                result, error = geometry_utils.circle_area(radius)
            else:
                result, error = geometry_utils.circle_perimeter(radius)

        elif operation in ["rectangle_area", "rectangle_perimeter"]:
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            if operation == "rectangle_area":
                result, error = geometry_utils.rectangle_area(width, height)
            else:
                result, error = geometry_utils.rectangle_perimeter(width, height)

        elif operation == "triangle_area":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result, error = geometry_utils.triangle_area(base, height)

        if error:
            print(error)
        else:
            print(f"Result: {result}")

    except ValueError:
        print("Input Error: Please enter valid numeric values.")