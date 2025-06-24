# Multi-agent Application Notebook

## Introduction
This notebook demonstrates the implementation of a multi-agent system using LangGraph and Azure OpenAI. The solution is designed to create a group chat of the following agent:

1. **Web Agent**: Perform web-based searches using Tavily.
2. **Portfolio Reader Agent**: Read and summarize portfolio data.
3. **Report Generator Agent**: Create detailed reports based on portfolio optimization.

The group chat will be managed by a Supervisor Agent which manages interactions between agents and ensure task completion.


## Setup Instructions

### Prerequisites
1. **Python Version**: Ensure Python 3.9 or higher is installed.
2. **Environment Variables**: Create a `.env` file in the `Chapter 7` directory with the following keys:
   - `AZURE_OPENAI_API_VERSION`
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
   - `TAVILY_API_KEY`

   **Note**: You can use any other LLM provider. In that case, ensure to specify the provider's API or Hugging Face API in the `.env` file.

### Installation
1. **Install Required Libraries**:
   Run the following command to install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install LangGraph**:
   Run the following command to install LangGraph:
   ```bash
   pip install -U langgraph
   ```

### Running the Notebook
1. Open the notebook `multiagent.ipynb` in Jupyter Notebook or VS Code.
2. Execute the cells sequentially to:
   - Set up environment variables.
   - Initialize agents.
   - Generate and analyze portfolio data.
   - Create a detailed report.

### Useful Links
- [LangChain Documentation](https://docs.langchain.com/)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- [Tavily Search API](https://tavily.com/)

## Outputs
Generated files and reports will be saved in the `outputs` directory within `Chapter 7`. Ensure this directory exists before running the notebook.

## Notes
- Ensure all environment variables are correctly set up.
- The notebook is designed to handle portfolio optimization tasks for Q4 2025.
- For any issues, refer to the documentation links provided above.
