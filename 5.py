import re

# Input: Raw text
raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# Function to clean and normalize text
def clean_and_normalize(text):
    # Remove mentions (e.g., @John)
    text = re.sub(r"@\w+", "", text)
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    # Remove special characters, emojis, and excessive punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Convert to lowercase
    text = text.lower()
    # Trim extra whitespace
    text = text.strip()
    return text

# Clean the raw text
cleaned_text = clean_and_normalize(raw_text)

# Output the cleaned and normalized text
print("Original Text:", raw_text)
print("Cleaned Text:", cleaned_text)
