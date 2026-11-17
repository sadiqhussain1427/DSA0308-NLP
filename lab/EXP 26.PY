def dialog_act(sentence):
    sentence = sentence.lower()

    if sentence.startswith(("hi", "hello")):
        return "Greeting"
    elif sentence.startswith(("what", "where", "when", "why", "how")):
        return "Question"
    elif sentence.startswith(("please", "kindly")):
        return "Request"
    else:
        return "Statement"


sentences = [
    "Hello, how are you?",
    "What is your name?",
    "Please help me",
    "I am a student"
]

print("Dialog Act Recognition:")

for sentence in sentences:
    print(sentence, "->", dialog_act(sentence))
