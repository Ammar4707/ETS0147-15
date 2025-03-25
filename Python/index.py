sentence = "Python is a powerful programming language."
word_index = sentence.index("powerful")
print(f"The word 'powerful' starts at index: {word_index}")



file_name = "report_2025.docx"
if file_name.startswith("report"):
    print("The file name starts with 'report'")

# Example demonstrating str.endswith()
if file_name.endswith(".docx"):
    print("The file is a Word document")
