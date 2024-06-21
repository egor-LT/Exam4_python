from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def print(self):
        pass

    def prepare_for_printing(self):
        self.print()

class PDFDocument(Document):
    def print(self):
        print("Printing PDF document...")

class WordDocument(Document):
    def print(self):
        print("Printing Word document...")

class ExcelDocument(Document):
    def print(self):
        print("Printing Excel document...")

class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == "PDF":
            return PDFDocument()
        elif doc_type == "Word":
            return WordDocument()
        elif doc_type == "Excel":
            return ExcelDocument()
        else:
            raise ValueError("Unknown document type")

# Приклад використання:
factory = DocumentFactory()

pdf_doc = factory.create_document("PDF")
word_doc = factory.create_document("Word")
excel_doc = factory.create_document("Excel")

# Виклик методу prepare_for_printing
pdf_doc.prepare_for_printing()
word_doc.prepare_for_printing()
excel_doc.prepare_for_printing()
