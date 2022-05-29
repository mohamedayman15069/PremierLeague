import React from "react";
import axios from "axios";

import Teams from "../components/Teams";

class TeamList extends React.Component {
  state = {
    teams: [],
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:5000/api/teams/").then((res) => {
      this.setState({
        teams: res.data,
      });
    });
  }

  render() {
    return <Teams data={this.state.teams} />;
  }
}

export default TeamList;
