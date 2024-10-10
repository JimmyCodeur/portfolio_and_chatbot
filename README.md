# Portfolio_and_Chatbot
This project is a web application deployed on Microsoft Azure that combines a personal portfolio with an integrated chatbot. The chatbot is designed to answer user questions based on the information contained in the portfolio.

## User Interface Screenshot

![User Interface Screenshot](./front/img/Screen_demo.PNG)

## Features
Personal Portfolio: My achievements, projects, skills, and professional experience.

Integrated Chatbot: Ask questions about the portfolio content and get relevant real-time responses.

## `main Branch` - Azure Project
To run the code, you need to replace your three keys with Azure credentials:
- `AZURE_CREDENTIALS` : Credentials for connecting to Azure.
- `REGISTRY_PASSWORD` : The password required to access your Azure Container Registry.
- `AZURE_OPENAI_KEY`: The OpenAI API key used for the chatbot.

### Deployment
To run the code, make sure to replace the Azure key values in the appropriate configuration file. Follow the instructions in the `azur-connect.yml` file to configure the CI/CD pipeline and deploy the application on Azure.

## `localhost` Branch - Localhost Project
To run the project locally, start the front end with the command `python3 -m http.server 8011` and run the `fastapi_chat` file for the back end, which will launch the AI.

# Project Structure with Azure

```bash
Portfolio_and_Chatbot/      
│
├── .github/
│   └── workflows/
│       └── azur-connect.yml
│
├── back/
│   └── fastapi_chat.py
│
├── front/
│   ├── Css/ styles.css
│   ├── img/ *.png
│   ├── Dockerfile
│   └── js/ chat.js, script.js
│
├── test/
│   └── tests_unit.py
│
├── .gitignore
├── deploy-aci.yaml
├── Dockerfile
├── README.md
└── requirements.txt
```

