
#Combine HTML index file

index_body = open("content/index.html").read()
combine_index = top_template + index_body + bottom_template
open("docs/index.html", "w+").write(combine_index)

#Combine HTML about file
about_body = open("content/about.html").read()
combine_about = top_template + about_body + bottom_template
open("docs/about.html", "w+").write(combine_about)

#Combine HTML work file
work_body = open("content/work.html").read()
combine_work = top_template + work_body + bottom_template
open("docs/work.html", "w+").write(combine_work)

#Combine HTML contact file
contact_body = open("content/contact.html").read()
combine_contact = top_template + contact_body + bottom_template
open("docs/contact.html", "w+").write(combine_contact)


pages = [
              {
              'filename': 'content/index.html',
              'output': 'docs/index.html',
              'title': 'Annie Project',
              'pagename': 'index_page',
              },
              {
              'filename': 'content/about.html',
              'output': 'docs/about.html',
              'title': 'A little about me',
              'pagename': 'about_page',
              },
              {
              'filename': 'content/work.html',
              'output': 'docs/work.html',
              'title': 'My works',
              'pagename': 'work_page',
              },
              {
              'filename': 'content/contact.html',
              'output': 'docs/contact.html',
              'title': 'Contact Me',
              'pagename': 'contact_page',
              }
  ]
  
def main():
    top_template = open("templates/top.html").read()
    bottom_template = open("templates/bottom.html").read()
    base = top_template + "{{content}}" + bottom_template
    open("templates/base.html", "w+").write(base)


def loop(pages):
    template = open("templates/base.html").read()
    for datum in pages:
      filename = datum['filename']
      output = datum['output']
      title = datum['title']
      pagename = datum['pagename']
      index_content = open(datum['filename']).read()
      index_page = template.replace("{{content}}", index_content).replace("{{title}}", title)
      open(output, "w+").write(index_page)
loop(pages)


if __name__ == "__main__":
  main()



