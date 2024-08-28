# ml_engineer_test_project
ML Engineer Test Project: Building an Agentic Worker



## Installation

1. Clone the repository:
    ```plaintext
    git clone git clone https://github.com/lizmarques/ml_engineer_test_project.git
    ```

2.  Create a virtual environment:
    
    ```plaintext
    python -m venv venv
    ```
    
3.  Install the dependencies:
    
    ```plaintext
    pip install -r requirements.txt
    ```
    
4.  Adjust all file paths in the scripts to match your personal directory structure. For example:
   
    ```plaintext
    load_dotenv(r"C:\Users\YourUsername\YourProject\.env")
    ```
    
5.  Update the .env file with your own credentials and configuration settings.
    ```plaintext
    SERPER_API_KEY=your_serper_api_key
    OPENAI_API_KEY=your_openai_api_key
    AGENTOPS_API_KEY=your_agentops_api_key
    ```
    
7.  Launch the Streamlit application by running the following command in your terminal:
   
    ```plaintext
    streamlit run main.py
    ```
