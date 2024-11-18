from textblob import TextBlob
from deep_translator import GoogleTranslator

# Input text
sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

# Function to translate and analyze sentiment
def translate_and_analyze(sentences):
    results = []
    for sentence in sentences:
        # Translate to English using DeepTranslator
        translation = GoogleTranslator(source='auto', target='en').translate(sentence)
        # Perform sentiment analysis
        sentiment = TextBlob(translation).sentiment.polarity
        
        # Determine sentiment category
        if sentiment > 0.5:
            emotion = "pozitīvs"
        elif sentiment < 0:
            emotion = "negatīvs"
        else:
            emotion = "neitrāls"
        # Append results
        results.append((sentence, translation, emotion))
    return results

# Analyze sentences
analysis_results = translate_and_analyze(sentences)

# Display results
for original, translated, emotion in analysis_results:
    print(f"Original: {original}")
    print(f"Translated: {translated}")
    print(f"Emotion: {emotion}\n")
