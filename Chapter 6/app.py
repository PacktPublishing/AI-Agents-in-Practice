import streamlit as st
import requests
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
import sqlite3
from langchain.callbacks import StreamlitCallbackHandler
from langchain.memory import ConversationBufferMemory
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

# Display the logo in the sidebar
st.set_page_config(
    page_title="MammaChePiada!",
    page_icon="🥙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_chat_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")


# Initialize the Azure OpenAI model
model = AzureChatOpenAI(
    openai_api_version=openai_api_version,
    azure_deployment=azure_chat_deployment,
)



embeddings = AzureOpenAIEmbeddings(
    api_key = openai_api_key,
    azure_deployment="text-embedding-3-large"
)


db = SQLDatabase.from_uri("sqlite:///piadineria.db")



sql_toolkit = SQLDatabaseToolkit(db=db, llm=model)

# Define the tool to add an item to the cart
@tool
def add_to_cart(item_name: str, item_price: float) -> str:
    """Add an item to the cart."""
    url = 'http://localhost:3000/cart'  # Ensure this matches the JSON Server endpoint
    cart_item = {
        'name': item_name,
        'price': item_price
    }
    
    response = requests.post(url, json=cart_item)
    
    if response.status_code == 201:
        return f"Item '{item_name}' added to cart successfully."
    else:
        return f"Failed to add item to cart: {response.status_code} {response.text}"
    


index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)




index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

file_path = (
    "documents"
)
loader = PyPDFDirectoryLoader(file_path)
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)


vector_store.add_documents(documents=docs)

retriever = vector_store.as_retriever()



rag_tool = create_retriever_tool(
    retriever,
    "document_search",
    """
    Search and return information restaurants health certificate and owner's history.
    """
)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """You are an AI assistant for a Piadineria Restaurant. 
            You help customers explore the menu and choose the best piadine or Italian specialties through friendly, interactive questions.
            When the user asks for product details (ingredients, allergens, vegetarian options, price, etc.), you can query the product database.

            Once the user is ready to order, ask if they'd like to add the selected item to their cart.
            If they confirm, add the item to the cart using your tools.

            When using a tool, respond only with the final result. For example:
            Human: Add Classic Piadina to the cart with price 5.50
            AI: Item 'Classic Piadina' added to cart successfully.
        """),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

# Setup the toolkit
toolkit = [rag_tool, add_to_cart, sql_toolkit.get_tools()[0], sql_toolkit.get_tools()[1], sql_toolkit.get_tools()[2], sql_toolkit.get_tools()[3]]



msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
)

# Construct the OpenAI Tools agent
agent = create_openai_tools_agent(model, toolkit, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=toolkit, memory=memory,
        return_intermediate_steps=True,
        handle_parsing_errors=True, verbose=True)



#st.image("images/Picture3.png", width=1000)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    .big-title {
        font-family: 'Pacifico', cursive;
        font-size: 60px;
        color: #000000;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .header-2 {
        font-family: 'Pacifico', cursive;
        font-size: 40px;
        color: #000000;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .header-3 {
        font-family: 'Pacifico', cursive;
        font-size: 30px;
        color: #000000;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title
st.markdown("<h1 class='header-2'>Welcome to MammaChePiada!</h1>", unsafe_allow_html=True)
# Display the styled title in the sidebar

st.image("images/Picture3.png", use_container_width =True)

with st.container(border=True):
    st.markdown(
    "<h1 class='header-2'>Our history</h1>",
    unsafe_allow_html=True)
    st.image("images/piada.jpg", use_container_width =True)

    st.markdown("<h2 class='header-3'>La Piada</h2>", unsafe_allow_html=True)
    st.write("A traditional Italian flatbread typically filled with various ingredients.")

    st.image("images/chiosco.jpg", use_container_width =True)
    st.markdown("<h2 class='header-3'>Chiosco</h2>", unsafe_allow_html=True)
    st.write("Our cozy kiosk where you can enjoy freshly made piadas.")


    st.image("images/aperta.jpg", use_container_width =True)
    st.markdown("<h2 class='header-3'>Ingredients</h2>", unsafe_allow_html=True)
    st.write("Our piadas are made with the finest ingredients and cooked to perfection.")



if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if "messages" not in st.session_state:
    st.session_state.messages = []


st.markdown("<h1 class='header-2'>Curious to learn more about our Piadinas? Ask anything!</h1>", unsafe_allow_html=True)


if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
    msgs.clear()
    msgs.add_ai_message("How can I help you?")
    st.session_state.steps = {}

avatars = {"human": "user", "ai": "assistant"}
for idx, msg in enumerate(msgs.messages):
    with st.chat_message(avatars[msg.type]):
        # Render intermediate steps if any were saved
        for step in st.session_state.steps.get(str(idx), []):
            if step[0].tool == "_Exception":
                continue
            with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
                st.write(step[0].log)
                st.write(step[1])
        st.write(msg.content)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Want to know what's in the menu?")
if prompt:
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = agent_executor.invoke({"input": prompt}, {"callbacks": [st_cb]})
        st.write(response["output"])
        st.session_state.steps[str(len(msgs.messages) - 1)] = response["intermediate_steps"]

if st.button("Clear chat"):
    st.session_state.messages = []
    st.rerun()

