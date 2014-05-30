from __future__ import unicode_literals
import os

import hoep as h


class MyRenderer(h.Hoep):
    def strikethrough(self, text):
        return self.replace

    #def preprocess(self, markdown):
    #    print "Preprocess:", markdown

    def doc_header(self):
        print "Doc Header"
        return ""

    def doc_footer(self):
        print "Doc Footer"
        return ""

    def postprocess(self, html):
        print "Postprocess", html
        return html

    def block_code(self, text, language):
        print "Block code:", text, language
        return text

    def block_html(self, text):
        print "Block html:", text
        return text

    def block_quote(self, text):
        print "Block quote:", text
        return text

    def footnotes(self, text):
        print "Footnotes:", text
        return text

    def footnote_def(self, text, number):
        print "Footnote def:", text, number
        return text

    def header(self, text, level):
        print "Header:", text, level
        return text

    def hrule(self):
        print "Hrule"
        return "---"

    def list(self, text, ordered):
        print "List:", text, ordered
        return text

    def list_item(self, text, ordered):
        print "List item:", text, ordered
        return text

    def paragraph(self, text):
        print "Paragraph:", text
        return text

    def table(self, header, body):
        print "Table:", header, body
        return header

    def table_row(self, text):
        print "Table row:", text
        return text

    def table_cell(self, text, flags):
        print "Table cell:", text, flags
        return text


md = MyRenderer()

os.chdir("..")
top = "."
for root, dirs, files in os.walk(top):
    for name in files:
        print "-------------", name, "----------------"
        _, ext = os.path.splitext(name)
        if ext == ".md":
            with open(name, "r") as f:
                text = f.read()
                print "TEXT -----------------------"
                text = text.decode('utf-8')
                print "----------------------------"
                html = md.render(text)
        else:
            print "skipping"
