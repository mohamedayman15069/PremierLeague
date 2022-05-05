import React from "react";
import axios from "axios";

import Matches from "../components/Matches";

class MatchList extends React.Component {
  state = {
    matches: [],
  };

  componentDidMount() {
    axios
      .get("http://127.0.0.1:5000/api/matches/")
      .then((res) => {
        this.setState({
          matches: res.data,
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    return <Matches data={this.state.matches} />;
  }
}

export default MatchList;
