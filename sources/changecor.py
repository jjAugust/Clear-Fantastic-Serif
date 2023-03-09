import random
import re

# Read in the .glyph file
with open("font.glyphs") as f:
    content = f.read()

# Define a regex pattern to match nodes with the format of the example you provided
pattern = r"\((\d+),(\d+),(\w+)\)"

# Loop through all matches of the pattern in the file
for match in re.findall(pattern, content):
    x, y, node_type = match

    # Only apply the adjustment to nodes with a "ls" node_type
    # Generate a random adjustment value of either +1, +2, -1, or -2 for both x and y coordinates
    x_adjustment = random.choice([-2, -1, 1, 2])
    y_adjustment = random.choice([-2, -1, 1, 2])

    # Calculate the new x and y coordinates
    new_x = int(x) + x_adjustment
    new_y = int(y) + y_adjustment

    # Replace the old node coordinates with the new ones in the content string
    old_node = f"({x},{y},{node_type})"
    new_node = f"({new_x},{new_y},{node_type})"
    content = content.replace(old_node, new_node)

# Write the modified content back to the .glyph file
with open("newfont.glyphs", "w") as f:
    f.write(content)
