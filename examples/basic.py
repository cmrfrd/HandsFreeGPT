
from chromadb.config import Settings
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.tools.ddg_search.tool import DuckDuckGoSearchTool
from langchain.tools.file_management.read import ReadFileTool
from langchain.tools.file_management.write import WriteFileTool
from langchain.vectorstores import Chroma

from handsfreegpt.agent import AutoGPT
from handsfreegpt.tools import PythonTool, ThinkTool

embeddings = OpenAIEmbeddings()

tools = [
    DuckDuckGoSearchTool(),
    WriteFileTool(root_dir="/tmp"),
    ReadFileTool(root_dir="/tmp"),
    PythonTool(),
    ThinkTool()
]

c = Chroma(
    embedding_function=embeddings,
    client_settings=Settings(
        chroma_api_impl="rest",
        chroma_server_host="chroma",
        chroma_server_http_port="8000",
    )
)
c.add_texts(texts=[" "])
c._client.create_index(c._LANGCHAIN_DEFAULT_COLLECTION_NAME)

agent = AutoGPT.from_llm_and_tools(
    ai_name="Contribot",
    ai_role="Assistant",
    tools=tools,
    llm=ChatOpenAI(temperature=0, model_name="gpt-4"),
    memory=c.as_retriever(),
)
# Set verbose to be true
agent.chain.verbose = True
agent.run(
    [
        "Discover what the meaning of life is",
        "Ensure the calculation is correct",
        "Write the result to a file called 'meaning_of_life.txt' in the root directory",
    ]
)