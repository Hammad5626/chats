document.querySelector('#roomname').focus();
        document.querySelector('#submit').onclick = function(e) {
            var myRoom = document.querySelector('#roomname').value;
            window.location.pathname = '/chats/' + myRoom + '/';
        };