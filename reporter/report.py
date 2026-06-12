import csv
import sys

input_file = '/data/data.csv'
output_file = '/data/report.html'
results = []
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        results.append(row)
html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>K-POP Report</title>
    <style>
        body {{ font-family: Arial; margin: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #ff69b4; color: white; }}
    </style>
</head>
<body>
    <h1>K-POP Groups</h1>
    </table>
        <tr>
            <th>ID</th>
            <th>Group</th>
            <th>Label</th>
            <th>Year</th>
            <th>Genre</th>
            <th>Sales</th>
            <th>Listeners</th>
        </tr>
        {''.join(f'<tr><td>{g["group_id"]}</td><td>{g["group_name"]}</td><td>{g["label"]}</td><td>{g["debut_year"]}</td><td>{g["genre"]}</td><td>{g["album_sales"]}M</td><td>{g["monthly_listeners"]}M</td></tr>' for g in results)}
    </table>
</body>
</html>'''
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)