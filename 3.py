import re

# Input texts
text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

# Function to preprocess and tokenize text
def tokenize(text):
    # Convert to lowercase and extract words using regex
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)  # Convert to a set for unique words

# Tokenize both texts
words1 = tokenize(text1)
words2 = tokenize(text2)

# Identify common words
common_words = words1 & words2  # Intersection of both sets
total_words = words1 | words2  # Union of both sets

# Calculate overlap percentage
overlap_percentage = (len(common_words) / len(total_words)) * 100

# Display results
print("Common Words:", common_words)
print(f"Overlap Percentage: {overlap_percentage:.2f}%")
