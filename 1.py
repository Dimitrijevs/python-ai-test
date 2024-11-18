from collections import Counter
import re

# Input text
text = """Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."""

# Convert text to lowercase to ignore case
text = text.lower()

# Extract words using regular expressions
# Matches words composed of alphabetic characters and allows special Latvian characters
words = re.findall(r'\b\w+\b', text)

# Count the frequency of each word
word_frequencies = Counter(words)

# Display the word frequencies
print("Word Frequency Analysis:")
for word, count in word_frequencies.items():
    print(f"{word}: {count}")
