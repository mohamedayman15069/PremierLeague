import React from "react";
import axios from "axios";
import { Card, Image, Row, Col } from "antd";
import { Link } from "react-router-dom";
import { Form, Input, Button, Radio } from "antd";

class TeamDetail extends React.Component {
  state = {
    teamInfo: {},
    impInfo: [],
    squadInfo: [],
    team_name: String,
  };
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
  }
  componentDidMount() {
    const teamName = this.props.match.params.TeamName;
    axios
      .get(`http://127.0.0.1:5000/api/teams/${teamName}`)
      .then((res) => {
        this.setState({
          teamInfo: res.data[0],
          impInfo: res.data,
          team_name: teamName,
        });
        // console.log(res.data)
      })
      .catch((error) => {
        console.log(error);
      });
  }

  handleClick(event) {
    let v = event.target.textContent.slice(7);
    const team = this.props.match.params.TeamName;
    axios
      .get(`http://127.0.0.1:5000/api/teams/${team}/${v}`)

      .then((res) => {
        this.setState({
          squadInfo: res.data,
        });
        console.log(this.state.squadInfo);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    var stadium = null;
    if(this.state.teamInfo.stadiumName != undefined)
      stadium = this.state.teamInfo.stadiumName.replace(" ","-");
    return (
      <Card title={this.state.teamInfo.clubName}>
        <Row>
          <Col span={15}>
            Club Website:{" "}
            <a href = {`https://${this.state.teamInfo.clubWebsite}`}>
              {this.state.teamInfo.clubWebsite}
            </a>

            <p> Stadium Name: {this.state.teamInfo.stadiumName}</p>
            <Link to={`/stadiums/${stadium}`}>
                                      <li>
                                      <Button>Click Here For More Info about Stadium</Button>
                                      </li>
                                    </Link>
          </Col>
        </Row>
        <p></p>
        <h2>Filter By Season to know the team Squad</h2>
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
        {this.state.squadInfo.map((player) => (
          <Card>
            <Row>
              <Col span={19}>
                <p>Player Name: {player.playerName}</p>
                <p>Date Of Birth: {player.dateOfBirth}</p>
              </Col>
            </Row>
          </Card>
        ))}{" "}
      </Card>
    );
  }
}

export default TeamDetail;
