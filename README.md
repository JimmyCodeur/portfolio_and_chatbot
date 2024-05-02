# Portfolio_and_Chatbot
Ce projet est une application web déployée sur Microsoft Azure qui combine un portfolio personnel avec un chatbot intégré. Le chatbot est conçu pour répondre aux questions des utilisateurs en fonction des informations contenues dans le portfolio.

## Fonctionnalités
Portfolio personnel : Mes réalisations, projets, compétences et expériences professionnelles.
Chatbot intégré : Posez des questions sur le contenu du portfolio et obtenez des réponses pertinentes en temps réel.

## Déploiement
Ce projet utilise Azure DevOps pour la livraison continue (CI/CD). 

## Utilisation 
Pour faire fonctionner le code, il vaut remplacer vos 3 clef avec Azure : 
`AZURE_CREDENTIALS`
`REGISTRY_PASSWORD`
`AZURE_OPENAI_KEY`

## Arborescence du projet 

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

