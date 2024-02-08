
text = """listing_url<br>thumbnail_url<br>medium_url<br>picture_url<br>xl_picture_url<br>host_url<br>host_thumbnail_url<br>host_picture_url"""

rows = text.split("<br>")
table = "<table>"

for i in range(0, len(rows), 5):
    row = rows[i:i+5]
    table += "<tr>"
    for item in row:
        table += f"<td>{item}</td>"
    table += "</tr>"

table += "</table>"
print(table)
