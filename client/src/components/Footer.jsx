import React from 'react';

import './Footer.css';

const Footer = (props) => {
  return (
    <footer>
      <div className="footer container">
        <ul>
          <li><a href={process.env.REACT_APP_REDIRECT_URI} target="_blank" rel="noopener noreferrer">photo album</a></li>
          <li><a href="https://github.com/jastr945/flask_photoalbum" target="_blank" rel="noopener noreferrer">about</a></li>
          <li><a href="http://polina.mee.how/" target="_blank" rel="noopener noreferrer">contact</a></li>
        </ul>
      </div>
      <small>&copy;
        {(new Date().getFullYear())}
        &nbsp;Polina Jastrzebska; Icons made by <a href="http://www.freepik.com" title="Freepik" target="_blank" rel="noopener noreferrer">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon" target="_blank" rel="noopener noreferrer">www.flaticon.com</a> are licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank" rel="noopener noreferrer">CC 3.0 BY</a>; headline photo by Annie Spratt</small>
    </footer>
  )
}

export default Footer;
