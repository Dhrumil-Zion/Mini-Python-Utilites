from gtts import gTTS

file = open("mihir")
text_input = file.read()
language = "en"
ouput_audio = gTTS(text=text_input, lang=language, slow=False)
ouput_audio.save("mihir.mp3")
