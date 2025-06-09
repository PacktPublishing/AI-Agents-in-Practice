# Working with LLMs SDKs

This Jupyter notebook demonstrates how to interact with Large Language Models (LLMs) using both Azure OpenAI and OpenAI SDKs. It provides practical examples of setting up API connections and making various types of requests to these services.

## Prerequisites

- Python environment with Jupyter support
- Required packages:
  ```
  openai
  python-dotenv
  ```

## Setup and Configuration

### Environment Variables
The notebook requires the following environment variables to be set in a `.env` file:
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
- `OPENAI_API_KEY` (if using OpenAI directly)

## Features

### 1. Azure OpenAI Integration
- Detailed instructions for obtaining Azure OpenAI endpoint and API keys
- Example configuration for Azure OpenAI client
- Link to official Microsoft documentation for complete setup guide

### 2. OpenAI Integration
- Alternative setup for using the OpenAI API directly
- Example configuration for standard OpenAI client

### 3. Chat Completion Examples
- Basic chat completion request
- Response inspection and parsing
- JSON structure analysis of API responses

### 4. Interactive Chat Implementation
- Implementation of an interactive chat loop
- Message history management
- Conversation context preservation
- Exit commands handling

## Code Examples

The notebook includes several practical examples:
1. Basic API setup and authentication
2. Simple chat completion requests
3. Response structure inspection
4. Interactive chat implementation

## Usage

Each section of the notebook can be run sequentially to:
1. Set up the environment and load necessary credentials
2. Initialize the API client (Azure OpenAI or OpenAI)
3. Make API requests
4. Inspect responses
5. Run an interactive chat session

## Interactive Chat Features

The interactive chat implementation includes:
- System message setup
- User input handling
- Response processing
- Conversation history management
- Exit commands ("exit" or "quit")

## Response Analysis

The notebook demonstrates how to:
- Access response content
- Convert responses to JSON
- Pretty print response structures
- Extract specific fields from responses

## Security Notes

- API keys and endpoints should be stored in a `.env` file
- The `.env` file should never be committed to version control
- Azure OpenAI provides two keys for secure rotation
- Always use environment variables for sensitive credentials

## Additional Resources

- [Azure OpenAI Quickstart Guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/gpt-v-quickstart?tabs=command-line%2Ckeyless%2Ctypescript-keyless&pivots=programming-language-python)
- Azure Portal documentation for key management
- OpenAI API documentation
