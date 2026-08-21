# ============================================================
# PROGRAM: REPEATABLE RADIAL PATTERN (MENU BASED)
# ============================================================

import turtle

# Step 1: Function to draw shape
def draw_shape(t, shape, size):

    if shape == "triangle":
        for i in range(3):
            t.forward(size)
            t.left(120)
            
    elif shape == "square":
        for i in range(4):
            t.forward(size)
            t.left(90)

    elif shape == "pentagon":
        for i in range(5):
            t.forward(size)
            t.left(72)

    elif shape == "hexagon":
        for i in range(6):
            t.forward(size)
            t.left(60)

    elif shape == "circle":
        t.circle(size)


# Step 2: Radial pattern function
def radial_pattern(t, shape, size, count):
    for i in range(count):
        draw_shape(t, shape, size)
        t.left(360 / count)


# Step 3: Create turtle
t = turtle.Turtle()
t.pensize(2)
t.speed(2)


# ============================================================
# Step 4: LOOP for repeated choices
# ============================================================
while True:

    print("\n--- RADIAL PATTERN MENU ---")
    print("1. Triangle")
    print("2. Square")
    print("3. Pentagon")
    print("4. Hexagon")
    print("5. Circle")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Clear previous drawing
    t.clear()

    if choice == 1:
        shape = "triangle"
    elif choice == 2:
        shape = "square"
    elif choice == 3:
        shape = "pentagon"
    elif choice == 4:
        shape = "hexagon"
    elif choice == 5:
        shape = "circle"
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
        continue

    # Step 5: Take input for pattern
    size = int(input("Enter size: "))
    count = int(input("Enter number of repetitions: "))

    # Step 6: Draw pattern
    radial_pattern(t, shape, size, count)


# Step 7: End turtle
turtle.done()