from __future__ import unicode_literals
import os

import hoep as h


class MyRenderer(h.Hoep):
    def __init__(self):
        super(MyRenderer, self).__init__()
        self.index = []
        self.current_block = []
        self.reset()

    def reset(self):
        self.last_header = None
        self.path = None
        if self.current_block:
            self.index.append(self.current_block)
        self.current_block = []

    def set_path(self, path):
        self.path = path

    def header(self, text, level):
        self.last_header = text
        return text or "header"

    def link(self, link, mixed_title, content):
        self.current_block.append((self.path, self.last_header, link,
                                   mixed_title, content))
        return link or "link"

    def emphasis(self, text):
        return text or "em"


md = MyRenderer()

os.chdir("..")
top = "."
for root, dirs, files in os.walk(top):
    for name in files:
        _, ext = os.path.splitext(name)
        if ext == ".md":
            fn = os.path.join(root, name)
            md.set_path(fn)
            with open(fn, "r") as f:
                text = f.read()
                text = text.decode('utf-8')
                html = md.render(text)
    md.reset()

print "<!--- "
print "      Machine generated - DO NOT EDIT!"
print "use:  python ./flow/extract.py > toc.md"
print "-->"

for block in md.index:
    path, header, link, title, content = block[0]
    print "##", path
    last_header = None
    for path, header, link, title, content in block:
        if header != last_header:
            print "###", header
        last_header = header
        if title:
            o = u'[%s](%s "%s")' % (content, link, title)
        else:
            o = u'[%s](%s)' % (content, link)
        print o.encode('utf-8')

