import React from "react";
import axios from "axios";
import { Card, Image, Row, Col } from "antd";
import { Button, form } from "antd";

class WinTeam extends React.Component {
  state = {
    teamInfo: [],
    team_name: String,
  };
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(event) {
    let v = event.target.textContent.slice(7);
    axios
      .get(`http://127.0.0.1:5000/api/toptenteamsbyseason/${v}`)

      .then((res) => {
        this.setState({
          teamInfo: res.data,
        });
        console.log(this.state.teamInfo);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    return (
      <>
        <h2>Filter By Season to know the winning teams</h2>
        <form onClick={this.handleClick}>
          <Button class="1" variant="outline-primary">
            Season 2021-22
          </Button>{" "}
          <Button class="2" variant="outline-secondary">
            Season 2020-21
          </Button>{" "}
          <Button class="3" variant="outline-success">
            Season 2019-20
          </Button>{" "}
          <Button class="4" variant="outline-warning">
            Season 2018-19
          </Button>{" "}
        </form>

        {this.state.teamInfo.map((player) => (
          <Card>
            <Row>
              <Col span={19}>
                <p>Club Name: {player.ClubName}</p>
                <p>Score    :  {player.WIN}</p>
              </Col>
            </Row>
          </Card>
        ))}
      </>
    );
  }
}

export default WinTeam;
