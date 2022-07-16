# -*- coding: utf-8 -*-
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, BertTokenizerFast, EncoderDecoderModel

max_tokens = 6000

def Settings_ESP():
	"""
	Metodo para instancias las configuraciones del idioma español.
	Utiliza el algoritmos de BERT Fined Tuned Summarization.
		
	Inputs:
		:N/A
	Returns:
		:tokenizer: Herramienta para tokenizar el texto.
		:model: modelo de NLP
		:device: configuraciones del dispositivo
	"""
	device = 'cuda' if torch.cuda.is_available() else 'cpu'
	ckpt = 'mrm8488/bert2bert_shared-spanish-finetuned-summarization'
	tokenizer = BertTokenizerFast.from_pretrained(ckpt,model_max_length=max_tokens)
	model = EncoderDecoderModel.from_pretrained(ckpt).to(device)
	return tokenizer,model,device

def Settings_ENG():
	"""
	Metodo para instancias las configuraciones del idioma inglés.
	Utiliza el algoritmos de BERT CNN Summarization.
		
	Inputs:
		:N/A
	Returns:
		:tokenizer: Herramienta para tokenizar el texto.
		:model: modelo de NLP
		:device: configuraciones del dispositivo
	"""
	tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6",model_max_length=max_tokens)
	model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
	device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
	model = model.to(device)
	return tokenizer,model,device

def generate_sentences(text):
	"""
	Metodo para dividir el texto por oraciones.

	Inputs:
		:text: Texto original

	Returns:
		:sentences: Lista de oraciones.
	"""
	text = text.replace('.', '.<eos>')
	text = text.replace('?', '?<eos>')
	text = text.replace('!', '!<eos>')
	sentences = text.split('<eos>')
	return sentences


def chunker(max_chunk,sentences):
	"""
	Metodo Fragmentador de textos. Toma textos largos y los convierte en pedazos mas asumibles para el modelo.

	Inputs:
		:max_chunk: Maximo numero de palabras por fragmento.
		:sentences: Lista de oraciones.

	Returns:
		:chunks: Lista de fragmentos.
	"""
	current_chunk = 0 
	chunks = []
	for sentence in sentences:
		if len(chunks) == current_chunk + 1: 
			if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
				chunks[current_chunk].extend(sentence.split(' '))
			else:
				current_chunk += 1
				chunks.append(sentence.split(' '))
		else:
			#print(current_chunk)
			chunks.append(sentence.split(' '))
	for chunk_id in range(len(chunks)):
		chunks[chunk_id] = ' '.join(chunks[chunk_id])
	return chunks

def generate_summary(text,tokenizer,model,device,max_length,min_length):
	"""
	Método para generar los resúmenes de los fragmentos.

	Inputs:
		:text: Texto que se desea resumir.
		:tokenizer: Tokenizador para el texto.
		:model: Modelo NLP
		:device: Condifguraciones de dispostivo.
		:max_length: Longitud máxima del resúmen.
		:min_length: Longitud mínima del resúmen.

	Returns:
		:summary: Texto resumido según los parámetros.
	"""
	inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
	input_ids = inputs.input_ids.to(device)
	attention_mask = inputs.attention_mask.to(device)
	output = model.generate(input_ids, attention_mask=attention_mask,min_length=min_length,max_length=max_length)
	return tokenizer.decode(output[0], skip_special_tokens=True)

def summarize(lang,text,max_length,min_length):
	"""
	Método que unifica todas las configuraciones, pre-procesamiento y la generación del resúmen.

	Inputs:
		:lang: Idioma del texto.
		:text: Texto que se desea resumir.
		:max_length: Longitud máxima del resumen.
		:min_length: Longitud mínima del resumen.

	Returns:
		:summary: Texto resumido según los parámetros.
	"""
	max_chunks = max_tokens - 150
	if lang == "ESP":
		tokenizer,model,device = Settings_ESP()
	else:
		tokenizer,model,device = Settings_ENG()
	sentences = generate_sentences(text)
	#chunks = chunker(max_chunks,sentences)
	#max_len = max_length/len(chunks)
	#min_len = min_length/len(chunks)
	#summaries = []
	#for chunk in chunks:
		#summaries.append(generate_summary(chunk,tokenizer,model,device,max_len,min_len))
	#result = ' '.join([summary for summary in summaries])
	result = generate_summary(text,tokenizer,model,device,max_length,min_length)
	return result