# AI Assistant Library

This project is an Library AI Assistant built using OpenAI, ChromaDB, and Streamlit. The library is designed to provide a chatbot that can interact with users based on a knowledge base of uploaded books.

## Features

- **OpenAI Integration**: Utilizes OpenAI's powerful language models to generate responses.
- **ChromaDB**: Manages and queries the knowledge base efficiently. Learn from user feedback and response accordingly.
- **Streamlit**: Provides an interactive web interface for the chatbot.
- **Knowledge Base**: Includes a collection of books uploaded to enhance the chatbot's responses.
- **Testing with RAGAS**: Evaluates the chatbot's responses to ensure they meet desired thresholds.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/chatbot_openai_rag.git
    ```
2. Navigate to the project directory:
    ```bash
    cd chatbot_openai_rag
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Create a `.env` file in the project directory and add your OpenAI access key:
    ```plaintext
    OPENAI_API_KEY=your_openai_access_key
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run chatbot/main.py
    ```
2. Interact with the chatbot through the web interface.

## Testing

We use the RAGAS library to evaluate the chatbot's responses. To run the tests, use the following command:
```bash
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://openai.com/)
- [ChromaDB](https://chromadb.com/)
- [Streamlit](https://streamlit.io/)
- [RAGAS](https://github.com/yourusername/ragas)
