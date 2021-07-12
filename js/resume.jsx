import React from 'react';
import PropTypes from 'prop-types';
import ReactDOM from 'react-dom';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import ListSubheader from '@material-ui/core/ListSubheader';
import Card from './cards.jsx';

class Resume extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      width: window.innerWidth,
      size: window.innerWidth < 768,
      talents: ['development', 'education', 'projects', 'work'],
      style: { height: '100% !important'}
    };
  };

  componentDidMount() {
  }

  render() {
    return (
      <div className='resume'>
        <GridList cellHeight={this.state.size ? this.state.width : this.state.width/2} cols={(this.state.size) ? 2 : 4}>
          <GridListTile cols={1} className='d-none d-md-inline'>
          </GridListTile>
          <GridListTile key='image' cols={2}>
            <img src="static/img/Jonathan.jpg" alt="Picture of Me"/>
            <GridListTileBar
              title='Jonathan Silverstein'
              subtitle='Full Stack Web Developer and Machine Learning Engineer'
            />
          </GridListTile>
          <GridListTile cols={1} className='d-none d-md-inline'>
          </GridListTile>
        </GridList>
        <GridList className='talents' cols={(this.state.size) ? 2 : 4}>
          <GridListTile style={this.state.style} id='work' key='Work' cols={2}>
            <div className='cards-list shadow m-2'>
              <Card url='/cards/work'/>
            </div>
          </GridListTile>
          <GridListTile style={this.state.style} id='development' key='Development' cols={2}>
            <div className='cards-list shadow m-2'>
              <Card url='/cards/development'/>
            </div>
          </GridListTile>
          <GridListTile style={this.state.style} id='education' key='Education' cols={2}>
            <div className='cards-list shadow m-2'>
              <Card url='/cards/education'/>
            </div>
          </GridListTile>
          <GridListTile style={this.state.style} id='projects' key='Projects' cols={2}>
            <div className='cards-list shadow m-2'>
              <Card url='/cards/projects'/>
            </div>
          </GridListTile>
        </GridList>
      </div>
    );
  }
}
const Res = document.getElementById('resume')
if (Res) {
  ReactDOM.render(<Resume/>, Res)
}
