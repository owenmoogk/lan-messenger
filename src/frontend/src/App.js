import React, { useEffect, useState } from 'react';
import Nav from './components/Nav';
import Login from './components/accounts/Login';
import Signup from './components/accounts/Signup';
import {
	BrowserRouter as Router,
	Switch,
	Route
} from 'react-router-dom'
import Homepage from './components/Homepage'

export default function App(props) {

	const [username, setUsername] = useState()
	const [loggedIn, setLoggedIn] = useState(localStorage.getItem('token') ? true : false)

	function handleLogout() {
		localStorage.removeItem('token');
		setLoggedIn(false)
		setUsername('')
	};

	useEffect(() => {
		if (loggedIn) {
			fetch('/users/current_user/', {
				headers: {
					Authorization: `JWT ${localStorage.getItem('token')}`
				}
			})
				.then(response => response.json())
				.then(json => {
					if (json.username){
						setUsername(json.username)
					}
					else{
						handleLogout()
					}
				});
		}
	})

	function getCookie(name) {
		if (!document.cookie) {
			return null;
		}
	
		const xsrfCookies = document.cookie.split(';')
			.map(c => c.trim())
			.filter(c => c.startsWith(name + '='));
	
		if (xsrfCookies.length === 0) {
			return null;
		}
		return decodeURIComponent(xsrfCookies[0].split('=')[1]);
	}

	return (

		<Router>
			<Nav
				loggedIn={loggedIn}
				handleLogout={handleLogout}
			/>
			<Switch>
				<Route path="/login">
					<Login setLoggedIn={setLoggedIn} setUsername={setUsername} />
				</Route>
				<Route path="/signup">
					<Signup setLoggedIn={setLoggedIn} setUsername={setUsername} />
				</Route>
				<Route exact path=''>
					<Homepage username={username} loggedIn={loggedIn} getCookie={getCookie}/>
				</Route>
			</Switch>
		</Router>
	);
}