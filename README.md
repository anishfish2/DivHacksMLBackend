# DivHacks 2023 Project - Accessible Text Analysis Tools

Welcome to the **DivHacks 2023 Project** repository! This project was developed for the DivHacks 2023 competition and aims to create accessible text analysis tools for individuals with disabilities. The project includes a sarcasm detector, a sentiment analysis tool, and a summarizer, making online content more accessible and understandable.

## Project Overview

- **Sarcasm Detector**: This tool identifies instances of sarcasm in text, helping users better understand the intended tone of online content. Users with autism or difficulties in detecting sarcasm may benefit from this feature.

- **Sentiment Analysis Tool**: The sentiment analysis tool assesses the emotional tone of text, categorizing it as positive, negative, or neutral. This can aid individuals with emotional or mood disorders in interpreting online content.

- **Summarizer**: The summarizer generates concise summaries of longer texts, allowing users with cognitive impairments or reading difficulties to access content more efficiently.

## Repository Structure

Here's an overview of the files and folders within this repository:

- `/bbc`: Contains text data from the BBC, which serves as a dataset for some of the natural language processing tasks.

- `/models`: Stores trained models, including the sarcasm detector and sentiment analysis models.

- `/sarcasmData`: Contains data used for training the sarcasm detection model.

- `app.py`: The Flask application that serves as the backend for the accessible website.

- `sarcasmDetect.py`: The Python script for the sarcasm detector, which identifies sarcastic sentences.

- `sarcasmModel.py`: Python script containing the sarcasm detection model and training code.

- `sentiment.py`: The Python script for the sentiment analysis tool, which assesses the emotional tone of text.

- `summary.py`: Python script for the summarizer, which generates concise text summaries.

- `requirements.txt`: Lists the required Python packages and their versions for this project. You can install these dependencies using `pip install -r requirements.txt`.

## Who Would Benefit

The accessible text analysis tools in this project can benefit individuals with various disabilities and impairments, including but not limited to:

- **Autism Spectrum Disorders (ASD)**: The sarcasm detector helps users with ASD better understand the intended tone of online content.

- **Emotional or Mood Disorders**: The sentiment analysis tool assists individuals with emotional or mood disorders in gauging the emotional tone of text.

- **Cognitive Impairments**: The summarizer provides concise content summaries, aiding users with cognitive impairments in accessing information more efficiently.

## How to Use the Flask Application

To use the Flask application, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies by running the following command:

pip install -r requirements.txt

3. Start the Flask application by running:

python app.py

4. Connect the application to a front end.

5. Explore the various accessible text analysis tools available on the website.

Enjoy using and enhancing these accessible text analysis tools!

If you have any questions or feedback, please feel free to reach out.




