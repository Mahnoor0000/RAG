# USED FOR SPLITTING CODE AND MARKDOWN WITH SPECIAL SEPARATORS

from langchain_classic.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return "self.name"
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
)

result = splitter.split_text(text)
print(len(result))
print(result[0])