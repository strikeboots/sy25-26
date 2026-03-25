seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman']

upset_count = 0

# Link winners to seeds by index
for i, winner in enumerate(winners):
    seed = seeds[i]
    if seed >= 10:
        print(f"Ciderella Alert! {winner} pulls the upset!")
        upset_count += 1

print(f"Total number of upsets: {upset_count}")
