from summarizer import Summarizer

model = Summarizer()


def get_summary(text=None, sentences=3):
    return model(text, num_sentences=sentences)
