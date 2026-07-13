from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
if __name__ == "__main__":
    doc=load_all_documents("data")
    store=FaissVectorStore("faiss_store")
    # store.build_from_documents(doc)
    # store.load()
    # print(store.query("Machine Learning Basics", top_k=3))

    rag_search = RAGSearch()
    query = "What is Machine Learning Basics"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)

    
    
