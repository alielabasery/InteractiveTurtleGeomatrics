import math
import turtle

def move_to(pen, destination_x, destination_y):
    pen.up()
    pen.goto(destination_x, destination_y)
    pen.down()

def draw_axes(pen, width, height):
    center_x, center_y = width / 2, height / 2
    move_to(pen, 0, center_y)
    pen.goto(width, center_y)
    move_to(pen, center_x, 0)
    pen.setheading(90)
    pen.goto(center_x, height)

def draw_circle_and_line(pen, xc, yc, r, x1, y1, x2, y2):
    pen.setheading(0)
    move_to(pen, xc, yc - r)
    pen.pencolor("red")
    pen.circle(r)
    move_to(pen, x1, y1)
    pen.pencolor("blue")
    pen.goto(x2, y2)

def draw_intersection_circles(pen, intersections, intersection_r):
    pen.pencolor("green")
    for intersection in intersections:
        move_to(pen, intersection[0], intersection[1] - intersection_r)
        pen.circle(intersection_r)

def draw_text(pen, x, y, text, font_size=16, align="center"):
    move_to(pen, x, y)
    style = ("Arial", font_size)
    pen.write(text, font=style, align=align)

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Error: Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input. Please enter a valid float.")

def calculate_intersections(xc, yc, r, x1, y1, x2, y2):
    a = (x2 - x1)**2 + (y2 - y1)**2
    b = 2 * ((x2 - x1) * (x1 - xc) + (y2 - y1) * (y1 - yc))
    c = xc**2 + yc**2 + x1**2 + y1**2 - 2 * (xc * x1 + yc * y1) - r**2

    discriminant = b**2 - 4 * a * c

    if discriminant < 0 or a == 0:
        print("Error: No intersection or division by zero encountered. Redirecting back to menu.")
        return None  # No intersection

    alpha1_denominator = 2 * a

    # Check for division by zero before performing the division
    alpha1 = (-b + math.sqrt(discriminant)) / alpha1_denominator if alpha1_denominator != 0 else None
    alpha2 = (-b - math.sqrt(discriminant)) / (2 * a) if (2 * a) != 0 else None

    if alpha1 is not None and 0 <= alpha1 <= 1:
        x1_intersection = (1 - alpha1) * x1 + alpha1 * x2
        y1_intersection = (1 - alpha1) * y1 + alpha1 * y2
    else:
        x1_intersection, y1_intersection = None, None

    if alpha2 is not None and alpha2 != alpha1 and 0 <= alpha2 <= 1:
        x2_intersection = (1 - alpha2) * x1 + alpha2 * x2
        y2_intersection = (1 - alpha2) * y1 + alpha2 * y2
    else:
        x2_intersection, y2_intersection = None, None

    return x1_intersection, y1_intersection, x2_intersection, y2_intersection

def change_colors(pen):
    circle_color = input("Enter circle color: ")
    line_color = input("Enter line color: ")

    pen.pencolor(circle_color)
    pen.circle(50)  # Draw a sample circle
    pen.pencolor(line_color)
    pen.forward(100)  # Draw a sample line

def main():
    # Setting up the window
    WIDTH, HEIGHT = 800, 600
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    turtle.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    turtle.hideturtle()

    turtle_pen = turtle.Turtle()

    while True:
        turtle_pen.clear()
        draw_axes(turtle_pen, WIDTH, HEIGHT)

        print("Menu:")
        print("1. Draw Circle and Line")
        print("2. Change Colors")
        print("3. Exit")

        try:
            choice = get_user_choice()

            if choice == 1:
                try:
                    # User input
                    xc = get_float_input("Enter the X-coordinate for the center of the circle: ")
                    yc = get_float_input("Enter the Y-coordinate for the center of the circle: ")
                    r = get_float_input("Enter the radius of the circle: ")
                    x1 = get_user_input("Enter the X-coordinate for the start of the line: ")
                    y1 = get_user_input("Enter the Y-coordinate for the start of the line: ")
                    x2 = get_user_input("Enter the X-coordinate for the end of the line: ")
                    y2 = get_user_input("Enter the Y-coordinate for the end of the line: ")

                    draw_circle_and_line(turtle_pen, xc, yc, r, x1, y1, x2, y2)

                    # Calculating intersections and drawing circles
                    intersections = calculate_intersections(xc, yc, r, x1, y1, x2, y2)

                    if intersections is not None:
                        intersection_r = 5  # intersection at the radius is equal to 5
                        draw_intersection_circles(turtle_pen, intersections, intersection_r)

                        # The text
                        draw_text(turtle_pen, WIDTH / 2, HEIGHT / 2, f"There are {len(intersections)} intersections")

                    else:
                        # No intersection
                        draw_text(turtle_pen, WIDTH / 2, HEIGHT / 2, "An intersection does not exist.")

                except Exception as e:
                    print(f"Error: {str(e)}. Redirecting back to menu.")

            elif choice == 2:
                try:
                    change_colors(turtle_pen)
                except Exception as e:
                    print(f"Error: {str(e)}. Redirecting back to menu.")

            elif choice == 3:
                break

        except Exception as e:
            print(f"Error: {str(e)}. Redirecting back to menu.")

    turtle.done()

if __name__ == "__main__":
    main()
