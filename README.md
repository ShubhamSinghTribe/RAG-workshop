# RAG Workshop Project

## Project Description
This project demonstrates the implementation of a Retrieval-Augmented Generation (RAG) system using Python, LlamaIndex, and Ollama. RAG combines the power of large language models with the ability to retrieve and use external knowledge, making it an effective solution for building AI applications that can access and utilize specific information.

## Technologies Used
- Python 3.8+
- LlamaIndex
- Ollama
- Virtual Environment (venv)
- pip (Python package manager)

## Prerequisites
Before starting, ensure you have the following installed:
1. Python 3.8 or higher
2. Git (for cloning the repository)
3. A code editor (VS Code recommended)

## Step-by-Step Setup Guide

### 1. Install Python
1. Visit [Python's official website](https://www.python.org/downloads/)
2. Download the latest version for your operating system
3. Run the installer
4. During installation, make sure to check "Add Python to PATH"
5. Verify installation by opening a terminal and running:
   ```bash
   python --version
   ```

### 2. Set Up Ollama
1. Visit [Ollama's GitHub repository](https://github.com/ollama/ollama)
2. Download and install Ollama for your operating system
3. Open a terminal and run the following commands:
   ```bash
   # Pull the Llama model
   ollama pull llama3.1
   
   # Start the Ollama server
   ollama serve
   ```
   Keep this terminal window open as it needs to run continuously.

### 3. Create and Set Up Project Environment
1. Create a new directory for your project:
   ```bash
   mkdir rag-workshop
   cd rag-workshop
   ```

2. Create a virtual environment:
   ```bash
   # Create virtual environment
   python3.12 -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install LlamaIndex:
   ```bash
   pip install llama-index
   ```
   For detailed installation instructions, visit: [LlamaIndex Installation Guide](https://docs.llamaindex.ai/en/stable/getting_started/installation/)

### 4. Project Setup
1. Clone this repository or create the necessary files
2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 5. Running the Project
1. Ensure Ollama server is running (from Step 2)
2. Activate your virtual environment if not already activated
3. Run the starter code:
   ```bash
   python rag_create_index.py
   ```

## Understanding the Commands

### Python Virtual Environment Commands
- `python -m venv venv`: Creates a new virtual environment named 'venv'
- `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows): Activates the virtual environment
- `deactivate`: Deactivates the virtual environment

### Ollama Commands
- `ollama pull gemma3:1b`: Downloads the Llama 3.1 model
- `ollama serve`: Starts the Ollama server
- `ollama run gemma3:1b`: Runs the gemma3:1b model. Run this command in a separate terminal window.

### Package Management Commands
- `pip install package_name`: Installs a Python package
- `pip install -r requirements.txt`: Installs all packages listed in requirements.txt
- `pip freeze > requirements.txt`: Creates a requirements.txt file with current package versions

## Best Practices
1. Always work within a virtual environment to avoid package conflicts
2. Keep your requirements.txt updated
3. Use meaningful variable names and add comments to your code
4. Follow PEP 8 style guide for Python code
5. Regularly commit your changes to version control
6. Keep your dependencies up to date
7. Document your code and changes

## Troubleshooting
If you encounter any issues:
1. Ensure Python is properly installed and added to PATH
2. Verify that the virtual environment is activated
3. Check if Ollama server is running
4. Ensure all dependencies are installed
5. Check for any error messages in the terminal

## Additional Resources
- [Python Documentation](https://docs.python.org/)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
