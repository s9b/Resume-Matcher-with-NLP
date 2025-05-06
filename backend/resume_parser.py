from pdfminer.high_level import extract_text
from docx import Document
import io

class ResumeParser:
    def parse(self, content: bytes, filename: str) -> str:
        """Parse resume content from PDF or DOCX files."""
        if filename.endswith('.pdf'):
            return self._parse_pdf(content)
        elif filename.endswith('.docx'):
            return self._parse_docx(content)
        else:
            raise ValueError("Unsupported file format. Please upload PDF or DOCX.")

    def _parse_pdf(self, content: bytes) -> str:
        """Extract text from PDF content."""
        try:
            return extract_text(io.BytesIO(content))
        except Exception as e:
            raise Exception(f"Error parsing PDF: {str(e)}")

    def _parse_docx(self, content: bytes) -> str:
        """Extract text from DOCX content."""
        try:
            doc = Document(io.BytesIO(content))
            return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        except Exception as e:
            raise Exception(f"Error parsing DOCX: {str(e)}")