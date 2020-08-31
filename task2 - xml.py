import xml.etree.ElementTree as ET
from my_module import filter_words, count_words

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

items_list = root.findall("channel/item/description") # с помощью xpath достаем данные из 'description', получаем список

for title in items_list: # итерируемся по списку
	title = (title.text) # с помощью text читаем в нормальный формат, получаем данные в виде строк
	news_split = title.split() # сплитим строки в список
	
word_more_six = filter_words(news_split)
count_words(word_more_six)

