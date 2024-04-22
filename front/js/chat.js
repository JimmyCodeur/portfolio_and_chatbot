const chatMessages = document.getElementById("chat-messages");

document.getElementById("chat-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const userInput = document.getElementById("user-input").value;
    const userMessage = `<div class="message user-message">${userInput}</div>`;
    chatMessages.innerHTML += userMessage;

    document.getElementById("user-input").value = "";

    try {
        console.log('Envoi de la requête à FastAPI...');
        const response = await fetch('http://127.0.0.1:8008/generate-text', {
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
