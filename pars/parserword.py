import docx

def readingTextDocuments(fileName):
    doc = docx.Document(fileName)

    completedText = []

    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)


    return  '/n'.join(completedText)



print(readingTextDocuments('парсинг.docx'))