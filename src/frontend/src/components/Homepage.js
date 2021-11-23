import React, { useEffect, useState } from "react"

export default function Homepage(props) {

    const [items, setItems] = useState(undefined)

    useEffect(() => {
        setInterval(() => {
            fetch('/getMessages/')
                .then(response => response.json())
                .then(dictionary => {
                    var newItems = dictionary['items']
                    var messageDiv = document.getElementById('messages')
                    if (messageDiv.childNodes.length != newItems.length) {
                        setItems(newItems)
                        messageDiv.scrollTop = messageDiv.scrollHeight
                    }
                })
        }, 1000)
    }, [])

    function sendMessage(e) {
        e.preventDefault()
        var message = document.getElementById('messageInput').value

        fetch('/sendMessage/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('token')}`,
                'X-CSRFToken': props.getCookie('csrftoken')
            },
            body: JSON.stringify({ text: message })
        })
            .then(response => response.json())
            .then(json => {
                document.getElementById('messageInput').value = ''
                if (json.detail) {
                    document.getElementById('error').innerHTML = "Please Log In"
                }
            })
    }

    return (
        <>
            <h3>
                {props.loggedIn
                    ? `Hello, ${props.username}`
                    : 'Not logged in'}
            </h3>
            <div id="messages">
                {items
                    ? items.map((item, key) => {
                        return (
                            <div className={'message ' + (item.owner === props.username ? "user" : '')}>
                                <p className='message-user'>{item.owner}</p>
                                <p className='message-text'>{item.text}</p>
                            </div>
                        )
                    })
                    : null
                }
            </div>
            <form onSubmit={(e) => sendMessage(e)}>
                <input type='text' id='messageInput' style={{ width: '200px' }} />
                <input type="submit" value="Send" name="send" id="name" />
            </form>
            <p id='error'></p>
        </>
    )
}