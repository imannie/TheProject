
  
def main():
  pages_list = [
              {
              'filename': 'content/index.html',
              'output': 'docs/index.html',
              'title': 'Homie',
              'page': 'index_page',
              },
              {
              'filename': 'content/about.html',
              'output': 'docs/about.html',
              'title': 'A little about me',
              'page': 'about_page',
              },
              {
              'filename': 'content/work.html',
              'output': 'docs/work.html',
              'title': 'My works',
              'page': 'work_page',
              },
              {
              'filename': 'content/contact.html',
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


