from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def document_reader(path):
    """
    Load documents from a directory.
    """
    # documents = SimpleDirectoryReader('/content/drive/MyDrive/beyond_enlightenment').load_data()
    try:
        documents_loaded = SimpleDirectoryReader(path).load_data()
        return documents_loaded
    except Exception as e:
        print(f"An error occurred while loading documents: {e}")
        return None

def create_index_from_documents(documents, embed_model, index_persist_path=None):
    """
    Create an index from the loaded documents using the specified embedding model.
    If no embedding model is provided, it will use the default one.
    If index_persist_path is provided, the index will be persisted to that path.
    """
    try:
        if embed_model is None:
            # Uses openai embedding model which is not free
            vector_store_index = VectorStoreIndex.from_documents(documents, show_progress=True)
        else:
            # Uses passed embedding model which is free
            vector_store_index = VectorStoreIndex.from_documents(documents, show_progress=True,
                                                                 embed_model=embed_model)
        # Persist index to disk
        if index_persist_path is not None:
            vector_store_index.storage_context.persist(index_persist_path)
        return vector_store_index
    except Exception as e:
        print(f"An error occurred while creating the index: {e}")
        return None

if __name__ == '__main__':
    # verify key is working
    # verify_api_key()

    # Create an index from the documents
    create_index = True
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2") # this is the embedding model to use for the index generation
    index_persist_path = "rag_files_miniLM"
    if create_index:
        # document location
        path = "rag_files"
        documents = document_reader(path)
        print(f"Documents loaded: {len(documents)}")
        index = create_index_from_documents(documents=documents, embed_model=embed_model,
                                            index_persist_path=index_persist_path)
    print(f"Index Loaded: {index}")
