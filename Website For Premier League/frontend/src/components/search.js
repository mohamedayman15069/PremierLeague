import React from "react";
import "reactjs-popup/dist/index.css";
import axios from "axios";
import {Button,Card ,Image, Row, Col, Alert } from "antd";
// import { useNavigate } from 'react-router-dom';

import { Container } from "./popup/Container";
import { Container2 } from "./popup2/Container";
import { Container3 } from "./popup3/Container";
import { Container4 } from "./popup4/Container";
import { Container5 } from "./popup5/Container";
import { Container6 } from "./popup6/Container";
import { BrowserRouter as Router, Link, Route } from "react-router-dom";



const triggerText = "Getting Players Info from Nationality";
const triggerText1 = "Getting Players Info by First and Last Name";
const triggerText2 = "Getting Home Team Name from Stadium";
const triggerText3 = "Getting players in a cetrain Position";
const triggerText4 = "Getting Team Names in a specific City";
const triggerText5 = "Getting All Reviews in a given Match";
class GoogleSearch extends React.Component {
  state = {
    
    whichRendering: "",
     whichButton : 0, 
    playersInfo : [], 
    oneinfo:{},
    homeTeam: {},
    teams :[], 
    isSubmit6 : false, 
    season : "", 
    hometeam : "",
    awayteam : ""

  };

  onClose = () => {
    this.setState({ isShown: false });
  };

  onSubmit = (onClose)=>(event) => {
    event.preventDefault(event);
    console.log(event.target.name.value);
  
    var v = event.target.textContent;
    console.log(v);
    this.state.whichButton = 1;
    axios.post(`http://127.0.0.1:5000/api/players/`,
    {
      "nationality": event.target.name.value
    }).then(res => {
        this.setState({
          playersInfo: res.data,
        })
        console.log(this.state.playersInfo)

        if(this.state.playersInfo.length == 0)
          alert("Something Wrong")
    })
    .catch(error => {
        console.log(error)
        alert("Something Wrong")

    });
    onClose();

  };

  onSubmit1 = (onClose)=>(event) => {
    event.preventDefault(event);
    this.state.whichButton = 2;

    console.log(event.target.name1.value);
    console.log(event.target.name2.value);

    axios.post(`http://127.0.0.1:5000/api/playerInfoFromName/`,
    {
      "firstName": event.target.name1.value,
      "lastName": event.target.name2.value
    }).then(res => {
        this.setState({
          playersInfo: res.data,
          oneinfo:res.data[0]

        }

        )
        window.location.replace(`/players/${this.state.oneinfo.playerName.replace(" ", ".")}`)

        console.log(this.state.oneinfo.playerName.replace(" ", "."))
    })
    .catch(error => {
        console.log(error)
        alert("This Name does not exist in Premier League!");

    });
    onClose();

  };


  onSubmit2 = (onClose)=>(event) => {
    this.state.whichButton = 3;

    event.preventDefault(event);
    console.log(event.target.stadium.value);
    axios.post(`http://127.0.0.1:5000/api/stadium/`,
    {
      "stadium": event.target.stadium.value

    }).then(res => {
        this.setState({
          homeTeam: res.data[0],
        })
        console.log(this.state.homeTeam)
        if(this.state.homeTeam == undefined)
          alert("You wrote the Name of Stadium Wrong!")
        else 
        window.location.replace(`/teams/${this.state.homeTeam.clubName.replace(" ", "-")}`)

    })
    .catch(error => {
        console.log(error)
    });
    onClose();
  };

  onSubmit3 = (onClose)=>(event) => {
    this.state.whichButton = 4;

    event.preventDefault(event);
    console.log(event.target.position.value);

    axios.post(`http://127.0.0.1:5000/api/positions/`,
    {
      "position": event.target.position.value

    }).then(res => {
        this.setState({
          playersInfo: res.data,
        })
        console.log(this.state.playersInfo)

        if(this.state.playersInfo.length == 0)
          alert("Keep in Mind that Premier League website classifies players in 4 categories: GoalKeeper, Defender, Midfielder, and Forward");
    })
    .catch(error => {
        console.log(error)
    });
    onClose();

  };


  onSubmit4 = (onClose)=>(event) => {
    this.state.whichButton = 5;

    event.preventDefault(event);
    console.log(event.target.city.value);

    axios.post(`http://127.0.0.1:5000/api/teamcity/`,
    {
      "city": event.target.city.value

    }).then(res => {
        this.setState({
          teams: res.data,
        })
        console.log(this.state.teams)
        if(this.state.teams.length == 0)
        {
          alert("There are no teams in this City");
        }
    })
    .catch(error => {
        console.log(error)
    });
    onClose();

  };

