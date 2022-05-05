import React from "react";
import axios from "axios";

import Players from "../components/Players";

class PlayersList extends React.Component {
  state = {
    players: [],
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:5000/api/players/").then((res) => {
      this.setState({
        players: res.data,
      });
      console.log(res);
    });
  }

  render() {
    return <Players data={this.state.players} />;
  }
}

export default PlayersList;
