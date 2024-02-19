import string
def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

user_input=input("Enter your text : ")
clean_string = remove_punctuation(user_input)
lowercase_input = clean_string.lower()
words=lowercase_input.split()
dic={}
for i in range(len(words)):
    word=words[i]
    if word not in dic:
        dic[word]=[]
    dic[word].append(i)
print(dic)