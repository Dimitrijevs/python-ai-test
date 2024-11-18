from lingua import Language, LanguageDetectorBuilder

# Initialize the language detector with supported languages
detector = LanguageDetectorBuilder.from_languages(
    Language.LATVIAN, Language.ENGLISH, Language.RUSSIAN
).build()

# List of text examples
texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

# Detect languages
print("Detected Languages:")
for i, text in enumerate(texts, start=1):
    language = detector.detect_language_of(text)
    print(f"Text {i}: {language.name.lower()} ({language.name})")
