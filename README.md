# API-Analizador de Textos Largos Para La Generación de Resúmenes

Análisis de textos Largos para la generación de un resumen

## Description
Como parte de los requisitos para optar por el título de Ingeniería en Sistemas y Computación, se requiere el desarrollo de un proyecto final cuya finalidad sea proveer una solución a una problemática identificada, aplicando los conocimientos obtenidos y utilizando herramientas innovadoras. En el caso de este proyecto, la intención es desarrollar un algoritmo que aplique machine learning mediante el procesamiento de lenguaje natural (NLP) para la generación de resúmenes de textos de larga longitud. Para ello se estarán desarrollando tres componentes. El primer componente, corresponde al desarrollo de un algoritmo simplificado que ejemplifica el flujo de procesos base de la generación de resúmenes mediante métodos extractivos. El segundo elemento corresponde a la creación de un API, auxiliándonos de modelos pre-entrenados con elementos complejos y detallados capaces de manejar una alta cantidad de textos. Por último, se implementará un aplicativo Web que consuma el API desarrollado.

## Getting Started

### Dependencies

* Transformer Library
* PyTorch
* NLTK (Natural Language Tool Kit) - Extractive Summarization
* EncoderDecoderModel (BERT Summarization Model)
* BertTokenizerFast (BERT Summarization Model)
* AutoTokenizer (BART Summarization Model)
* AutoModelForSeq2SeqLM (BART Summarization Model)

### Installing
* Installing Transformers
```
!pip install transformers
```
* Importing Transformers
```
import transformers
```
* Importing Pipelines
```
from transformers import pipeline
```
* Importing Tokenizers and AutoModel
```
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import AutoTokenizer, AutoModelWithLMHead
```
* Import Torch (PyTorch)
```
import torch
```
* Import NLTK
```
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
```


### Executing program

Open the *.py* algorithm with and import all modules.

## Version History

* 1.0
    * Initial Summarization Codes
    * See [commit change]() or See [release history]()
* 1.1
    * Initial Release and uploading base algorithm and summarizer modules
* 1.2
    * Uploading the *main.py* the uses both created modules.  

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgments
* Alami, N., Meknassi, M., & Rais, N. (2015). Automatic Texts Summarization: Current State of the Art. Journal of Asian Scientific Research, 1-15.
Arc, T. D. (31 de Mayo de 2021). Recuperado el 28 de Mayo de 2022, de https://www.smarthint.co/es/google-bert/#:~:text=BERT%20es%20un%20algoritmo%20de,contenidos%20de%20las%20p%C3%A1ginas%20web
* Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. Cornell University, 1-16. doi:10.48550/ARXIV.1810.04805
* Gholamrezazadeh, S., Salehi, M. A., & Gholamzadeh, B. (2009). A Comprehensive Survey on Text Summarization Systems. 2009 2nd International Conference on Computer Science and its Applications, (p. 6). Jeju, Korea (South).
* Gudivada, V. N. (2018). Natural Language Core Tasks and Applications. En C. R. Rao (Ed.), Handbook of Statistics (Vol. 38, págs. 403-428). Amsterdam: Elsevier. doi:https://doi.org/10.1016/bs.host.2018.07.010
* Ko, Y., & Seo, J. (2008). An effective sentence-extraction technique using contextual information and statistical approaches for text summarization. En Pattern Recognition Letters (págs. 1366-1371).
* Lewis, M., Liu, Y., Goyal, N., Ghazvininejad, M., Mohamed, A., Levy, O., . . . Zettlemoyer, L. (2019). BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension. Cornell University, 1-10.
* Salton, G. (1989). Automatic Text Processing: The Transformation, Analysis, and Retrieval of Information by Computer. Addison-Wesley Publishing Company.
* Watson, M. (1998). “Using leading text for news summaries:Evaluation results and implications for commercial summarization applications. 17th International Conference on Computational Linguistics and 36th Annual Meeting of ACL. 




