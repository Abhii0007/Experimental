def speech_synthesizer(self):
    import pyttsx3
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 190)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say('hello, i am artificial intelligence')
    engine.runAndWait()

