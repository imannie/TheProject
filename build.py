
#Python Script Site Generator
    top_template = open("templates/top.html").read()
    bottom_template = open("templates/bottom.html").read()

#Combine HTML index file
<<<<<<< HEAD
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






