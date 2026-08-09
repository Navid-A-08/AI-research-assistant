from crewai import Task  # pyright: ignore[reportMissingImports]
from agents import document_reader, retriever, summarizer

ingest_task = Task(
    description="Read the PDF at {file_path}, extract its text, and store it in the vector database under paper_id={paper_id}.",
    expected_output="Confirmation that the paper's text was chunked and stored successfully.",
    agent=document_reader
)

retrieve_task = Task(
    description="Given the user's question: '{question}', retrieve the most relevant passages from the vector database.",
    expected_output="The most relevant text passages related to the question.",
    agent=retriever,
    context=[ingest_task]
)

summarize_task = Task(
    description="Using the retrieved passages, answer the user's question: '{question}'",
    expected_output="A clear, accurate answer grounded in the retrieved passages.",
    agent=summarizer,
    context=[retrieve_task]
)