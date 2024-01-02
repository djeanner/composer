import json

# Load JSON data
with open('composers.json', 'r') as file:
    data = json.load(file)

# Function to create HTML content for each composer
def create_html_for_composer(composer):
    html_content = f"""
    <html>
    <head>
        <title>{composer['fullName']}</title>
        <style>
            table, th, td {{
                border: 1px solid black;
                border-collapse: collapse;
            }}
            th, td {{
                padding: 5px;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <h1>{composer['fullName']}</h1>
        <h2>Works</h2>
        <table>
            <tr>
                <th>Title</th>
                <th>Opus</th>
                <th>Composition Date</th>
                <th>Year of Composition</th>
                <th>Instruments</th>
                <th>Type</th>
            </tr>"""

    for work in composer['compositions']:
        html_content += f"""
            <tr>
                <td>{work['title']}</td>
                <td>{work.get('opus', 'N/A')}</td>
                <td>{work.get('compositionDate', 'N/A')}</td>
                <td>{work.get('yearOfComposition', 'N/A')}</td>
                <td>{', '.join(work.get('instruments', []))}</td>
                <td>{work.get('type', 'N/A')}</td>
            </tr>"""

    html_content += """
        </table>
    </body>
    </html>"""
    
    return html_content

# Generate HTML files for each composer
for composer in data['composers']:
    filename = composer['lastName'].lower() + '.html'
    html_content = create_html_for_composer(composer)
    with open(filename, 'w') as file:
        file.write(html_content)

