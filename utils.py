

import glob
import os
from jinja2 import Template
import markdown

pages = []

def main():
    for page in pages:
        index_page = replace_template(page)
        open(page['output'], "w+").write(index_page)



def dict():
    all_html_files = glob.glob("content/*.html")
    for file in all_html_files:
        file_path = file
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        list_dict = {}
        list_dict['filename'] = filename
        list_dict['title'] = name_only
        list_dict['output'] = 'docs/' + file_name
        pages.append(list_dict)


def replace_template(datum):
    page_html = open(page['filename']).read()
    template_html = open("templates/base.html").read()
    footer = 'Learn to code. Code away!'
    index_page = Template(template_html)
    index_page = index_page.render(
        title = page['title'],
        footer = footer,
        content = page_html,
        )
    return index_page
    
    
def markdown_converted(page):
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    data = open(page['filename']).read()
    html = md.convert(data)
    return html


main()




