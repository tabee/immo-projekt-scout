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
import json
from utils import pretty_print_json

OPENAI_API_KEY = "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"

class AiHelper():
    def __init__(self):
        self.set_key()        
        pass
    
    def set_key(self):
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    def index_pipeline(self, sources_paths):
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

    def answer_question_pipeline(self, document_store, question):

        prompt_template = """
        Alle Fragen beziehen sich ausschliesslich auf das Grundstück
        in den folgenden Dokumenten:
        Beantworte die Frage und nutze dazu die folgenden
        Dokumente:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
        Frage: {{question}}
        Antwort:
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


        results = rag_pipeline.run(data=
            {
                "retriever": {"query": question},
                "prompt_builder": {"question": question},
                "answer_builder": {"query": question},
            }
        )

        return results 

    def answer_questions(self, document_store, questions):
        answers = []
        for question in questions:
            answers.append(self.answer_question_pipeline(document_store, question))
        return answers


if __name__ == "__main__":

    ai_helper = AiHelper()
    
    document_store = ai_helper.index_pipeline(["/workspaces/immo-projekt-scout/20240121111049_extract.pdf"])
    
    
    answers = ai_helper.answer_questions(
        document_store=document_store,
        questions= [
        "Fläche vom Grundstück in m²? Return only the number without m²:",
        "In welchem Jahr wurde das Haus gebaut?",
        "In welcher Gemeinde inkl. BFS-Nr.befindet sich das Haus?",
        """ Was wird steht NACH der Überschrift 1:
        Überschrift 1:  Öffentlich-rechtliche Eigentumsbeschränkungen, welche das Grundstück ... in ... betreffen
        
        Was steht oberhalb der Überschrift 2:
        Überschrift 2:  Öffentlich-rechtliche Eigentumsbeschränkungen, welche das Grundstück nicht betreffen
        
        Zeige mir den Text zwischen den beiden Überschriften:
        """,
        ])
    
    print(f"len(answers): {len(answers)}")
    for answer in answers:
        print(answer['answer_builder']['answers'][0].query)
        print(answer['answer_builder']['answers'][0].data)
        print("\n\n\n")