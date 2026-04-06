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

# 1. Remove the onclick attribute from the row template
content = content.replace(
    '<tr onclick="showDetail(\'${id}\')">',
    '<tr>'
)

# 2. Remove the cursor: pointer CSS for table rows
css_target = """tbody tr {
  border-bottom: 1px solid var(--border);
  transition: background 0.1s;
  cursor: pointer;
}"""

css_replacement = """tbody tr {
  border-bottom: 1px solid var(--border);
  transition: background 0.1s;
}"""

content = content.replace(css_target, css_replacement)

with open(file_path, "w") as f:
    f.write(content)

print("Successfully removed click functionality and pointer cursor from table rows!")
