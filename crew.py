from crewai import Crew, Process

from agents import document_reader, retriever, summarizer, citation_agent, research_adviser, lead_orchestrator
from tasks import (
    ingest_task,
    retrieve_task,
    summarize_task,
    citation_task,
    research_adviser_task,
    lead_orchestrator_task,
)

crew = Crew(
    agents=[document_reader, retriever, summarizer, citation_agent, research_adviser, lead_orchestrator],
    tasks=[
        ingest_task,
        retrieve_task,
        summarize_task,
        citation_task,
        research_adviser_task,
        lead_orchestrator_task,
    ],
    process=Process.sequential,
    verbose=True
)
