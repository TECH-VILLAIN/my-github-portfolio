text = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."


class TextAnalyzer:
    def __init__(self, text):
        formattedtext = text.replace(',', '').replace('!', '').replace('.', '').replace('?', '')
        formattedtext = formattedtext.lower()
        self.FmtText = formattedtext

    def FreqAll(self):
        wordlist = self.FmtText.split()
        freqMap = {}
        for word in set(wordlist):
            freqMap[word] = wordlist.count(word)
        return (freqMap)


analyzer = TextAnalyzer(text)
print(analyzer.FreqAll())
analyzed = TextAnalyzer(text)
print('formatted text:analyzed.FmtText')
freqMap = analyzed.FreqAll()
print(freqMap)
word = "lorem".count("lorem")
frequency = analyzed.word
print(f"the word{word} appeared {frequency}times")
