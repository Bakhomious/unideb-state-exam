import os
import yaml

def read_title(md_file):
    with open(md_file, 'r') as f:
        content = f.read()
        try:
            # Extract YAML front matter
            if content.startswith('---'):
                _, fm, _ = content.split('---', 2)
                metadata = yaml.safe_load(fm)
                return metadata.get('title', os.path.basename(md_file))
        except:
            pass
    return os.path.basename(md_file)

# HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>State Exam Materials</title>
    <style>
        body {{
            font-family: monospace;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            line-height: 1.6;
        }}
        h1, h2 {{
            font-family: monospace;
        }}
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>State Exam Materials</h1>
    {content}
</body>
</html>
"""

def main():
    # Get the correct paths
    src_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(src_dir)
    
    math_cs_topics = []
    informatics_topics = []
    
    # Collect and categorize all markdown files
    for filename in sorted(os.listdir(src_dir)):
        if filename.endswith('.md'):
            file_path = os.path.join(src_dir, filename)
            title = read_title(file_path)
            pdf_name = filename.replace('.md', '.pdf')
            
            if filename.startswith('1-'):
                math_cs_topics.append((pdf_name, title))
            elif filename.startswith('2-'):
                informatics_topics.append((pdf_name, title))
    
    # Generate HTML content
    content = []
    if math_cs_topics:
        content.append("<h2>Mathematics and Computer Science Topics</h2>")
        content.append("<ul>")
        for pdf_name, title in math_cs_topics:
            content.append(f'<li><a href="pdfs/{pdf_name}">{title}</a></li>')
        content.append("</ul>")
    
    if informatics_topics:
        content.append("<h2>Informatics Topics</h2>")
        content.append("<ul>")
        for pdf_name, title in informatics_topics:
            content.append(f'<li><a href="pdfs/{pdf_name}">{title}</a></li>')
        content.append("</ul>")
    
    # Write the index.html file
    index_path = os.path.join(project_root, 'index.html')
    with open(index_path, 'w') as f:
        f.write(html_template.format(content='\n'.join(content)))

if __name__ == '__main__':
    main()