
<<<<<<< HEAD
#Python Script Site Generator
    top_template = open("templates/top.html").read()
    bottom_template = open("templates/bottom.html").read()

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



=======
  
def main():
  pages_list = [
              {
              'filename': 'content/mid_index.html',
              'output': 'docs/index.html',
              'title': 'Homie',
              'page': 'index_page',
              },
              {
              'filename': 'content/mid_about.html',
              'output': 'docs/about.html',
              'title': 'A little about me',
              'page': 'about_page',
              },
              {
              'filename': 'content/mid_work.html',
              'output': 'docs/work.html',
              'title': 'My works',
              'page': 'work_page',
              },
              {
              'filename': 'content/mid_contact.html',
              'output': 'docs/contact.html',
              'title': 'Contact Me',
              'page': 'contact_page',
              },
  ]

  top_template = open("templates/top.html").read()
  bottom_template = open("templates/bottom.html").read()
  base = top_template + "{{content}}" + bottom_template
  open("templates/base.html", "w+").write(base)

  def loop(pages_list):
    for datum in pages_list:
      filename = datum['filename']
      output = datum['output']
      title = datum['title']
      page = datum['page']
      template = open("templates/base.html").read()
      index_content = open(datum['filename']).read()
      index_page = template.replace("{{content}}", index_content).replace("{{title}}", "Annie Project")
      open(datum['output'], "w+").write(index_page)
  loop(pages_list)


if __name__ == "__main__":
  main()


