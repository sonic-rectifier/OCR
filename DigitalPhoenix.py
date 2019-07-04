import io
from tools import *

GET_INFO_FROM_FILE = True
EOL_ENUM = 3

listArray = []
coordinateArray = []


def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    image_context = vision.types.ImageContext(language_hints=["en-t-i0-handwrit"])

    print("getting info from Google")
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image, image_context=image_context)
    # save_file = open("payload.txt", "a")
    # save_file.write(str(str(response)))

    for page in response.full_text_annotation.pages:
        # qp(page)
        # save_file = open("payload.txt", "a+")
        # save_file.write(str(save_file))
        # print(page)
        # print("---------------------------------------------------------------------------------------------")
        for block in page.blocks:
            # print('\nBlock confidence: {}\n'.format(block.confidence))
            for paragraph in block.paragraphs:
                # print('Paragraph confidence: {}'.format(
                # paragraph.confidence))
                word_to_print = ""
                for word in paragraph.words:

                    # print(word)
                    # print(
                    # "----------------------------------------------------------------------------------------")
                    # save_file = open("payload.txt", "a+")
                    # save_file.write(str(word))

                    # transfer_object = json.loads(str(word))

                    # print (word)
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    qp(word_text)
                    word_to_print += word_text
                    # print(word.symbols)
                    # print(word_text)
                    # print('Word text: {} (confidence: {})'.format(
                    # word_text, word.confidence))

                    for symbol in word.symbols:
                        # print("bounding box = {}".format(symbol.bounding_box))
                        # print("Confidence = {}".format(symbol.confidence))
                        # print("Word = {}".format(symbol.text)
                        # addText(symbol.text)
                        # print(type(symbol.property.detected_break))

                        # print(temp)
                        # print(symbol.property.detected_break)
                        if symbol.property.detected_break.type == EOL_ENUM:
                            pass
                            # print("EOL Detected")
                        # print("detected_break: {}".format(symbol.property.detected_break))
                        # print("detected_break: {}".format(symbol.property.detected_break.type))
                        # print('confidence: {}'.format(symbol.confidence))
                        # print('text: {}'.format(symbol.text))
                        word_to_print += " "
                        coordinateArray.append(symbol.bounding_box.vertices)
                        listArray.append(symbol.text)
            qp(word_to_print)
            return listArray


def getCoordinates():
    return coordinateArray

# detect_document("handwriting.jpg")

