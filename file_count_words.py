a= "/content/programm1.tex" 
with open(a, 'r', encoding='utf-8') as file:
    content = file.read()
    word_count = len(content.split())
print("Number of words:", word_count)
