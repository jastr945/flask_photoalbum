import React from 'react';
import Observer from '@researchgate/react-intersection-observer';

import Loading from './Loading';
import './ImageRow.css';

class ImageRow extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      start: 0,
      finish: null,
      slideslength: null,
      screenSize: window.innerWidth,
      fadedleft: true,
      fadedright: false,
      imgHovered: false,
      imgClicked: false,
      imgID: -1,
      visibility: null,
      albumClicked: -2
    }
    this.updateSize = this.updateSize.bind(this);
  }
  componentDidMount() {
    window.addEventListener("resize", this.updateSize);
    this.updateSize();
    setTimeout(() => this.setState({
      loading: false
    }), 1500);
  }
  componentWillUnmount() {
    window.removeEventListener("resize", this.updateSize);
  }
  updateSize() {
    this.setState({
      screenSize: window.innerWidth,
      fadedleft: true,
      fadedright: false,
      start: 0
    });
    if (this.state.screenSize > 1200) {
      this.setState({
        finish: 5,
        slideslength: 5,
      });
    } else if (this.state.screenSize < 1200 && this.state.screenSize > 1010) {
      this.setState({
        finish: 4,
        slideslength: 4
      });
    } else if (this.state.screenSize < 1010 && this.state.screenSize > 920) {
      this.setState({
        finish: 3,
        slideslength: 3
      });
    } else if (this.state.screenSize < 920 && this.state.screenSize > 590) {
      this.setState({
        finish: 2,
        slideslength: 2
      });
    } else {
      this.setState({
        finish: 1,
        slideslength: 1
      });
    }
  }
  imgHover(imgindex) {
  if (!this.state.imgClicked) {
      this.setState({
        imgID: imgindex,
        imgHovered: true
      });
    }
  }
  imgMouseLeave() {
    this.setState({
      imgHovered: false
    });
  }
  openImg(imgindex, albumIndex) {
    if (this.state.imgID === imgindex) {
      this.setState({
        imgClicked: true,
        imgHovered: false,
        albumClicked: albumIndex
      });
    }
  }
  closeImg() {
    this.setState({
      imgClicked: false,
      imgHovered: false,
      albumClicked: -1
    });
  }
  leftClick() {
    let start = this.state.start;
    let finish = this.state.finish;
    let slideslength = this.state.slideslength;
    if (start > 0 && finish > 0) {
      this.setState({
        start: start - slideslength,
        finish: finish - slideslength,
        fadedright: false
      });
    } else {
      this.setState({
        fadedleft: true
      });
    }
  }
  rightClick(length) {
    let start = this.state.start;
    let finish = this.state.finish;
    let slideslength = this.state.slideslength;
    if (finish < length) {
      this.setState({
        start: start + slideslength,
        finish: finish + slideslength,
        fadedleft: false
      });
    } else {
      this.setState({
        fadedright: true
      });
    }
  }
  handleIntersection(event) {
    this.setState({
      visibility: event.isIntersecting ? 'inview' : ''
    });
  };
  render() {
    const {start, finish, fadedleft, fadedright, imgHovered, imgID, imgClicked, albumClicked} = this.state
    const albumID = this.props.albumID;
    const albumIndex = this.props.albumkey;
    const albumHovered = this.props.albumHovered;
    const left = fadedleft ? "arrow-left col-md-1 text-center faded-left" : "arrow-left col-md-1 text-center";
    const right = fadedright ? "arrow-right col-md-1 text-center faded-right" : "arrow-right col-md-1 text-center";
    var length = this.props.albums[this.props.albumkey].images.length;
    // console.log("imgID: " + imgID, "albumID: " + albumID, "imgClicked: " + imgClicked, "imgHovered: " + imgHovered, "albumHovered: " + albumHovered);
    // console.log("albumID: " + albumID, "albumClicked: " + albumClicked, "imgClicked: " + imgClicked);
    var hiddenslides = imgClicked && albumID === albumClicked ? "open" : "hiddenslides";

    return (
      this.state.loading ? <Loading /> :
      <Observer onChange={this.handleIntersection.bind(this)}>
        <div className={`slideshow row ${this.state.visibility} ${hiddenslides}`}>
          <div className={left} onClick={this.leftClick.bind(this)}>
            <img src={require('./static/arrow-left.png')} width={50} alt="arrow" />
          </div>
          {
            this.props.albums[albumIndex].images.slice(start, finish).map((i, imgindex) => {
              var zoomedImg = imgHovered && albumHovered && imgID === imgindex && albumID === albumIndex ? "zoomed" : "";
              var openImg = imgClicked && imgID === imgindex ? "opened" : "";
              var imgClass = `imageContainer ${openImg} ${zoomedImg}`;
              return (
                <div className={imgClass} key={imgindex}>
                  {imgHovered && albumHovered && imgID === imgindex && albumID === albumIndex && <img className="expandicon" onClick={this.openImg.bind(this, imgindex, albumIndex)} onMouseEnter={this.imgHover.bind(this, imgindex)} src={require('./static/expand.png')} width={30} alt="expand" />}

                  {imgClicked && albumHovered && imgID === imgindex && albumID === albumIndex && <img className="closeicon" onClick={this.closeImg.bind(this)}  src="http://icons.iconarchive.com/icons/graphicloads/100-flat/256/close-icon.png" width={45} alt="close" />}

                  <img className="albumimage" onMouseEnter={this.imgHover.bind(this, imgindex)} onMouseLeave={this.imgMouseLeave.bind(this)} src={i} alt='album img' />
                </div>
              )
            })
          }
          <div className={right} onClick={this.rightClick.bind(this, length)}>
            <img src={require('./static/arrow-right.png')} width={50} alt="arrow" />
          </div>
        </div>
      </Observer>
    )
  }
}

export default ImageRow;
