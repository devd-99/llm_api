# AI-Powered Essay Analysis

This project demonstrates how to use LlamaIndex and Ollama to analyze essays using AI. It includes a Python script that reads an essay, indexes it, and answers questions about its content.

## Prerequisites

- Docker
- Docker Compose
- wget (for downloading sample data)

## Setup

1. Clone this repository:
   ```
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. Download the sample essay:
   ```
   mkdir -p paul_graham
   wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt' -O 'paul_graham/paul_graham_essay.txt'
   ```

3. Build and start the Docker container:
   ```
   docker-compose up -d --build
   ```

4. Enter the container:
   ```
   docker-compose exec dev bash
   ```

5. Inside the container, install the required Python packages:
   ```
   pip install llama-index chromadb ipython
   ```

## Usage

1. Run the Python script:
   ```
   python app.py
   ```

   This script will:
   - Load the essay from the `paul_graham` directory
   - Create an index using LlamaIndex
   - Set up a query engine
   - Ask a sample question: "What did the author do growing up?"

2. The script will print the response to the console.

## Project Structure

- `docker-compose.yml`: Defines the Docker services for the project.
- `app.py`: The main Python script that processes the essay and performs the query.
- `paul_graham/`: Directory containing the downloaded essay.

## Customization

- To analyze different essays, replace the content in the `paul_graham` directory and update the `SimpleDirectoryReader` path in `app.py`.
- Modify the query in `app.py` to ask different questions about the essay.

## Troubleshooting

If you encounter any issues with Chroma or Ollama connections, ensure that:
- The Chroma server is running and accessible.
- The Ollama service is running on the specified IP and port.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]