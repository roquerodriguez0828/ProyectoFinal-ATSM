# -*- coding: utf-8 -*-

#importing libraries
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize


def create_frequency_table(text_string,language) -> dict:
	"""
	Metodo para crear la tabla de frecuencia
		
	Inputs:
		:text_string: String que contiene el texto
		:language: Idioma del texto
	Returns:
		:frequency_table: Diccionario con la tabla de frecuencia de las palabras.
	"""
	if language == 'ENG':
		f = open('english')
	else:
		f = open('spanish')
	stopwds = []
	for line in f:
		stopwds.append(line)
	f.close()
	#removing stop words
	stop_words = set(stopwds)
	words = word_tokenize(text_string)
	stem = PorterStemmer()
	frequency_table = dict()
	for wd in words:
		wd = stem.stem(wd)
		if wd in stop_words:
			continue
		if wd in frequency_table:
			frequency_table[wd] += 1
		else:
			frequency_table[wd] = 1
	return frequency_table

def calculate_sentence_scores(sentences, frequency_table) -> dict:
	"""
	Metodo calcular el puntaje de las oraciones, basado en la tabla de frecuencia
		
	Inputs:
		:sentences: Lista de oraciones del texto.
		:frequency_table: Diccionario que contiene la frequencia de las palabras. 
	Returns:
		:sentence_weight: Diccionario con el puntaje acumulado de cada oracion.
	"""   
	sentence_weight = dict()
	for sentence in sentences:
		sentence_wordcount = (len(word_tokenize(sentence)))
		sentence_wordcount_without_stop_words = 0
		for word_weight in frequency_table:
			if word_weight in sentence.lower():
				sentence_wordcount_without_stop_words += 1
				if sentence[:7] in sentence_weight:
					sentence_weight[sentence[:7]] += frequency_table[word_weight]
				else:
					sentence_weight[sentence[:7]] = frequency_table[word_weight]
		sentence_weight[sentence[:7]] = sentence_weight[sentence[:7]] / sentence_wordcount_without_stop_words
	return sentence_weight

def calculate_average_score(sentence_weight) -> int:
	"""
	Metodo para calcular el threshold minimo de seleccion de oraciones relevantes
		
	Inputs:
		:sentence_weight: Diccionario con el puntaje de cada oracion.
	Returns:
		:average_score: Threshold con el puntaje de referencia para las oraciones.
	"""
	#calculating the average score for the sentences
	sum_values = 0
	for entry in sentence_weight:
		sum_values += sentence_weight[entry]
	#getting sentence average value from source text
	average_score = (sum_values / len(sentence_weight))
	return average_score

def get_article_summary(sentences, sentence_weight, threshold):
	"""
	Metodo encargado de seleccionar las oraciones que exceden el threshold establecido.
		
	Inputs:
		:sentences: Lista de oraciones del texto.
		:sentence_weight: Diccionario con el puntaje de cada oracion.
		:threshold: Puntaje de referencia para las oraciones.
	Returns:
			:article_summary: Resumen generado de según el threshold.
		"""
	sentence_counter = 0
	article_summary = ''
	for sentence in sentences:
		if sentence[:7] in sentence_weight and sentence_weight[sentence[:7]] >= (threshold):
			article_summary += " " + sentence
			sentence_counter += 1
	return article_summary

def run_article_summary(article,language):
	"""
	Metodo general que unifica todos los metodos y genera el resumen.
		
	Inputs:
		:article: Texto que se desea resumir.
		:language: Idioma del texto.
	Returns:
		:article_summary: Resumen del texto.
	"""
	#creating a dictionary for the word frequency table
	frequency_table = create_frequency_table(article,language)

	#tokenizing the sentences
	sentences = sent_tokenize(article)

	#algorithm for scoring a sentence by its words
	sentence_scores = calculate_sentence_scores(sentences, frequency_table)

	#getting the threshold
	threshold = calculate_average_score(sentence_scores)

	#producing the summary
	article_summary = get_article_summary(sentences, sentence_scores, threshold)

	return article_summary
