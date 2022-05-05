import React from "react";
import axios from "axios";
import { Card, Image, Row, Col, Radio, Input } from "antd";
import { Link } from "react-router-dom";

const { TextArea } = Input;

function ReviewsList(props) {
  const reviews = props.reviews;
  //console.log(genres)
  const listItems = reviews.map((review) => (
    <li>
      <p>
        {review.homeClubName} VS {review.awayClubName} | {review.matchSeason}:{" "}
      </p>
      <p>Rating: {review.rating}</p>
      <p>Review: {review.textReview}</p>
      <br />
    </li>
  ));
  return (
    <div>
      <h3>User Reviews:</h3>
      <ul>{listItems}</ul>
    </div>
  );
}

class UserDetail extends React.Component {
  state = {
    user_data: {},
    reviews: [],
  };

  componentDidMount() {
    const eMail = sessionStorage.getItem("email");
    var success;
    axios
      .get(`http://127.0.0.1:5000/api/user/${eMail}/`)
      .then((res) => {
        this.setState({
          user_data: res.data[0],
        });
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get(`http://127.0.0.1:5000/api/user/${eMail}/allreviews/`)
      .then((res) => {
        this.setState({
          reviews: Object.values(res.data),
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    //console.log('data', this.state.movie)
    return (
      <Card title={this.state.user_data.username}>
        <Row>
          <Col>
            <p>Email : {this.state.user_data.userEmail}</p>
            <p>Username : {this.state.user_data.userName}</p>
            <p>Birthdate : {this.state.user_data.birthDate}</p>
            <p>FavouriteClubName : {this.state.user_data.favouriteClubName}</p>
            <p>
              Gender:{" "}
              {this.state.user_data.gender === "m" ||
              this.state.user_data.gender === "M"
                ? "Male"
                : "Female"}
            </p>
            <ReviewsList reviews={this.state.reviews} />
          </Col>
        </Row>
      </Card>
    );
  }
}

export default UserDetail;
