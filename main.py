import xml.etree.ElementTree as ET
# mytree = ET.parse('Samplexml100.xml')
# myroot = mytree.getroot()
# print(myroot)
#######################################
# data = '''<?xml version="1.0" encoding="UTF-8" ?>
# <root>
#   <feeds>
#     <id>2140</id>
#     <title>gj</title>
#     <description>ghj</description>
#     <location>Hermannplatz 5-6, 10967 Berlin, Germany</location>
#     <lng>0</lng>
#     <lat>0</lat>
#     <userId>4051</userId>
#     <name>manoj</name>
#     <isdeleted>false</isdeleted>
#     <profilePicture>Images/9b291404-bc2e-4806-88c5-08d29e65a5ad.png</profilePicture>
#     <videoUrl/>
#     <images/>
#     <mediatype>0</mediatype>
#     <imagePaths/>
#     <feedsComment/>
#     <commentCount>0</commentCount>
#     <multiMedia>
#       <id>3240</id>
#       <name></name>
#       <description/>
#       <url>http://www.youtube.com/embed/mPhboJR0Llc</url>
#       <mediatype>2</mediatype>
#       <likeCount>0</likeCount>
#       <place/>
#       <createAt>0001-01-01T00:00:00</createAt>
#     </multiMedia>
#     <likeDislike>
#       <likes>0</likes>
#       <dislikes>0</dislikes>
#       <userAction>2</userAction>
#     </likeDislike>
#     <createdAt>2020-01-02T13:32:16.7480006</createdAt>
#     <code>0</code>
#     <msg/>
#   </feeds>
# </root>'''
# myroot = ET.fromstring(data)
# print(myroot.tag)

# mytree = ET.parse('Samplexml100.xml')
# myroot = mytree.getroot()
# print(myroot[2][1].tag)

# mytree = ET.parse('Samplexml100.xml')
# myroot = mytree.getroot()
# print(myroot[0].attrib)
#
# for x in myroot[0]:
#     print(x.tag,'-',x.text)
########################################
# mytree = ET.parse('Samplexml100.xml')
# myroot = mytree.getroot()
# print(myroot[0].attrib)
#
# for x in myroot.findall('feeds'):
#     item=x.find('id').text
#     price=x.find('description').text
#     print(item,price)
##########################

# mytree = ET.parse('Samplexml100.xml')
# myroot = mytree.getroot()
# print(myroot[0].attrib)
#
# for x in myroot.iter('description'):
#     a = str(x.text) + 'description has been added'
#     x.text = str(a)
#     x.set('updated','yes')
# mytree.write('new2.xml')
#################################################
# mytree = ET.parse('Samplexml100.xml')
# myroot = mytree.getroot()
# ET.SubElement(myroot[0],'speciality')
# for x in myroot.iter('speciality'):
#     x.text=str('vaibhav')
# mytree.write('new3.xml')
##############################################
# mytree = ET.parse('Samplexml100.xml')
# myroot = mytree.getroot()
# #myroot[0][0].attrib.pop('id')
# myroot[0].remove(myroot[0][0])
# mytree.write('new4.xml')
######################################
1212127879


