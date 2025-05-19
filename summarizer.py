from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 3)  # Summarize to 3 sentences

    print("\n=== Summary ===")
    for sentence in summary:
        print(sentence)

if __name__ == "__main__":
    input_text = input("Enter the text to summarize:\n")
    summarize_text(input_text)
