import io


def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    image_context = vision.types.ImageContext(language_hints=["en-t-i0-handwrit"])

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image, image_context=image_context)

    for page in response.full_text_annotation.pages:
        #print(page)
        for block in page.blocks:
            #print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                #print('Paragraph confidence: {}'.format(
                 #   paragraph.confidence))
                word_to_print = ""
                for word in paragraph.words:
                    #print (word)
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    word_to_print += word_text
                    #print(word_text)
                   # print('Word text: {} (confidence: {})'.format(
                   #     word_text, word.confidence))

                    for symbol in word.symbols:
                        pass
                        #print('\tSymbol: {} (confidence: {})'.format(symbol.text, symbol.confidence))
                        #print('{}'.format(symbol.text))
                    word_to_print += " "
            print(word_to_print)

detect_document("docs\white1.jpg")
#detect_document("handwriting.jpg")

