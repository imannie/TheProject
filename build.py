#Python Script Site Generator
top_template = open("templates/top.html").read()
bottom_template = open("templates/bottom.html").read()

#Combine HTML index file
index_body = open("content/mid_index.html").read()
combine_index = top_template + index_body + bottom_template
open("index.html", "w+").write(combine_index)

#Combine HTML about file
about_body = open("content/mid_about.html").read()
combine_about = top_template + about_body + bottom_template
open("about.html", "w+").write(combine_about)

#Combine HTML work file
work_body = open("content/mid_work.html").read()
combine_work = top_template + work_body + bottom_template
open("worl.html", "w+").write(combine_work)

#Combine HTML contact file
contact_body = open("content/mid_contact.html").read()
combine_contact = top_template + contact_body + bottom_template
open("contact.html", "w+").write(combine_contact)

