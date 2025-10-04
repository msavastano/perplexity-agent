document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    const converter = new showdown.Converter();

    function addMessage(message, sender) {
        const messageElement = document.createElement("div");
        messageElement.classList.add(sender === "user" ? "user-message" : "agent-message");

        if (sender === 'agent') {
            messageElement.innerHTML = converter.makeHtml(message);
        } else {
            messageElement.innerText = message;
        }

        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const message = userInput.value;
        if (message.trim() === "") return;

        addMessage(message, "user");
        userInput.value = "";

        const agentMessageElement = document.createElement("div");
        agentMessageElement.classList.add("agent-message");
        agentMessageElement.innerHTML = "<i>Thinking...</i>";
        chatBox.appendChild(agentMessageElement);
        chatBox.scrollTop = chatBox.scrollHeight;

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            agentMessageElement.innerHTML = converter.makeHtml(data.reply);

        } catch (error) {
            console.error("Error sending message:", error);
            agentMessageElement.innerText = "Sorry, something went wrong. Please try again.";
        } finally {
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", (event) => {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});