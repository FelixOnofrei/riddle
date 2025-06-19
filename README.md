# Streamlit Riddle App

A simple Streamlit application that reveals secret content when the correct password is entered.

## Running the App Locally

### Without Docker

1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   streamlit run app.py
   ```

### With Docker

1. Build and start the container:
   ```
   docker-compose up -d
   ```

2. Access the app at http://localhost:8501

3. To stop the container:
   ```
   docker-compose down
   ```
