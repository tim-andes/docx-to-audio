from docx import Document
from gtts import gTTS
import os

def extract_text_from_docx(file_path):
  """
  Extracts text content from a Microsoft Word document (.docx) file.

  Args:
      file_path (str): The path to the .docx file.

  Returns:
      str: The extracted text content from the document.
  """
  # Open the .docx file
  document = Document(file_path)

  # Extract the text
  text = ''
  for paragraph in document.paragraphs:
    text += paragraph.text + ' '

  return text.strip()

def convert_text_to_audio(text, output_file):
  """
  Converts text to speech and saves it as an MP3 audio file.

  Args:
      text (str): The text content to be converted to speech.
      output_file (str): The name of the output MP3 file.
  """
  # Convert the text to speech using gTTS
  tts = gTTS(text=text, lang='en')
  tts.save(output_file)

def main():
  """
  The main function that handles user interaction, file validation,
  text extraction, conversion to audio, and success message.
  """
  file_path = input("Enter the path of your .docx file: ")
  if not os.path.exists(file_path):
    print(f"The file {file_path} does not exist.")
    return

  print(f"Creating audio file `{output_file}`, please wait...")
  output_file = 'output.mp3'
  text = extract_text_from_docx(file_path)
  convert_text_to_audio(text, output_file)

  print(f"Success! Audio saved to {output_file}")

if __name__ == "__main__":
  main()