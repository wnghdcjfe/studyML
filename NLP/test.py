from utils.util import removeBlank 
text_file = open("./desc.txt", "r", encoding="utf-8")
lines = text_file.read().split('.') 
lines = removeBlank(lines) 
print(lines)  