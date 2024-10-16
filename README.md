# Kansai Food Guide

A Streamlit-powered app that recommends restaurants in the Kansai region based on cuisine and price. The app uses LangChain and Ollama, running locally with the **llama3.2:3b** model, for intelligent, location-specific suggestions. A map display showing the locations of the restaurants is also available.

## Requirements

- **Python**: Version **3.11** or later
- **Streamlit**: Version **1.39.0** or later
- **langchain_community**: Any version
- **geopy**: Version **2.4.1** or later
- **Ollama**: Version **0.3.13** or later

## Setup and Usage

1. **Create and enter your virtual environment**:
   Run the following commands from the project directory:
   ```bash
   conda env create -f environment.yml
   conda activate test

2. Clone the repo
   ```sh
   git clone https://github.com/iceman2434/kansai-food-guide.git
   ```

3. Get your Geocoding API Key (optional) at [https://developers.google.com/maps/documentation/geocoding/start](https://developers.google.com/maps/documentation/geocoding/start)

4. Enter your Geocoding API in `config.py` or leave it empty
   ```py
   API_KEY = 'ENTER YOUR API';
   ```

5. Run the application with:
   ```bash
   streamlit run main.py
   ```
