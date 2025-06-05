import re
text = "Python is amazing! It is versatile. Do you agree?"
class SentenceAnalyzer:
    def __init__(self, text):
        self.original_text = text

        # Split into sentences
        self.sentences = re.split(r'[.!?]', text)
        self.sentences = [s.strip() for s in self.sentences if s.strip()]

        # Clean each sentence
        self.cleaned_sentences = [re.sub(r'[^\w\s]', '', s.lower()) for s in self.sentences ]
analyzer = SentenceAnalyzer(text)
print(analyzer.sentences)
print(analyzer.cleaned_sentences)
