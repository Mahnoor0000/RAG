from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

text = "This is a sample text that will be split into smaller chunks based on the specified chunk size and overlap. The RecursiveCharacterTextSplitter will help in dividing the text into manageable pieces for further processing or analysis."

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=["\n\n", "\n", " ", ""],
)
result = splitter.split_text(text)
print(len(result))
print(result)


