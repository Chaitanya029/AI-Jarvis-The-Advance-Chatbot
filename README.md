# AI-Jarvis-The-Advance-Chatbot
AI Jarvis is an open-source AI chatbot developed in Python with the main inspiration taken from the film ‘Ironman’ and its iconic assistant Jarvis and powered by Google Open-AI. This project makes the future touch your hand by providing an advanced version of the AI assistant which can listen to voice commands, even claps and keyboard presses.

**Inspired by Ironman's Jarvis, built with Python**

![ab3c01e6-a011-4287-afb0-f7c2dbf350cc (1)](https://github.com/user-attachments/assets/011db23b-bbdd-4007-b469-8a94665eab7c)

AI Jarvis is a cutting-edge AI chatbot that brings the futuristic experience of having a personal assistant to your fingertips. This project utilizes the power of Python, Google Open-AI, and various libraries to create a highly advanced and interactive AI assistant.

### Features
Voice and Clap Control
Listen to your voice commands and respond accordingly Activate AI Jarvis with a simple clap, no need to press any buttons

### WhatsApp Integration
Open WhatsApp and send text or files with just a voice command Send messages to your loved ones or share files with ease

### Language Translation
Translate languages in real-time, supporting over 11 languages including Hindi, English, Spanish, and more Communicate with people from diverse linguistic backgrounds effortlessly

### Customizable Voice Assistant
Choose from male or female voice assistants to suit your preference Get responses in a voice that's tailored to your liking

## Setup Procedures
For getting JARVIS up and running, the instructions are given below :

![2106 i201 007 F m004 c9 call center technical support isometric](https://github.com/user-attachments/assets/dedd854d-aa11-4948-9ba2-9e2b3edd240f)

### Environment setup
<ul>
  <li> <h4> You need to have Python 3.7 or later versions top run Jarvis. Jarvis is initially developed in Python 3.8.9, so getting the same version will be nice to avoid any other issues but 3.7 or later is also okay</h4> <b>Please note : Make sure to download Python 64 bit only ! Some modules are compatible only with 64 bit version. Also add Python to your system PATH.</b> <br><br> Download your python version from https://www.python.org/ <br> For getting Python 3.8.9, just click this link and download python for your os - https://www.python.org/downloads/release/python-389/ <br> Python 3.8.9 download for windows - https://www.python.org/ftp/python/3.8.9/python-3.8.9-amd64.exe <br></li>
  
  <li> <h4> After installing python correctly, make sure you have pip installed on your machine. Open command prompt or powershelll and type <i>pip</i> or <i>pip3</i> if something shows up, it's fine but if it says "It is not recognised as an internal or external command", just google it on how to install pip.<br><br>How to fix pip - https://www.youtube.com/resultssearch_query=how+to+fix+pip+is+not+recognized+as+an+internal+or+external+command</h4></li>
  
  <li><h4>Finally, once you install Python 64-bit version and pip, we can go on with installing the key dependencies. <br></h4></li>
</ul>

### Installing the required modules

<ul>
  <li><h4> First, navigate to this cloned repository and open cmd and then type : </h4></li>
</ul>

```
pip install -r requirements.txt
```
<ul>
  <li>Most of the times, you may run into an error saying <b>'no module named pyaudio'</b>. If there is any error on installing SpeechRecognition, do check out this website. Please download the ".whl" file of pyaudio of your python version. Link to website - https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio . After downloading that, pip install that .whl file. For Eg:</li>
  </ul>
  
 ```
 pip install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
 ```
 <ul>
  <li>The above wheel is suitable for Python 3.8 version. amd64 means 64 bit and win32 means 32-bit. First pip install the wheel and then again run pip install -r requirements.txt . After all these procedures, we are ready to start testing out JARVIS. <br></li>
  </ul>

### Getting the models for our Speech Engine

<ul>
  <li><h4>Now, the next step is to download the models for our Vosk speech Engine. Go to this website to download the model of your choice - https://alphacephei.com/vosk/models</h4></li>
  <li>There are models available for several accents of English and I am currently using the Indian Model. If you are in the USA, you could download the usa-english model. The model is not uploaded on Git Hub as it will take up a large space.<br></li>
  <li>Once you have downloaded the Vosk speech engine model, then extract all the files inside the downloaded folder and copy the files inside the <b>'vosk_speech_engine/model'</b> folder. Make sure to place this in the model folder inside vosk_speech_engine.<br></li>
  <li>Once you have placed that, we can successfully run our JARVIS program<br><br></li>
  </ul>

## Running the Python script

Now we can run our Python script. Just navigate to the cloned directory open cmd and then type :
```python
python jarvis.py
```
This will initialize the Python program. If you run into any problems during the installation of any modules, feel free to open an [issue](https://github.com/JoelShine/JARVIS-AI-ASSISTANT/issues). Thanks for supporting this project and happy coding !!


## Technologies used

<ul> <li><b>Libraries</b>: <ul> <li><b>json</b> for data manipulation</li> <li><b>torch</b> for machine learning capabilities</li> <li><b>numpy</b> for numerical computations</li> <li><b>random</b> for generating random responses</li> <li><b>pyaudio</b> for audio processing</li> <li><b>struct</b> for data structuring</li> <li><b>math</b> for mathematical operations</li> <li><b>os</b> for operating system interactions</li> <li><b>keyboard</b> for keyboard control</li> <li><b>pyautogui</b> for GUI automation</li> <li><b>web-browser</b> for web interactions</li> </ul> </li> </ul>
## How it Works
AI Jarvis uses Google Open-AI to process and transmit data, enabling it to understand and respond to your voice commands. The project's advanced natural language processing (NLP) capabilities allow it to comprehend complex requests and provide accurate responses.

## Getting Started
To run AI Jarvis, ensure you have Python 3.8 installed on your system. Clone this repository and install the required libraries using pip install -r requirements.txt. Then, simply run the main.py file to activate AI Jarvis.

## Contributing
I welcome all contributions to AI Jarvis! If you want to improve or add features to this project, please fork the repository and submit a pull request.

## License
AI Jarvis is licensed under the #MIT License. See LICENSE for details.

## Acknowledgments
I want to thank the developers of the libraries used in this project, as well as the Google Open-AI team for providing the foundation for AI Jarvis's advanced capabilities.
