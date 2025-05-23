from xml.dom import minidom

root = minidom.Document()

xml = root.createElement("root")
root.appendChild(xml)

productChild = root.createElement("product")
productChild.setAttribute("name", "Python-To-Python")
xml.appendChild(productChild)

print(root)
xml_str = root.toprettyxml()
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="Python-To-Python"/>
# </root>

with open("ptp.xml", "w") as f:
    f.write(xml_str)