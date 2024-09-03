AI Tutor for Computer Networking

<!-- Optional: Add a logo if you have one -->
Overview

The AI Tutor for Computer Networking is an intelligent, interactive tool designed to help students navigate through the renowned textbook "Computer Networking: A Top-Down Approach" by James Kurose and Keith Ross. This app not only provides access to the textbook itself but also offers an AI-powered tutor that can answer questions, clarify concepts, and guide students through the complexities of computer networking.

Unlike generic AI models, this AI Tutor is enhanced with a custom assistant that has a working memory of the textbook. This feature enables the AI to provide more relevant, context-aware responses that are directly tied to the content of the book.
Features

    Interactive PDF Viewer: Students can read the "Computer Networking: A Top-Down Approach" textbook directly within the app.
    AI-Powered Tutor: A custom assistant built using OpenAI's Assistants API, capable of answering questions related to the textbook with context-aware responses.
    Working Memory: The AI retains a memory of the book’s content, enabling it to reference specific sections and provide detailed explanations tailored to the user's query.
    User-Friendly Interface: The app is designed with simplicity in mind, offering an intuitive interface where students can easily switch between reading and asking questions.

How It Works

    Read the Textbook: The app features an embedded PDF viewer that allows you to read "Computer Networking: A Top-Down Approach" by James Kurose and Keith Ross.
    Ask Questions: If you encounter any difficulties or need clarification, you can ask the AI tutor questions related to the content of the textbook.
    Custom AI Responses: The AI tutor leverages its working memory of the textbook to provide accurate, contextually relevant answers, helping you better understand complex topics.
    Continuous Learning: The AI can guide you through exercises, help with difficult concepts, and offer insights that are directly aligned with the material in the textbook.

Installation
Prerequisites

    Python 3.7 or later
    Git
    A GitHub account
    A Streamlit account for deployment (if deploying on Streamlit Cloud)

Clone the Repository

```bash
git clone https://github.com/shayanahmad7/streamlit-tutor-app.git
cd streamlit-tutor-app
```
Install Dependencies

Make sure you have the necessary dependencies installed. You can do this using pip:

```bash
pip install -r requirements.txt
```
Running the App Locally

To run the Streamlit app locally, use the following command:

```bash
streamlit run app.py
```

This will start a local server where you can interact with the AI Tutor.
Deploying on Streamlit Cloud

To deploy this app on Streamlit Cloud:

    Ensure your project is pushed to your GitHub repository.
    Go to Streamlit Cloud and create a new app.
    Select your GitHub repository and configure the deployment settings.
    Deploy the app, and Streamlit Cloud will provide a URL where your app is accessible.

Usage
Reading the Book

    Open the app in your browser.
    The left side of the interface will display the PDF viewer with the textbook.
    Scroll through and read the content as needed.

Asking Questions

    On the right side of the interface, you will find the AI tutor chat window.
    Type your question related to the textbook content.
    The AI tutor will respond with context-aware answers, helping you understand the material better.

Example Questions

    "Can you explain how TCP congestion control works?"
    "What is the difference between IPv4 and IPv6?"
    "How does DNS resolve domain names?"

Technologies Used

    Streamlit: The main framework for building the web application.
    OpenAI's Assistants API: For creating a custom AI tutor with memory capabilities.
    Python: The programming language used to build the app.
    Google Drive: Used to host and embed the PDF version of the textbook.

Contributing

Contributions to the project are welcome! Feel free to submit issues or pull requests to improve the app.
Steps to Contribute

    Fork the repository.
    Create a new branch for your feature or bugfix.
    Commit your changes and push the branch to your fork.
    Submit a pull request describing your changes.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    James Kurose and Keith Ross: For writing the "Computer Networking: A Top-Down Approach", the textbook that this AI tutor is based on.
    OpenAI: For providing the powerful API that powers the AI tutor.
    Streamlit: For making web app deployment easy and accessible.

