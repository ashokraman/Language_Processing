#from docx import Document
import docx2txt

def convertDocxToText(path):
#	document = Document(path)
#	return "\n".join([para.text for para in document.paragraphs])
	text = docx2txt.process(path)
	return text

