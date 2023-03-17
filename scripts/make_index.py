import os

directory = os.path.dirname(os.path.abspath(__file__))
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

with open(os.path.join(directory, 'index.html'), 'w') as f:
    f.write('<html><body>')
    for file in html_files:
        f.write(f'<a href="{file}">{file}</a><br>')
    f.write('</body></html>')