from langchain_classic.text_splitter import CharacterTextSplitter


text = "This is a sample text that will be split into smaller chunks based on the specified chunk size and overlap. The CharacterTextSplitter will help in dividing the text into manageable pieces for further processing or analysis."



splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=" ",
)

result = splitter.split_text(text)
print(result)