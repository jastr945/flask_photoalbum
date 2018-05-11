import React from 'react';

import Loading from './Loading';
import './AlbumsList.css';
import ImageRow from './ImageRow';


const Timestamp = require('react-timestamp');

class AlbumsList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      albumID: -1,
      albumHovered: false
    }
  }
  componentDidMount() {
    this.setState({
      loading: false
    });
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
  render() {
    return (
      this.state.loading ? <Loading /> :
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
    )
  }
};

export default AlbumsList;
