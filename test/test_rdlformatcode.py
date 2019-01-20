from .unittest_utils import RDLSourceTestCase

class TestRDLFormatCode(RDLSourceTestCase):
    
    def test_tags(self):
        root = self.compile(
            ["rdl_testcases/rdlformatcode.rdl"],
            "rdlformatcode"
        )
        
        html = []
        for i in range(0,18):
            reg = root.find_by_path("rdlformatcode.r%d" % i)
            html.append(reg.get_html_desc())
        
        def p(s):
            return "<p>%s</p>" % s
        
        self.assertEqual(html[0], "<p>asdf</p>")
        self.assertEqual(html[1], p("<b>asdf</b>"))
        self.assertEqual(html[2], p("<i>asdf</i>"))
        self.assertEqual(html[3], p("<u>asdf</u>"))
        self.assertEqual(html[4], p('<span style="color:red">asdf</span>'))
        self.assertEqual(html[5], p('<span style="font-size:12">asdf</span>'))
        self.assertEqual(html[6], p('<a href="github.com">github.com</a>'))
        self.assertEqual(html[7], p('<a href="github.com">asdf</a>'))
        self.assertEqual(html[8], p('<a href="mailto:asdf@example.com">asdf@example.com</a>'))
        self.assertEqual(html[9], p('<img src="image.png">'))
        self.assertEqual(html[10], p('<code>asdf</code>'))
        self.assertEqual(html[11], p('"asdf"'))
        self.assertEqual(html[12], p('<br>[]&amp;nbsp'))
        self.assertEqual(html[13], p("r13"))
        self.assertEqual(html[14], p("r14"))
        
        r15 = root.find_by_path("rdlformatcode.r15[1]")
        self.assertEqual(r15.get_html_desc(), p("<span class='rdlfc-index'>[1]</span>"))
        
        f = root.find_by_path("rdlformatcode.r15[2].f")
        self.assertEqual(f.get_html_desc(), p("<span class='rdlfc-index_parent'>[2]</span>"))
        
        self.assertEqual(html[16], "")
        self.assertEqual(html[17], "")
