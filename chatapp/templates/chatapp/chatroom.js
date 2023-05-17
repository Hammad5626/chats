const roomName = JSON.parse(document.getElementById('roomname').textContent);
        const chatSocket = new WebSocket(
            `ws://${window.location.host}/ws/chat/${roomName}/`
        );
        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            document.querySelector('#log').value += `${data.message}\n`;
        };
        chatSocket.onclose = function(e) {
            console.error('Oops! Chats closed.');
        };
        document.querySelector('#chatmssg').focus();
        document.querySelector('#submit').onclick = function(e) {
            const messageDom = document.querySelector('#chatmssg');
            const message = messageDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageDom.value = '';
        };