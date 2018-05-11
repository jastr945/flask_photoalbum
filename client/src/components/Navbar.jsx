import React, { Component } from 'react';
import axios from 'axios';
import { Navbar, Nav, NavItem } from 'react-bootstrap';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

import './Navbar.css';


class Header extends Component  {
  constructor() {
    super()
    this.state = {
      useremail: null,
      userpic: null
    }
    this.responseGoogle = this.responseGoogle.bind(this);
    this.logout = this.logout.bind(this);
  }
  getUsers() {
    axios.get('http://slider.mee.how:5001/login/authorized')
    .then((res) => {
    this.setState({ albums: res.data });
    console.log('user info called');
     })
    .catch((err) => { console.log(err); })
  }
  responseGoogle = (response) => {
    console.log("login", response);
    var accessCode = response.code;
    const config2 = {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + accessCode,
        'mode': 'no-cors'
      }
    }
    console.log(config2);
    axios.post('http://slider.mee.how:5001/login/authorized', config2)
    .then((res) => {
      console.log('access code sent');
    })
    .catch((err) => {
      console.log(err);
    });
    this.getUsers();
  }
  logout = () => {
    console.log('logout');
    this.setState({
      useremail: null,
      userpic: null
    });
  }
  render() {
    return (
      <Navbar inverse fluid className="navbar">
        <Navbar.Header>
          <Navbar.Brand className="navbar-brand">
            <a href="#">React + Flask Photo Album</a>
          </Navbar.Brand>
          <Navbar.Toggle />
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav pullRight>
            <NavItem eventKey={1} href="https://github.com/jastr945" target="_blank">About</NavItem>
            <NavItem eventKey={2} href="http://polina.mee.how/" target="_blank">Contact</NavItem>
            {!this.state.useremail && <NavItem eventKey={3}>
            <GoogleLogin
              clientId="418257197191-75oafj28gkn84pj7ebgvt54av0vtt7br.apps.googleusercontent.com"
              buttonText="Login"
              onSuccess={this.responseGoogle}
              onFailure={this.responseGoogle}
              offline={true}
              approvalPrompt="force"
              responseType="code"
              prompt="consent"
              isSignedIn
            />
            </NavItem>}
            {this.state.useremail && <NavItem>{this.state.useremail} | <img src={this.state.userpic} height="22px" width="22px"/></NavItem>}
            {this.state.useremail &&
              <GoogleLogout buttonText="Logout" onLogoutSuccess={this.logout} />}
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}

export default Header;
