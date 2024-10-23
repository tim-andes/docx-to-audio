from docx import Document
from gtts import gTTS
import os

def extract_text_from_docx(file_path):
    # Open the .docx file
    document = Document(file_path)

    # Extract the text
    text = ''
    for paragraph in document.paragraphs:
        text += paragraph.text + ' '

    return text.strip()

def convert_text_to_audio(text, output_file):
    # Convert the text to speech using gTTS
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

def main():
    file_path = input("Enter the path of your .docx file: ")
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    output_file = 'output.mp3'
    text = extract_text_from_docx(file_path)
    convert_text_to_audio(text, output_file)

    print(f"Audio saved to {output_file}")

if __name__ == "__main__":
    main()