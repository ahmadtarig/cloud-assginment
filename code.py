file = open('paragraphs.txt', 'r')  # Read a file
data = file.read()  # Save a file content in variable "data"

data = data.split()  # Convert data to list of words

print(data[:50])
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

# Join data in string
data = " ".join(data)

file.close()  # close a file
