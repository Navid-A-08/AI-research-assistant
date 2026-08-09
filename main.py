from dotenv import load_dotenv
from crew import crew
load_dotenv()

result = crew.kickoff(inputs={
    "file_path": "sample_paper.pdf",
    "paper_id": "paper_001",
    "question": "What is the main contribution of this paper?"
})

print("\n\nFINAL RESULT:\n")
print(result)
