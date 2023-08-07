# Define the preset for the material class
import datetime

preset = """
class $material1(MaterialAPI):
	def __init__(self):
		super().__init__()
		self.get()

	def get(self):
		return Py2J(code="Material.$material2", imports=["org.bukkit.Material"])
"""

file = open("materials.txt", "r")  # open materials.txt file
lines = file.readlines()  # real all lines
for i in range(len(lines)):
	lines[i] = lines[i].replace("\n", "")  # remove all newlines in strings

lines_j = "\n".join(lines)  # join

# define some information variables
return_value = f""
legacy_removed = 0
empty_strings = 0
success = 0
version = "1.1 for MC 1.20.1 (paper-api-1.20.1-R0.1)"
return_value += f"# Generated with Py2McMaterialBuilder-{version} at {datetime.datetime.now()}\n"

# for each line
for line in lines_j.split("\n"):
	if line == "":  # if the line is empty, we don't care about it
		empty_strings += 1
		continue
	if line.startswith("LEGACY"):  # if it is a legacy material, we don't care about it
		legacy_removed += 1
		continue

	print(line)  # dev info for materials
	return_value += f"{preset.replace('$material1', line).replace('$material2', line)}\n"  # make the preset work with the material
	success += 1

# outcome
print(f"\nRemoved {legacy_removed} legacies")
print(f"Removed {empty_strings} empty strings")
print(f"Made {success} successes")
print(f"Dev info: {success} to {empty_strings - legacy_removed}")
print("\nGenerating output.py...")
with open("output.py", "w") as output_file:
	output_file.write(return_value)  # write the output.py

print("Finished!")
