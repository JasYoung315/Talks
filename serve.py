#!/usr/bin/env python
"""
Script to index the talks in this repository and create an index.html file.
"""
import os
import glob
import re

root = "./"
directories = sorted([name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name))], reverse=True)
talk_formats = ['.pdf', '.html']


index = open('index.html', 'w')
index.write(open('head.html', 'r').read())
index.write(open('header.html', 'r').read())

index.write("""
            <body>
            <div class="page-content">
            <div class="wrap">
            <div class="home">
            <ul class='posts'>""")

for dir in directories:
    if dir not in ['.git', 'reveal.js']:
        talk = [f for f in glob.glob(root + dir + "/" + dir[:10] + '*') if  os.path.splitext(f)[1] in talk_formats][0]
        date = talk[len(root+dir) + 1: len(root + dir) + 11]
        title, extension =  os.path.splitext(talk[len(root+dir)+11:].replace("-", " "))
        index.write("""
                    <li>
                    <span class="post-date">%s [%s]</span>
                    <a class="post-link" href="%s">%s</a>
                    <p>
                    <a href="%s">(Source files)</a>
                    </p>
                    """ % (date, extension[1:], talk, title, 'https://github.com/drvinceknight/Talks/tree/gh-pages/' + dir ))
        if os.path.isfile(root + dir + "/screencast" ):
            index.write("""
                        <p>
                        <a href="%s">(Screencast)</a>
                        </p>
                        """ % open(root+dir+"/screencast",'r').read())
        index.write("""
                    </li>
                    """)
index.write("""
            </ul>
            </div>
            </div>
            </div>
            """)
index.write(open('footer.html', 'r').read())
index.write("</body>")
index.close()
