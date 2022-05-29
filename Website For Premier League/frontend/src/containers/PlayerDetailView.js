import React from "react";
import axios from "axios";

import { Card, Image, Row, Col } from "antd";
import { Link } from "react-router-dom";

class playerDetail extends React.Component {
  state = {
    importantInfo: [],
    playerInfo: [],
  };

  componentDidMount() {
    const playerName = this.props.match.params.playerName;
    axios
      .get(`http://127.0.0.1:5000/api/players/${playerName}/`)
      .then((res) => {
        this.setState({
          importantInfo: res.data,
          playerInfo: res.data[0],
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    console.log("data", this.state.playerInfo);
    return (
      <Card title={this.state.playerInfo.playerName}>
        <Row>
          <Col span={15}>
            <p>Birthdate: {this.state.playerInfo.dateOfBirth}</p>
            <p>Nationatlity: {this.state.playerInfo.nationality}</p>

            {this.state.playerInfo.Weight != null ? (
              <p>Weight: {this.state.playerInfo.Weight}</p>
            ) : (
              ""
            )}
            {this.state.playerInfo.height != null ? (
              <p>height: {this.state.playerInfo.height}</p>
            ) : (
              ""
            )}
          </Col>
        </Row>
        {this.state.importantInfo.map((player) => (
          <Card>
            <Row>
              <Col span={19}>
                <p>season: {player.season}</p>
                <p>position: {player.position}</p>
                <p>clubName: {player.clubName}</p>
              </Col>
            </Row>
          </Card>
        ))}{" "}
      </Card>
    );
  }
}

export default playerDetail;
