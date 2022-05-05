import React from "react";
import axios from "axios";
import { Card, Image, Row, Col } from "antd";
import { Link } from "react-router-dom";
import { Form, Input, Button, Radio } from "antd";
import * as table from "../components/Menu";

class TopTen extends React.Component {
  state = {
    Info: [],
    mapper: {
      "Top Ten Teams By Match": "toptenteams",
      "Top Ten Teams By Home Match": "toptenteamsbyhome",
      "Top Ten Teams By yellow Cards": "toptenteamswithyellowcards",
      "Top Ten Teams By Fouls": "toptenteamsbyfouls",
      "Top Ten Teams By Shots": "toptenteamsbyshots",
    },
    counter: 0,

   
  };
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(event) {
    let v = this.state.mapper[event.target.textContent];
    console.log(v);
    axios
      .get(`http://127.0.0.1:5000/api/${v}`)

      .then((res) => {
        this.setState({
          Info: res.data,
          Value: event.target.textContent,
        });
        console.log(this.state.Info);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    let rowCounter = 0;
    return (
      <>
        <Row>
          <h2>Over All Seasons, Top Ten Teams By</h2>
          <form onClick={this.handleClick}>
            <Button class="1" variant="outline-primary">
              Top Ten Teams By Match
            </Button>{" "}
            <Button class="2" variant="outline-secondary">
              Top Ten Teams By Home Match
            </Button>{" "}
            <Button class="3" variant="outline-success">
              Top Ten Teams By yellow Cards
            </Button>{" "}
            <Button class="4" variant="outline-warning">
              Top Ten Teams By Fouls
            </Button>{" "}
            <Button class="5" variant="outline-warning">
              Top Ten Teams By Shots
            </Button>{" "}
          </form>
        </Row>
        <Card>
          {this.state.Info.map((player) => (
            <Card>
              <Row>
                <Col span={19}>
                  <p>
                    {player.ClubName}<p>    </p>{player['Score']}
                    
                  </p>
                </Col>
              </Row>
            </Card>
          ))}
        </Card>
      </>
    );
  }
}

export default TopTen;
