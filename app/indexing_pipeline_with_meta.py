from typing import Dict, Any
from pathlib import Path
from datetime import datetime
import os

from haystack import Pipeline
from haystack.dataclasses import ByteStream
from haystack.components.others import Multiplexer
from haystack.components.converters import PyPDFToDocument, TextFileToDocument
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack.components.routers import FileTypeRouter
from haystack.components.joiners import DocumentJoiner
from haystack.components.writers import DocumentWriter
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.pipeline_utils import build_indexing_pipeline
from haystack.pipeline_utils.indexing import download_files


document_store = InMemoryDocumentStore()

p = Pipeline()
p.add_component(instance=FileTypeRouter(mime_types=["text/plain", "application/pdf"]), name="file_type_router")
p.add_component(instance=Multiplexer(Dict[str, Any]), name="metadata_multiplexer")
p.add_component(instance=TextFileToDocument(), name="text_file_converter")
p.add_component(instance=PyPDFToDocument(), name="pdf_file_converter")
p.add_component(instance=DocumentJoiner(), name="joiner")
p.add_component(instance=DocumentCleaner(), name="cleaner")
p.add_component(instance=DocumentSplitter(split_by="sentence", split_length=250, split_overlap=30), name="splitter")
p.add_component(instance=DocumentWriter(document_store=document_store), name="writer")

p.connect("file_type_router.text/plain", "text_file_converter.sources")
p.connect("file_type_router.application/pdf", "pdf_file_converter.sources")
p.connect("metadata_multiplexer", "text_file_converter.meta")
p.connect("metadata_multiplexer", "pdf_file_converter.meta")
p.connect("text_file_converter.documents", "joiner.documents")
p.connect("pdf_file_converter.documents", "joiner.documents")
p.connect("joiner.documents", "cleaner.documents")
p.connect("cleaner.documents", "splitter.documents")
p.connect("splitter.documents", "writer.documents")

# Add metadata to your files by using ByteStream
sources = ["/workspaces/immo-projekt-scout/20240121111049_extract.pdf"]
for position, path in enumerate(list(Path(".").iterdir())):
    if path.is_file():
        # Create the ByteStream
        source = ByteStream.from_file_path(path)
        # Add the metadata
        source.meta["path"] = path
        source.meta["position"] = position
        sources.append(source)

result = p.run(
    {
        "file_type_router": {"sources": sources},
        "metadata_multiplexer": {"value": {"date_added": datetime.now().isoformat()}},
    }
)

assert all("date_added" in doc.meta for doc in document_store.filter_documents())

print("document_store after indexing one PDF file.")
print(f"we have {document_store.count_documents()} in the document store")
print(document_store.to_dict())





# Download example files from web
files = download_files(sources=[
    "https://www.eak.admin.ch/eak/de/home/dokumentation/pensionierung/altersrente.html",
    "https://www.eak.admin.ch/eak/de/home/reform-ahv21/ueberblick/ausgleichsmassnahmen.html",
    "https://www.eak.admin.ch/eak/de/home/EAK/publikationen/jahresberichte/jahresbericht-2022-wrapper/beitraege.html", 
    "https://www.eak.admin.ch/dam/eak/de/dokumente/jahresberichte/eak-jahresbericht-2022.pdf.download.pdf/EAK%20Jahresbericht%202022%20d.pdf",
    ])

# Pipelines are our main abstratcion.
# Here we create a pipeline that can index TXT and HTML. You can also use your own private files.
indexing_pipeline = build_indexing_pipeline(
    document_store=document_store,
    embedding_model="intfloat/e5-base-v2",
    supported_mime_types=["text/plain", "text/html"],  # "application/pdf"
)
indexing_pipeline.run(files=files)  



print("\n\n")
print("document_store after indexing one HTML file.")
print(f"we have {document_store.count_documents()} in the document store")
print(document_store.to_dict())