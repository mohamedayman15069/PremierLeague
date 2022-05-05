import React from "react";
import axios from "axios";

import Stadiums from "../components/Stadiums";

class StadiumList extends React.Component {
  state = {
    stadiums: [],
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:5000/api/stadium/").then((res) => {
      this.setState({
        stadiums: res.data,
      });
    });
  }

  render() {
    return <Stadiums data={this.state.stadiums} />;
  }
}

export default StadiumList;
