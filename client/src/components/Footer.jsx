import React from 'react';

import './Footer.css';

const Footer = (props) => {
  return (
    <footer>
      <div className="footer container">
        <ul>
          <li><a href="#">photo album</a></li>
          <li><a href="#">about</a></li>
          <li><a href="#">contact</a></li>
        </ul>
      </div>
      <small>&copy;
        {(new Date().getFullYear())}
        &nbsp;Polina Jastrzebska; Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> are licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a>; headline photo by Annie Spratt</small>
    </footer>
  )
}

export default Footer;
