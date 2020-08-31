import collections

def filter_words(words):
	list_len_more_six = []
	for items in words: # итерируемся по списку
		if len(items) > 6: # проверяем слова на кол символов больше 6
			list_len_more_six.append(items) # если слово больше 6 символов, добавляем его в пустой список
	return list_len_more_six

def count_words(words):
	items2 = collections.Counter(words).most_common(10)
	
	print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
	for items3 in items2:
		print(items3[0])
