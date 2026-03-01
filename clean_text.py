import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # 去除多余的空格
    # 注释掉去除非ASCII字符的行，因为中文就是非ASCII
    # text = re.sub(r'[^\x00-\x7F]+', '', text)  # 去除非ASCII字符
    return text

# 修改文件名为您实际的文件名
with open('50000字诗文_原文.txt', 'r', encoding='utf-8') as file:
    text = file.read()

cleaned_text = clean_text(text)

with open('cleaned_document.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

print("清洗完成！生成文件：cleaned_document.txt")
