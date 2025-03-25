document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('userInput');
    const submitButton = document.getElementById('submitButton');
    const chatConversation = document.getElementById('chat-conversation');

    submitButton.addEventListener('click', async () => {
        const inputText = userInput.value;
        if (!inputText.trim()) return;

        // Display user message
        displayMessage(inputText, 'user-message');

        const response = await fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: inputText }),
        });

        const data = await response.json();
        // Wrap code in <pre> and <code> tags
        const formattedCode = `<pre><code>${data.result}</code></pre>`;
        displayMessage(formattedCode, 'bot-message');

        userInput.value = ''; // Clear input
    });

    function displayMessage(text, className) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', className);
        messageDiv.innerHTML = text;
        chatConversation.appendChild(messageDiv);
        chatConversation.scrollTop = chatConversation.scrollHeight; // Scroll to bottom
    }
});