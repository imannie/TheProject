

import glob
import os
from jinja2 import Template
import markdown

pages = []

def main():
    for datum in pages:
        index_page = replace_template(datum)
        open(datum['output'], "w+").write(index_page)



def dict():
    all_html_files = glob.glob("content/*.html")
    for file_path in all_html_files:
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
                     'filename': str(file_path),
                     'output': 'docs/' + str(file_name),
                     'title': 'Annie Project',
                     'footer': 'Learn to code. Code away!',
                     'pagename': 'index_page',
        })

def replace_template(datum):
    page_html = open(datum['filename']).read()
    template_html = open("templates/base.html").read()
    footer = 'Learn to code. Code away!'
    index_page = Template(template_html)
    index_page = index_page.render(
        title = datum['title'],
        footer = footer,
        content = page_html,
        )
    return index_page
    
    
def markdown_extexsion(datum):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    data = open(datum['filename']).read()
    html = md.convert(data)
    return html




main()




