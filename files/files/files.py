fname = "output.txt"
file = open(fname, "a")
for i in range(10):
    file.write(f"this is line {i}\n")
file.write("This is the first line.\n")
file.close()

