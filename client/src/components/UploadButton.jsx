import React from 'react';

import './UploadButton.css';

const UploadButton = (props) => {
  return (
    <button className="formOpener" onClick={props.openForm}>Upload Images</button>
  );
}

export default UploadButton;
