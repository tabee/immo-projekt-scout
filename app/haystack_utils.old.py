''' A.I. copilot for information extraction '''
from haystack.components.builders.answer_builder import AnswerBuilder
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack.components.converters import PyPDFToDocument
from haystack.components.generators import OpenAIGenerator
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.components.writers import DocumentWriter
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.pipeline import Pipeline
from pathlib import Path
import os


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def index_pipeline(sources_paths):
    document_store = InMemoryDocumentStore()
    converter = PyPDFToDocument()

    pipeline = Pipeline()
    pipeline.add_component("converter", PyPDFToDocument())
    pipeline.add_component("cleaner", DocumentCleaner())
    pipeline.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=5))
    pipeline.add_component("writer", DocumentWriter(document_store=document_store))
    pipeline.connect("converter", "cleaner")
    pipeline.connect("cleaner", "splitter")
    pipeline.connect("splitter", "writer")
    pipeline.draw("index-pipeline.png")
    pipeline.run({"converter": {"sources": sources_paths}})
    return document_store

def answer_pipeline(question, document_store):
    
    prompt_template = """
    Given these documents, answer the question.
    Documents:
    {% for doc in documents %}
        {{ doc.content }}
    {% endfor %}
    Question: {{question}}
    Answer:
    """

    retriever = InMemoryBM25Retriever(document_store=document_store)
    prompt_builder = PromptBuilder(template=prompt_template)
    llm = OpenAIGenerator(api_key=os.environ.get("OPENAI_API_KEY"))
    answer_builder = AnswerBuilder()


    rag_pipeline = Pipeline()
    rag_pipeline.add_component("retriever", retriever)
    rag_pipeline.add_component("prompt_builder", prompt_builder)
    rag_pipeline.add_component("llm", llm)
    rag_pipeline.add_component("answer_builder", answer_builder)
    rag_pipeline.connect("retriever", "prompt_builder.documents")
    rag_pipeline.connect("prompt_builder", "llm")
    rag_pipeline.connect("llm.replies", "answer_builder.replies")
    rag_pipeline.draw("rag_pipeline.png")


    rag_pipeline.draw("rag_pipeline.png")

    results = rag_pipeline.run(
        {
            "retriever": {"query": question},
            "prompt_builder": {"question": question},
            "answer_builder": {"query": question},
        }
    )
    return results 

if __name__ == "__main__":
    
    document_store = index_pipeline(["/workspaces/immo-projekt-scout/20240121111049_extract.pdf"])
    anser_q1 = answer_pipeline(
        question="Fläche vom Grundstück in m²? Return only the number without m²:",
        document_store=document_store,
    )

    for answer in anser_q1["answer_builder"]["answers"]:
        print(answer.data)