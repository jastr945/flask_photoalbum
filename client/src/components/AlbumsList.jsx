import React from 'react';
import axios from 'axios';

import './AlbumsList.css';
import ImageRow from './ImageRow';


const Timestamp = require('react-timestamp');

class AlbumsList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      albumID: -1,
      albumHovered: false
    }
  }
  albumHover(albumindex) {
    this.setState({
      albumID: albumindex,
      albumHovered: true
    });
  }
  albumMouseLeave() {
    this.setState({
      albumHovered: false
    });
  }
  handleDelete(title) {
    if (window.confirm('Are you sure you wish to delete this album?')) {
      var url = 'http://slider.mee.how:5001/albums/' + title;
      console.log(url);
      axios.delete(url)
      .then((res) => { console.log(res); })
      .catch((err) => { console.log(err); })
    }
  }
  render() {
    return (
      <div>
      {this.props.albums.length === 0 ? <div className="empty">You have no galleries yet.</div> :
      <div className="container albumSpace">
        {
          this.props.albums.map((album, albumindex) => {
            return (
                <div
                  onMouseEnter={this.albumHover.bind(this, albumindex)}
                  onMouseLeave={this.albumMouseLeave.bind(this)}
                  className="album"
                  key={albumindex}
                >
                  <div className="header row">
                    <h2>{album.title}</h2>
                    <h6>{album.images.length} files - <Timestamp time={album.created_at} format='full' /> - <i><Timestamp time={album.created_at} format='ago' includeDay={true} precision={2} autoUpdate={60} /></i></h6>
                    <h5>{album.description}</h5>
                    <h6 className="delete" onClick={this.handleDelete.bind(this, album.title)}><u>delete</u></h6>
                  </div>
                  <ImageRow
                  albums={this.props.albums}
                  albumID={this.state.albumID}
                  albumHovered={this.state.albumHovered}
                  albumkey={albumindex}
                  />
              </div>
            )
          })
        }
      </div>
      }
      </div>
    )
  }
};

export default AlbumsList;
