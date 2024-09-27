# Dialogent

Dialogent is a chat application that showcases the integration of OpenAI's powerful functions to enrich user prompts. The application allows users to interact with an AI agent that can provide insightful responses based on user queries.

## Key Features

- **Interactive Chat**: Engage in a dynamic conversation with the AI. Type your questions in the input box and hit "Submit" to receive responses.
- **Prompt Enrichment**: Utilizing OpenAI's capabilities, the application enriches user prompts to provide more accurate and contextually relevant answers.
- **Weather Functionality**: Get current weather updates based on your location or specific queries about weather conditions.
- **News Functionality**: Stay informed with the latest news articles. Ask about current events or topics of interest, and receive curated news content.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/claudiobottari/dialogent.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dialogent
   ```

3. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory and add your OpenAI API key and database URL:

   ```dotenv
   OPENAI_API_KEY=your-openai-api-key-here
   DATABASE_URL=postgresql://username:password@host:port/database
   ```

6. Run the application:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Start the application and enter your queries in the chat interface.
2. Experiment with questions related to the weather and news.
3. Enjoy engaging with the AI and discovering enriched responses!

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries, suggestions, or feedback, please reach out to:

**Claudio Bottari**  
Email: [bottari@gmail.com](mailto:bottari@gmail.com)  
GitHub: [claudiobottari](https://github.com/claudiobottari)

Thank you for using Dialogent! We hope you enjoy your experience interacting with AI.