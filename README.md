## Text-to-Speech from Docx

This Python script extracts text from a Microsoft Word document (.docx) and converts it into an audio file (MP3) using Google Text-to-Speech (gTTS).

**Features:**

* Reads text content from a .docx file.
* Converts the extracted text into an audio file using gTTS (English language supported).
* Provides a user-friendly interface for specifying the input .docx file path.
* Handles errors if the input file doesn't exist.

**Installation:**

1. Make sure you have Python 3 installed.

2. Install the required libraries:

```bash
pip install docx gtts
```

**Usage:**

1. Clone or download this repository.
2. Open a terminal or command prompt and navigate to the directory containing the script (docx-to-audio.py).   
3. Run the script:

```bash
python text_to_speech_docx.py
```

4. You will be prompted to enter the path of your .docx file.
5. If the file exists, the script will extract the text and convert it to an audio file named output.mp3.

```bash
Enter the path of your .docx file: path/to/your/file.docx
Creating audio file `output.mp3`, please wait...
Success! Audio saved to output.mp3
```