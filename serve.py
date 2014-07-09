"""
Script to index the talks in this repository and create an index.html file.
"""
import os
import glob
import re

root = "./"
directories = sorted([name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name))], reverse=True)
#talks = [name for name in directories if ]


index = open('index.html', 'w')

index.write("""<head>
                <title>VK: Talks</title>
                <link rel="icon" href="./favicon.ico" type="image/x-icon" />
               </head>
            """)
index.write("<body>")
index.write("<h1>Vincent Knight: Talks</h1>")
index.write("<ul>")
for dir in directories:
    if dir not in ['.git', 'reveal.js']:
        talk = glob.glob(root + dir + "/" + dir[:10] + '*')[0]
        date = talk[len(root+dir) + 1: len(root + dir) + 11]
        title = talk[len(root+dir)+11:].replace("-", " ")
        index.write("<li><a href=%s>%s: %s</a></li>" % (talk, date, title))
index.write("</ul>")
index.write("</body>")
index.close()
