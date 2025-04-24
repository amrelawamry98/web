import unittest

from textnode import *

def test_text(self):
      node = TextNode("This is a text node", TextType.TEXT)
      html_node = text_node_to_html_node(node)
      code_node = TextNode("code",TextType.CODE)
      code_html_node = text_node_to_html_node(code_node)
      bold_node = TextNode("BOLD TEXT", TextType.BOLD)
      bold_html_node = text_node_to_html_node(bold_node)
      link_node = TextNode("click me" , TextType.LINK,"https://google.com")
      link_html_node = text_node_to_html_node(link_node)
      image_node = TextNode("this is an image",TextType.IMAGE, "image.com")
      image_html_node = text_node_to_html_node(image_node) 
      self.assertEqual(html_node.tag, None)
      self.assertEqual(html_node.value, "This is a text node")
      self.assertEqual(code_html_node.tag , "code")
      self.assertEqual(code_html_node.value, "code")
      self.assertEqual(bold_html_node.tag , "b")
      self.assertEqual(bold_html_node.value , "BOLD TEXT")
      self.assertEqual(link_html_node.tag , "a")
      self.assertEqual(image_html_node.tag,"img")
      self.assertEqual(image_html_node.value , "")
      self.assertEqual(image_html_node.props["src"] , "image.com")
      self.assertEqual(image_html_node.props["alt"] , "this is an image")
      self.assertEqual(link_html_node.value , "click me")
      self.assertEqual(link_html_node.props["href"] , "https://google.com")

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()

