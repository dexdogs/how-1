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

# 1. Hide the table header for 'Name'
content = content.replace(
    '<th>Name</th>',
    '<th style="display: none;">Name</th>'
)

# 2. Hide the table data cell for 'Name'
content = content.replace(
    '<td class="td-name">${esc(name)}</td>',
    '<td class="td-name" style="display: none;">${esc(name)}</td>'
)

with open(file_path, "w") as f:
    f.write(content)

print("Successfully hidden the 'Name' column!")
