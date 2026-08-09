from tools.pdf_tools import read_pdf

text = read_pdf.func("sample_paper.pdf")  # .func calls the underlying function directly
print(text[:500])  # print first 500 chars to check it worked