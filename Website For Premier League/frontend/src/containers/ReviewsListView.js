import React from "react";
import axios from "axios";

import Reviews from "../components/Review";

class ReviewsList extends React.Component {
  state = {
    reviews: [],
  };

  componentDidMount() {
    const season = this.props.match.params.season;
    const homeClubName = this.props.match.params.homeClubName;
    const awayClubName = this.props.match.params.awayClubName;

    axios
      .get(
        `http://127.0.0.1:5000/api/matches/${season}/${homeClubName}/${awayClubName}/allreview/`
      )
      .then((res) => {
        this.setState({
          reviews: res.data,
        });
        console.log(res);
      });
  }

  render() {
    return <Reviews data={this.state.reviews} />;
  }
}

export default ReviewsList;
