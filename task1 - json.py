import json

def func_json(files):
	with open(files, encoding = "utf-8") as file:
		json_news = json.load(file) # читаем данные из файла и сохраняем их в переменную
	
	# добавляем данные из 'items' в переменную добираясь по цепочке по ключам, получаем список со словарями
	news_list = json_news['rss']['channel']['items']
	
	list_len_more_six = []
	for news in news_list: # итерируемся по списку, получаем словари
		news_split = (news['description'].split()) # из словарей по ключу 'description' получаем данные и сплитим их в список
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

func_json("newsafr.json")










