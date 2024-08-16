from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, ServiceContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama



from IPython.display import Markdown, display
import chromadb
from chromadb.config import Settings

chroma_client = None

try:
    chroma_client = chromadb.EphemeralClient(Settings(anonymized_telemetry=False, chroma_server_host="0.0.0.0", chroma_server_http_port=8000))
except Exception as e:
    print("error initializing connection to chroma client"+str(e))
    exit(1)
print("here")
def setup_chroma_collection(collection_name="quickstart", index_name="paul"):
    try:
        
        # Create or get the collection
        try:
            collection = chroma_client.create_collection(name=collection_name)
        except chromadb.exceptions.CollectionAlreadyExistsError:
            collection = chroma_client.get_collection(name=collection_name)
        
        return collection

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# create client and a new collection
# chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")
llm = Ollama(model="llama3.1:8b", base_url="http://192.168.65.254:11434", request_timeout=60.0)
service_context = ServiceContext.from_defaults(llm=llm, embed_model=HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5"))

collection_name = "quickstart"
try:
    chroma_collection = chroma_client.get_or_create_collection(collection_name)
except Exception as e:
    print("error creating or connecting to connection"+str(e))


documents = SimpleDirectoryReader("paul_graham").load_data()

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama3", request_timeout=360.0)
print("settings loaded")
index = VectorStoreIndex.from_documents(
    documents,
    service_context = service_context
)
print("index loaded")

try:
    query_engine = index.as_query_engine()
except Exception as e:
    print("Exception at engine creation: "+str(e))

print("query engine loaded")
response = None
try:
    response = query_engine.query("What did the author do growing up?")
except Exception as e:
    print("Exception at query: "+(str(e)))
print(response)

