import os
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

# 1. Add to the table headers
content = content.replace(
    '          <th>Name</th>',
    '          <th>Ticker Name</th>\n          <th>Name</th>'
)

# 2. Add variable extraction in renderTable()
content = content.replace(
    '    const name = s.name || "—";',
    '    const short_name = s.short_name || "—";\n    const name = s.name || "—";'
)

# 3. Add to the row template in renderTable()
content = content.replace(
    '      <td class="td-name">${esc(name)}</td>',
    '      <td>${esc(short_name)}</td>\n      <td class="td-name">${esc(name)}</td>'
)

# 4. Add to the PUBLIC_FIELDS array for the detail panel
content = content.replace(
    '      ["Name", s.name],',
    '      ["Ticker Name", s.short_name],\n      ["Name", s.name],'
)

with open(file_path, "w") as f:
    f.write(content)

print("Successfully added 'Ticker Name' as the first column with default Space Grotesk font!")
