document.addEventListener('DOMContentLoaded', () => {
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const chatBox = document.getElementById('chat-box');

    messageForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const userMessage = messageInput.value.trim();

        if (userMessage) {
            addMessage(userMessage, 'user');
            messageInput.value = '';
            // Simulate agent response
            setTimeout(() => {
                const agentResponse = getAgentResponse(userMessage);
                addMessage(agentResponse, 'agent');
            }, 500);
        }
    });

    function addMessage(text, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);
        messageElement.textContent = text;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function getAgentResponse(userMessage) {
        // Simple rule-based responses for simulation
        const lowerCaseMessage = userMessage.toLowerCase();
        if (lowerCaseMessage.includes('hello') || lowerCaseMessage.includes('hi')) {
            return 'Hello! How can I help you today?';
        } else if (lowerCaseMessage.includes('how are you')) {
            return 'I am just a bot, but I am doing great! Thanks for asking.';
        } else if (lowerCaseMessage.includes('help')) {
            return 'I can provide information and answer your questions. What do you need help with?';
        } else {
            return 'I am a simple agent. I can only respond to a few queries.';
        }
    }
});