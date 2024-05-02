const chatMessages = document.getElementById("chat-messages");

document.getElementById("chat-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const userInput = document.getElementById("user-input").value;
    const userMessage = `<div class="message user-message">${userInput}</div>`;
    chatMessages.innerHTML += userMessage;

    document.getElementById("user-input").value = "";

    try {
        console.log('Envoi de la requête à FastAPI...');
        const response = await fetch('http://localhost:8008/generate-text', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                "history": [{"sender": "user", "message": userInput}] 
            })
        });
        console.log('Réponse de FastAPI reçue:', response);

        if (!response.ok) {
            throw new Error('Request failed');
        }

        const responseData = await response.json();

        const assistantMessage = `<div class="message bot-message">${responseData.response}</div>`;
        chatMessages.innerHTML += assistantMessage;

        chatMessages.scrollTop = chatMessages.scrollHeight;
    } catch (error) {
        console.error('Erreur:', error);
        const errorMessage = `<div class="message error-message">Une erreur s'est produite. Veuillez réessayer.</div>`;
        chatMessages.innerHTML += errorMessage;
    }
});

document.getElementById("feedback-button").addEventListener("click", async function(event) {
    event.preventDefault();

    const lastUserMessage = document.querySelector(".user-message:last-child").textContent;
    const lastAssistantMessage = document.querySelector(".bot-message:last-child").textContent;

    try {
        console.log('Envoi du feedback à FastAPI...');
        const response = await fetch('http://localhost:8008/feedback', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                "comment": "Votre commentaire ici",
                "question": lastUserMessage,
                "response": lastAssistantMessage
            })
        });
        console.log('Réponse de FastAPI reçue:', response);

        if (!response.ok) {
            throw new Error('Request failed');
        }

        const feedbackSuccessMessage = document.createElement("div");
        feedbackSuccessMessage.textContent = "Feedback envoyé avec succès !";
        feedbackSuccessMessage.style.color = "green";
        document.body.appendChild(feedbackSuccessMessage);

    } catch (error) {
        console.error('Erreur:', error);
        const feedbackErrorMessage = document.createElement("div");
        feedbackErrorMessage.textContent = "Une erreur s'est produite lors de l'envoi du feedback. Veuillez réessayer.";
        feedbackErrorMessage.style.color = "red";
        document.body.appendChild(feedbackErrorMessage);
    }
});
