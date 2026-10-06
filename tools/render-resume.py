"""Render files/Alex_Gold_Resume.pdf into the page images the on-site viewer shows.
Run after replacing the PDF:  pip install pymupdf && python3 tools/render-resume.py
Then update RESUME_PAGES in index.html if the page count changed."""
import fitz

doc = fitz.open('files/Alex_Gold_Resume.pdf')
for i, page in enumerate(doc, 1):
    z = 1600 / page.rect.width
    page.get_pixmap(matrix=fitz.Matrix(z, z), alpha=False).save(f'images/resume-{i}.jpg', jpg_quality=82)
print(f'rendered {len(doc)} pages')
