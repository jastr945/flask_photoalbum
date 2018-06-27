import React, { Component } from 'react';
import axios from 'axios';
import { Navbar, Nav, NavItem } from 'react-bootstrap';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

import './Navbar.css';


class Header extends Component {
  constructor() {
    super()
    this.state = {
      useremail: null,
      userpic: null
    }
    this.responseGoogle = this.responseGoogle.bind(this);
    this.logout = this.logout.bind(this);
    this.getUsers = this.getUsers.bind(this);
  }
  componentDidMount() {
    this.getUsers();
  }
  getUsers() {
    axios.get('http://slider.mee.how:5000/googleauthorized')
    .then((res) => {
    this.setState({
      useremail: res.data.data.email,
      userpic: res.data.data.pic
    });
    this.checkLogin();
    this.props.callgetAlbums();
    })
    .catch((err) => { console.log(err); })
  }
  responseGoogle = (response) => {
    var accessCode = response.code;
    const config2 = {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Authorization',
        'Access-Control-Allow-Methods': 'POST',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + accessCode,
        'mode': 'no-cors'
      }
    }
    axios.post('http://slider.mee.how:5000/google', config2)
    .then((res) => {
      console.log('Access code sent.');
      this.getUsers();
      console.log("Login successful.");
    })
    .catch((err) => {
      console.log(err);
    });
  }
  logout = () => {
    axios.get('http://slider.mee.how:5000/googlelogout')
    .then((res) => {
      this.setState({
        useremail: null,
        userpic: null
      });
      this.getUsers();
      console.log("Logout successful.")
    })
    .catch((err) => {
      console.log(err);
    });
  }
  checkLogin() {
    if (this.state.useremail === null || this.state.useremail === '') {
      this.props.loginError(true);
    } else {
      this.props.loginError(false);
    }
  }
  render() {
    console.log(this.state.useremail);
    return (
      <Navbar inverse fluid className="navbar" toggleable="lg">
        <Navbar.Header>
          <Navbar.Brand className="navbar-brand">
            <a href={process.env.REACT_APP_REDIRECT_URI}>React + Flask Photo Album</a>
          </Navbar.Brand>
          <Navbar.Toggle />
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav pullRight>
            <NavItem eventKey={1} href="https://github.com/jastr945/flask_photoalbum" target="_blank" rel="noopener noreferrer">About</NavItem>
            <NavItem eventKey={2} href="http://polina.mee.how/" target="_blank" rel="noopener noreferrer">Contact</NavItem>
            {!this.state.useremail &&
            <GoogleLogin
              className="googleButton"
              clientId={process.env.REACT_APP_CLIENT_ID}
              buttonText="Login with Google"
              onSuccess={this.responseGoogle}
              onFailure={this.responseGoogle}
              offline={true}
              responseType="code"
              prompt="consent"
              isSignedIn
              style={{}}
            />}
            {this.state.useremail && <li className="userinfo">{this.state.useremail} | <img src={this.state.userpic} alt="userpic" height="35px" width="35px"/></li>}
            {this.state.useremail &&
              <li><GoogleLogout className="googleButton" buttonText="Logout" onLogoutSuccess={this.logout} style={{}}/></li>}
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}

export default Header;
