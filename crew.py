from crewai import Crew, Process

from agents import document_reader, retriever, summarizer
from tasks import ingest_task, retrieve_task, summarize_task

crew = Crew(
    agents=[document_reader, retriever, summarizer],
    tasks=[ingest_task, retrieve_task, summarize_task],
    process=Process.sequential,
    verbose=True
)