  onSubmit5 = (onClose)=>(event) => {
    this.state.whichButton = 6;
    this.state.hometeam = event.target.hometeam.value;
    this.state.awayteam = event.target.awayteam.value;
    this.state.season   = event.target.season.value;
    this.state.isSubmit6 = true; 

    event.preventDefault(event);
    console.log(event.target.hometeam.value);
    console.log(event.target.awayteam.value);
    console.log(event.target.season.value);
  
    // const navigate = useNavigate();
    // navigate('/matches/${this.state.season.replace("/","-")}/${this.state.hometeam.replace(" ", "-")}/${this.state.awayteam.replace(" ", "-")}');

    // return (
      
    // );
    axios.post(`http://127.0.0.1:5000/api/getmatchreview/`,
    {
      "homeTeam": event.target.hometeam.value,
      "awayTeam": event.target.awayteam.value,
      "season": event.target.season.value

    }).then(res => {
        this.setState({
          oneinfo: res.data,
        })
        console.log(this.state.oneinfo)

        if((this.state.oneinfo.length) == 0)
          alert("This match does not have any review!")
        else 
          window.location.replace(`/matches/${this.state.season.replace("/", "-")}/${this.state.hometeam.replace("/", "-")}/${this.state.awayteam.replace("/", "-")}`)

    })
    .catch(error => {
      alert("This match does not have any review");

        console.log(error)
    });
    onClose();
  };


  render() {
    var renderit = null;
     if(this.state.whichButton == 1 || this.state.whichButton == 4)
     {
      renderit =   
      
      this.state.playersInfo.map((player) => (
                              <Card>
                                <Row>
                                  <Col span={19}>
                                    <Link to={`/players/${player.playerName.replace(" ",".")}`}>
                                      <li>
                                      <li>{player.playerName}</li>
                                      </li>
                                    </Link>

                                  </Col>
                                </Row>
                              </Card>))

    this.state.whichButton = 0;
    }
    // else if( this.state.whichButton == 2)
    // {
      
    
    // if(this.state.oneinfo != undefined)
    // {

    //     renderit = 
    //     <Card>  
    //             <Card>
    //             <Col span={19}>
    //                         <p>Player Name: {this.state.oneinfo.playerName}</p>
    //                         <p>Date Of Birth: {this.state.oneinfo.dateOfBirth}</p>
    //                         {this.state.oneinfo.weight != null ? (
    //                           <p>Weight: {this.state.oneinfo.weight}</p>
    //                         ) : (
    //                           ""
    //                         )}

    //                         {this.state.oneinfo.height != null ? (
    //                           <p>height: {this.state.oneinfo.height}</p>
    //                         ) : (
    //                           ""
    //                         )}
    //                         </Col>

    //                       </Card>
    //       {this.state.playersInfo.map((player) => (
    //                         <Card>
    //                           <Row>
    //                               <Col>
    //                               <p>Season: {player.season}</p>
    //                               <p>Position: {player.position}</p>
    //                               <p>clubName: {player.clubName}</p>

    //                             </Col>
    //                           </Row>
    //                         </Card>))
    //   }
    //                       </Card>
    // }

    // this.state.whichButton = 0;
                          
    // }
    else if(this.state.whichButton ==3)
    { 
      if(this.state.homeTeam != undefined)
      {
          renderit = <Card>
                  <Col span={19}>
                      <p>Club Name: {this.state.homeTeam.clubName}</p>
                      </Col>
                      </Card>
      }
        this.state.whichButton = 0;
    }

    else if(this.state.whichButton == 4)
    {
      renderit=   this.state.playersInfo.map((player) => (
              <Card>
                <Row>
                  <Col span={19}>
                    <p>Player Name: {player.playerName}</p>
                    <p>Date Of Birth: {player.dateOfBirth}</p>
                    {player.weight != null ? (
                      <p>Weight: {player.weight}</p>
                    ) : (
                      ""
                    )}

                    {player.height != null ? (
                      <p>height: {player.height}</p>
                    ) : (
                      ""
                    )}
                  </Col>
                </Row>
              </Card>))
    }
    else if(this.state.whichButton == 5)
    {
      renderit =  this.state.teams.map((team) => (
                <Card>
                  <Row>
                    <Col span={19}>
                     <p>Team Name: {team.clubName}</p>

                    </Col>
                  </Row>
                </Card>))
    }
    else if(this.state.whichButton == 6)
    {

      renderit = 
            this.state.oneinfo.map((matchreview) => (
              <Card>
                    <Row>
                      <Col span={19}>

                        <p>User Email :{matchreview.userEmail}</p>
                        <p>match Season: {matchreview.matchSeason}</p>
                        <p>Home Team: {matchreview.homeClubName}</p>
                        <p>Away Team: {matchreview.awayClubName}</p>
                        <p>rating   : {matchreview.rating}</p>
                        <p>text Review: {matchreview.textReview}</p>
                      </Col>
                    </Row>
                  </Card>
            )); 

    }

   


    return (
      <Card>
        <h2>What do you need to search for?</h2>

        <Container triggerText={triggerText} onSubmit={this.onSubmit} />
        <Container2 triggerText={triggerText1} onSubmit={this.onSubmit1} />
        <Container3 triggerText={triggerText2} onSubmit={this.onSubmit2} />
        <Container4 triggerText={triggerText3} onSubmit={this.onSubmit3} />
        <Container5 triggerText={triggerText4} onSubmit={this.onSubmit4} />
        <Container6 triggerText={triggerText5} onSubmit={this.onSubmit5} />
        
        
        <div>{renderit}</div>

      {this.state.isSubmit6 == true ?
        <Link to={`/matches/${this.state.season.replace("/","-")}/${this.state.hometeam.replace(" ", "-")}/${this.state.awayteam.replace(" ", "-")}/`}>
               <Card>
               <Button>Click Here If you want to Add Review</Button>
               </Card>
        </Link>

        :
        null          
      } 


          
      </Card>
    );
  }
}

export default GoogleSearch;
