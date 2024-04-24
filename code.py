file = open('paragraphs.txt', 'r')  # Read a file
data = file.read()  # Save a file content in variable "data"

data = data.split()  # Convert data to list of words

# Define a list of stop words
stopWords = [
    "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "he", "in", "is", "it", "its", "of", "on", "that", "the",
    "to", "was", "were", "will", "with"
]

# Remove a stop words from data list but this code does not work
# for stopWord in stopWords:
#     while stopWord in data:
#         data.remove(stopWord)
# so I am using this Chat-gpt code

# Remove stop words from data using list comprehension
data = [word for word in data if word.lower() not in stopWords]

# join data in text
text = " ".join(data)

print(text)


# Create frequency dict
frequency = {}

# Same error I don't know why does not work logically code is true
# for word in data:
#     print(word)
#     if word in frequency["words"]:
#         frequency["frequency"][frequency["words"].index(word)] += 1
#     else:
#         frequency["words"].append(word)
#         frequency["frequency"].append(1)

# So I am using chat-gpt code

# calc frequency
for word in data:
    frequency[word] = frequency.get(word, 0) + 1

# print a dict
for word, frequencyCount in frequency.items():
    print(f"word: {word} , frequency: {frequencyCount}")

file.close()  # close a file
