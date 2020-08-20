import xml.etree.ElementTree as ET

def func_xml(files):
	parser = ET.XMLParser(encoding="utf-8")
	tree = ET.parse(files, parser)
	root = tree.getroot()
	
	items_list = root.findall("channel/item/description") # с помощью xpath достаем данные из 'description', получаем список
	
	list_len_more_six = []
	for title in items_list: # итерируемся по списку
		title = (title.text) # с помощью text читаем в нормальный формат, получаем данные в виде строк
		news_split = title.split() # сплитим строки в список
		for items in news_split: # итерируемся по списку
			if len(items) > 6: # проверяем слова на кол символов больше 6
				list_len_more_six.append(items) # если слово больше 6 символов, добавляем его в пустой список
	
	dict_len_more_six = {}
	for items2 in list_len_more_six: # итерируемся по списку
		dict_len_more_six.setdefault(items2, 0) # добавляем в пустой словарь слово как ключ словаря, значение ключа делаем 0
		dict_len_more_six[items2] += 1 # при каждой итерации, если слово повторяется, то увеличиваем значение ключа на один
	
	count = 0
	print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
	# итерируемся по словарю, при помощи lambda сортируем словарь по значению
	for items3 in sorted(dict_len_more_six.items(), key=lambda para: para[1], reverse=True):
		# запускаем цикл, чтобы вывести на печать первые 10 слов
		while count < 10:
			count += 1
			print(items3[0])
			break

func_xml("newsafr.xml")
