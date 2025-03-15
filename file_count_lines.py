a= "/content/programm1.tex"
with open(a, 'r', encoding='utf-8') as file:
    line_count = len(file.readlines())
print("Number of lines:", line_count)
