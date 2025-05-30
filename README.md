## PySpeech
You can create mp3 file with text and gTTS library (Google Translate's text-to-speech API)

<h4><p align="center"><img src="design/design-1.jpg" width="800"/></p></h4>
<h4><p align="center"><img src="design/design-2.jpg" width="800"/></p></h4>

```
What the program does? 

- Generate mp3 file with text
- Generate multiple mp3 files through .txt file
- Multilingual
- A terminal windows program
``` 

## Quick start 

<h4>The simplest method is to install the portable version using the .exe file, available at <a href="https://github.com/duc11021102/pyspeech/releases/download/v1.0/tts-audio.exe">this link</a>.
<br>
Or install with <b>python</b>:

### Requirements

* Python (pip v25 or newer, python v3.10 or newer)
* Python Libraries: `gTTS pygame pyinstaller`

### Setup 

- Install the dependencies following these steps : 

  - Star this repository
  - <>Code > Download ZIP > Open cmd/terminal in that location
  - Run this command : `pip install -r requirements.txt`
  - Run `tts-audio.py` or open `tts-audio.bat` after installation


- If you want to build and creat a .exe program:

  - Run this command : `pyinstaller --onefile --icon=icon.ico  tts-audio.py`
  - Your .exe file in your generated dist folder

### Setup with Docker

- Pull and run:

  - Run this command : `docker pull duc11021102/text-to-speech-audio`
  - Run this command : `docker run -it duc11021102/text-to-speech-audio`

### Command 
```/m``` - change mode (one .mp3 file or multiple .mp3 files)

```/c``` - check current language

```/s``` - enable/disable automatic audio playback

```/*lang*``` - change language, default language is Chinese (Traditional), check <a href="https://github.com/duc11021102/pyspeech/blob/main/langs.py" >this file<a/> to use

Example: ```/vi``` - change to Vietnamese

##  Plans for future
<ul>
  <li>Make add-on in Anki</li>
</ul>