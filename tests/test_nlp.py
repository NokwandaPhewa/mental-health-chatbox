from chatbot.nlp_processor import NLPProcessor
print("Class exists!")
nlp = NLPProcessor()
print("Instance created!")
result = nlp.analyze_message("I feel sad")
print("Analysis worked:", result)
