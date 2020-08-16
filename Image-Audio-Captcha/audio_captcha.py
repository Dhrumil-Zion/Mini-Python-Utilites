from captcha.audio import AudioCaptcha

audio = AudioCaptcha()
data = audio.generate('45645')
audio.write('1234', 'out.wav')
