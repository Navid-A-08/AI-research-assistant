from crewai import Agents
from tools.pdf_tools import read_pdf
from tools.vector_tools import chunk_and_store, retrieve_chunks

document_reader = Agent(
    role="Document Reader",
    goal="Extract and prepare text from research paper PDFs for downstream processing.",
    backstory="You specialize in parsing academic PDFs and preparing them for search and analysis.",
    tools=[read_pdf, chunk_and_store],
    verbose=True
)

retriever = Agent(
    role="Retriever",
    goal="Find the most relevant passages from stored papers to answer a given query.",
    backstory="You are an expert at searching a knowledge base and surfacing exactly the right passages.",
    tools=[retrieve_chunks],
    verbose=True
)

summarizer = Agent(
    role="Summarizer",
    goal="Produce clear, accurate summaries and answers based on retrieved passages.",
    backstory="You turn dense academic text into clear, faithful summaries without adding unsupported claims.",
    tools=[],
    verbose=True
)
