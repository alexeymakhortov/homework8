import json
from my_module import filter_words, count_words

with open("newsafr.json", encoding="utf-8") as file:
	json_news = json.load(file) # читаем данные из файла и сохраняем их в переменную
	news_list = json_news['rss']['channel']['items'] # добавляем данные из 'items' в переменную добираясь по цепочке по ключам, получаем список со словарями
	for news in news_list: # итерируемся по списку, получаем словари
		news_split = (news['description'].split()) # из словарей по ключу 'description' получаем данные и сплитим их в список

word_more_six = filter_words(news_split)
count_words(word_more_six)
