#The Problem
# You're building a writing app and need to show users statistics about their text - word count,
# longest words, most used words, etc.
# text  = input("Enter your string")

result = {
  "total_chars": None,
  "chars_no_spaces": None,
  "word_count": None,
  "sentence_count": None,
  "longest_word": None,
  "shortest_word": None,
  "avg_word_length": None,
  "most_common": [],
  "unique_words": [],
  "punctuation_count": {}
}

text = "The quick brown fox jumps over the lazy dog. The dog was really lazy!"

#handle edge case
if not text:
    print("")
    
#count charaters
total_char = len(text)
result["total_chars"] = total_char

#count without spaces
chars_no_spaces = len(text.replace(" " ,""))
result["chars_no_spaces"] = chars_no_spaces

#punctuation_Count 
punctuation_count = 0
for char in text:
    if char in "!.?":
        punctuation_count+=1
result["punctuation_count"] = punctuation_count

#remove punctaution 
cleaned_text = text.replace("!","").replace("?" ,"").replace(".","")


#words count 
count_word = cleaned_text.split()
words = len(count_word)
result["word_count"] = words

#find longest and shortest count 
longest = count_word[0]
shortest = count_word[0]
for word in count_word:
    if len(word) > len(longest):
        longest = word
    elif len(word) < len(shortest):
        shortest = word
        
result["longest_word"] = longest
result["shortest_word"] = shortest

#average word count 
avg_word_count =  sum(len(word) for word in count_word) // len(count_word)

result["avg_word_length"] = avg_word_count



#checking word frequecny 
word_count = {}
for word in count_word:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word] = 1

 # Convert dictionary to list of tuples and sort # Convert dictionary to list of tuples and sort
most_common = []
unique_word = []
for word,count in word_count.items():
    if count == 1:
        unique_word.append(word)
    elif count >= 2:
        most_common.append((word,count))
sorted(most_common) 
result["most_common"] = most_common
result["unique_words"] = unique_word

  # Count sentence-ending punctuation
sentence_Count = 0
for char in text:
    if char in "!.?":
        sentence_Count+=1
    
result["sentence_count"] = sentence_Count
print(result)
    
    


