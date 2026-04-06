import glob

# Automatically find the HTML file in the workspace
files = glob.glob("**/basis-point-earth-1.html", recursive=True)
if not files:
    print("Error: Could not find basis-point-earth-1.html in this workspace.")
    exit(1)

file_path = files[0]
print(f"Found file at: {file_path}")

with open(file_path, "r") as f:
    content = f.read()

# 1. Replace the sorting logic
content = content.replace(
    'allStartups.sort((a, b) => countFilledFields(b) - countFilledFields(a));',
    'allStartups.sort((a, b) => (a.short_name || "").localeCompare(b.short_name || ""));'
)

# 2. Replace the comment for future clarity
content = content.replace(
    '// Sort descending by amount of filled fields',
    '// Sort alphabetically by Ticker Name (short_name)'
)

with open(file_path, "w") as f:
    f.write(content)

print("Successfully updated default sort to alphabetical by Ticker Name!")
