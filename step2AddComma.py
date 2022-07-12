import os

directory = "C:\\Users\\your dir\\Downloads\\results"

for root, subdirectories, files in os.walk(directory):
    for file in files:
        # if file.endswith('.json') and "hr=" in file:
        if file.endswith('.json'):
        # if "vm20210104hr=10" in file:
            filepath = os.path.join(root, file)
            with open(filepath) as f:
                lines = f.read().splitlines()

            with open(filepath, "w") as f:
                f.write("[")
                count = len(lines)
                # for line in lines:
                i = 0
                while (i < count-1):
                    line = lines[i]
                    f.write(line + ",\n")
                    i += 1
                f.write(lines[count-1]) 
                f.write("]")