from lxml import etree

xml_string = """
<bookstore>
<book category="fiction">
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <year>1925</year>
    <price>10.99</price>
</book>
<book category="non-fiction">
    <title>A Brief History of Time</title>
    <author>Stephen Hawking</author>
    <year>1988</year>
    <price>15.99</price>
</book>
</bookstore>
"""

root = etree.fromstring(xml_string)
print(f"Root element: {root.tag}")  # Root element: bookstore

for book in root.findall("book"):
    category = book.get("category")
    title = book.find("title").text
    author = book.find("author").text

    print(f"Book: {title} by {author} (Category: {category})")
# Root element: bookstore
# Book: The Great Gatsby by F. Scott Fitzgerald (Category: fiction
# Book: A Brief History of Time by Stephen Hawking (Category: non-fiction)
