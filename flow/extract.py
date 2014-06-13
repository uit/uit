from __future__ import unicode_literals
import os

import hoep as h


class MyRenderer(h.Hoep):
    #def preprocess(self, markdown):
    #    print "Preprocess:", markdown

    def doc_header(self):
        #print "Doc Header"
        return ""

    def doc_footer(self):
        #print "Doc Footer"
        return ""

    def postprocess(self, html):
        #print "Postprocess", html
        return html

    def block_code(self, text, language):
        #print "Block code:", text, language
        return text

    def block_html(self, text):
        #print "Block html:", text
        return text

    def block_quote(self, text):
        #print "Block quote:", text
        return text

    def footnotes(self, text):
        #print "Footnotes:", text
        return text

    def footnote_def(self, text, number):
        #print "Footnote def:", text, number
        return text

    def header(self, text, level):
        print "Header:", text, level
        return text

    def hrule(self):
        #print "Hrule"
        return "---"

    def list(self, text, ordered):
        #print "List:", text, ordered
        return text

    def list_item(self, text, ordered):
        #print "List item:", text, ordered
        return text

    def paragraph(self, text):
        #print "Paragraph:", text
        return text

    def table(self, header, body):
        #print "Table:", header, body
        return header

    def table_row(self, text):
        #print "Table row:", text
        return text

    def table_cell(self, text, flags):
        #print "Table cell:", text, flags
        return text

    def autolink(self, link, is_email):
        print "autolink:", link, is_email
        return link

    def codespan(self, text):
        #print "codespan:", text
        return text

    def double_emphasis(self, text):
        #print "double_emphasis:", text
        return text

    def emphasis(self, text):
        #print "emphasis:", text
        return text

    def footnote_ref(self, number):
        #print "footnot_ref:", number
        return number

    def highlight(self, text):
        #print "highlight:", text
        return text

    def image(self, link, mixed_title, alt):
        #print "image:", link, mixed_title, alt
        return link

    def line_break(self):
        #print "line_break"
        return

    def link(self, link, mixed_title, content):
        #print "link:", link, mixed_title, content
        if mixed_title:
            print '"%s"' % mixed_title,
        print content, '->', link
        return link

    def quote(self, text):
        #print "quote:", text
        return text

    def raw_html_tag(self, tag):
        #print "raw_html_tag:", tag
        return tag

    def strikethrough(self, text):
        #print "strikethrough:", text
        return text

    def superscript(self, text):
        #print "superscript:", text
        return text

    def triple_emphasis(self, text):
        #print "triple_emphasis:", text
        return text

    def underline(self, text):
        #print "underline:", text
        return text


md = MyRenderer()

os.chdir("..")
top = "."
for root, dirs, files in os.walk(top):
    for name in files:
        _, ext = os.path.splitext(name)
        if ext == ".md":
            fn = os.path.join(root, name)
            print "---------------------", fn, "-------------"
            with open(fn, "r") as f:
                text = f.read()
                text = text.decode('utf-8')
                html = md.render(text)
                print "---------------------", fn, "-------------"
        else:
            print "skipping"
