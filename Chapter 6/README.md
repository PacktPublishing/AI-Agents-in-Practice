# AI Agent for Piadineria Restaurant

This notebook demonstrates the implementation of an AI-powered assistant for a Piadineria restaurant using LangChain and Azure OpenAI services. The agent helps customers explore the menu, get product information, and place orders.

## Features


- **SQL Database Integration**: Product and supplier database management
- **Document Retrieval**: RAG (Retrieval Augmented Generation) implementation for accessing restaurant documentation
- **Shopping Cart Integration**: Ability to add items to a cart through an API
- **Interactive Chat Interface**: Natural language interaction with customers

## Components

### 1. Azure OpenAI Integration
- Uses Azure OpenAI for chat completion and embeddings
- Requires proper environment variables setup (API key, endpoint, etc.)

### 2. Database Management
- SQLite database (`piadineria.db`) containing:
  - Products table (30 Italian food items)
  - Suppliers table (10 suppliers)
- Includes comprehensive product information:
  - Product details (name, price, stock)
  - Allergen information
  - Nutritional data
  - Supplier relationships

### 3. Tools and Capabilities
- SQL Database Tools: Query and manage product/supplier data
- Cart Management: Add items to shopping cart
- Document Retrieval: Search through restaurant documentation
  - Health certificates
  - Owner's history
  - Other relevant documents

### 4. Agent Evaluation
- Integration with LangSmith for agent evaluation
- Custom evaluation metrics:
  - Correctness scoring
  - Tool usage evaluation
  - Response quality assessment

## Setup Requirements

1. Environment Variables:
   - AZURE_OPENAI_API_VERSION
   - AZURE_OPENAI_ENDPOINT
   - AZURE_OPENAI_API_KEY
   - AZURE_OPENAI_CHAT_DEPLOYMENT_NAME
   - LANGSMITH_API_KEY
   - LANGSMITH_ENDPOINT
   - LANGSMITH_PROJECT

2. Required Python Packages:
   - langchain
   - openai
   - python-dotenv
   - faiss-cpu
   - sqlite3
   - pandas
   - requests
   - langsmith

3. Additional Files:
   - `piadineria.db`: SQLite database
   - `documents/`: Folder containing PDF documentation
   - `db.json` running on localhost:3000 for cart functionality. To run this server 

## Usage

The notebook provides an interactive chat interface where users can:
- Query product information
- Check prices and availability
- Add items to cart
- Get information about allergens and ingredients
- Access restaurant documentation
- Learn about the restaurant's history and certifications


## Agent Evaluation

The notebook includes comprehensive evaluation capabilities:
- Dataset creation for testing
- Correctness evaluation
- Tool usage assessment
- Response quality measurement
- Integration with LangSmith for detailed analytics

## Notes

- The cart functionality requires a running JSON server on localhost:3000
- All sensitive information should be stored in a `.env` file
- Regular evaluation of agent performance is recommended through LangSmith
