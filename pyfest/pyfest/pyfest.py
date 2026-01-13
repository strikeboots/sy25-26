print("Welcome to Py-Fest 2026 Stage Manager!")
print("")
print("---Py-Fest 2026 Stage Manager ---")
print("1. View Lineup & Total Time")
print("2. Add a New Band")
print("3. Move First Band to End (Late Arrival)")
print("4. Remove a Band by Name")
print("5. Move Band to Specific Position")
print("6. Exit")
input("Select an option (1-6): ")

lineup = ["{'name': 'The Pythonistas', '(Rock)': 30},
          {'name': 'Code Play', '(Indie)': 45},
          {'name': 'Syntax Error', '(Metal)': 60}]"

if choice == "1." or choice == "1":
    total_time = sum(band['duration'] for band in lineup)
    print("--- Current Lineup ---")
    for band in lineup:
        print(f"{band['name']} - {band['duration']} mins")
    print(f"Total Performance Time: {total_time} mins")