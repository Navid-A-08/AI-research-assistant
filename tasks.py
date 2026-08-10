from crewai import Task  # pyright: ignore[reportMissingImports]
from agents import document_reader, retriever, summarizer, citation_agent, research_adviser, lead_orchestrator

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

citation_task = Task(
    description=(
        "Review the summarized answer and the original document. For each "
        "claim or piece of evidence used, extract the exact source location "
        "(page number, section) and produce a properly formatted citation list."
    ),
    expected_output=(
        "A list of citations mapping each claim in the summary to its source "
        "location in the original document."
    ),
    agent=citation_agent,
    context=[summarize_task]
)

research_adviser_task = Task(
    description=(
        "Based on the paper's content, identify its key limitations, suggest "
        "3-5 related papers worth exploring, and propose 2-3 promising future "
        "research directions."
    ),
    expected_output=(
        "A structured report with three sections: Limitations, Related Papers, "
        "and Future Research Directions."
    ),
    agent=research_adviser,
    context=[summarize_task]
)

lead_orchestrator_task = Task(
    description=(
        "Combine the summary, citations, and research advice into a single, "
        "coherent final response for the user. Ensure nothing is duplicated "
        "or contradictory, and that the response directly answers the "
        "original question."
    ),
    expected_output=(
        "A polished final report combining the summary, citations, and "
        "research adviser's findings."
    ),
    agent=lead_orchestrator,
    context=[summarize_task, citation_task, research_adviser_task]
)
