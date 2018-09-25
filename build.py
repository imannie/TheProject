#Define the main function

    
#Python Script Site Generator
top_template = open("templates/top.html").read()
bottom_template = open("templates/bottom.html").read()

#Combine HTML index file
index_body = open("content/mid_index.html").read()
combine_index = top_template + index_body + bottom_template
open("docs/index.html", "w+").write(combine_index)

#Combine HTML about file
about_body = open("content/mid_about.html").read()
combine_about = top_template + about_body + bottom_template
open("docs/about.html", "w+").write(combine_about)

#Combine HTML work file
work_body = open("content/mid_work.html").read()
combine_work = top_template + work_body + bottom_template
open("docs/work.html", "w+").write(combine_work)

#Combine HTML contact file
contact_body = open("content/mid_contact.html").read()
combine_contact = top_template + contact_body + bottom_template
open("docs/contact.html", "w+").write(combine_contact)


#Create a list of my homework files
pages_list = [
              {
              'filename': 'content/mid_index.html',
              'output': 'docs/index.html',
              'title': 'Home page',
              },
              {
              'filename': 'content/mid_about.html',
              'output': 'docs/about.html',
              'title': 'About me',
              },
              {
              'filename': 'content/mid_work.html',
              'output': 'docs/work.html',
              'title': 'my works',
              },
              {
              'filename': 'content/mid_contact.html',
              'output': 'docs/contact.html',
              'title': 'Contact Me',
              },
]

for datum in pages_list:
    print('File name:', datum['filename'])
    print('Output file is', datum['output'])
    print('Title:', datum['title'])

print('--------------------')


#Combine top.html and bottom.html onto one more templates file called base.html
top_template = open("templates/top.html").read()
bottom_template = open("templates/bottom.html").read()
base = top_template + bottom_template
open("templates/base.html", "w+").write(base)


