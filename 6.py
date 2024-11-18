import re
from collections import Counter
import string

def tokenize_sentences(text):
    sentence_endings = re.compile(r'(?<=[.!?])\s+')
    sentences = sentence_endings.split(text.strip())
    return sentences

def tokenize_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def summarize_text(text, num_sentences=2):
    sentences = tokenize_sentences(text)
    words = tokenize_words(text)
    filtered_words = [word for word in words if word not in string.punctuation]
    word_frequencies = Counter(filtered_words)
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / max_frequency
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = tokenize_words(sentence)
        sentence_score = 0
        for word in sentence_words:
            if word in word_frequencies:
                sentence_score += word_frequencies[word]
        sentence_scores[sentence] = sentence_score
    ranked_sentences = sorted(sentence_scores.items(), key=lambda item: item[1], reverse=True)
    summary_sentences = [item[0] for item in ranked_sentences[:num_sentences]]
    summary = ' '.join(summary_sentences)
    return summary

text = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

summary = summarize_text(text)

print("Oriģinālais teksts:")
print(text)
print("\nRezumējums:")
print(summary)
