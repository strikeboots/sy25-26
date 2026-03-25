A1 = ["A1" , "Hundai Accent WRC", 220, (221, 300), 5500, 4.5, 1998, 4]
D1 = ["D1" , "Mitsubishi Lancer RS", 220, (219, 300), 6200, 5.9, 1997, 4]
D2 = ["D2" , "Toyota Celica GT-Four", 245, (220, 299), 5600, 5.3, 1998, 4]
B4 = ["B4", "VW Golf-Kit-Car", 220, (191, 260), 8000, 6.2, 1998, 4]
E1 = ["E1" , "Mitsubishi Carisma GT", 225, (213, 290), 6000, 5.2, 1996, 4]
D3 = ["D3" , "Seat Toledo Marathon", 220, (195, 330), 9400, 5.2, 2100, 5]
C1 = ["C1" , "Subaru Impreza WRC", 220, (221, 330), 5500, 5.4, 1994, 4]
A2 = ["A2" , "Ford Focus WRC", 224, (221, 300), 5400, 5.5, 1995, 4]
F1 = ["F1" , "VW Off-Road-Bug", 185, (104, 142), 6000, 9.0, 1880, 4]
G2 = ["G2" , "Seat Ibiza GTi", 220, (205, 280), 8400, 6.5, 1984, 4]

cars = [A1, D1, D2, B4, E1, D3, C1, A2, F1, G2]

def print_car(c):
    print("+" + "-"*38 + "+")
    print(f"| {c[1]:^38} |")
    print("+" + "-"*38 + "+")
    left = [
        f"Class: {c[0]}",
        f"Top Speed: {c[2]} km/h",
        f"HP: {c[3][0]}",
        f"RPM: {c[4]}",
    ]
    right = [
        f"0-100 km/h: {c[5]}s",
        f"Torque: {c[3][1]} Nm",
        f"CCs: {c[6]}",
        f"Cylinders: {c[7]}",
    ]
    for l, r in zip(left, right):
        print(f"| {l:<18} | {r:<18} |")
    print("+" + "-"*38 + "+")

# Show list of cars
print("Available Cars:")
for idx, car in enumerate(cars, 1):
    print(f"{idx}. {car[1]}")

# Ask user for a car number
try:
    choice = int(input("Select a car by entering its number (1-10): ")) - 1
    if 0 <= choice < len(cars):
        print_car(cars[choice])
    else:
        print("Invalid choice.")
except ValueError:
    print("Please enter a valid number.")

