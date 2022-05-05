import React from "react";
import axios from "axios";
import ActionButton from "antd/lib/modal/ActionButton";
import { Card, Image, Row, Col, Radio, Input, Button, Form } from "antd";
import { Link } from "react-router-dom";
import Reviews from "../components/Review";

const { TextArea } = Input;

class ReviewForm extends React.Component {
  constructor(prop) {
    super(prop);
    this.handleReviewSubmit = this.handleReviewSubmit.bind(this);
  }

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

  handleReviewSubmit(event) {
    event.preventDefault();
    const rating = event.target.elements.rating.value;
    const review = event.target.elements.review.value;

    const season = this.props.match.params.season; // convert / to -

    const homeClubName = this.props.match.params.homeClubName;

    const awayClubName = this.props.match.params.awayClubName;

    const eMail = sessionStorage.getItem("email");

    console.log(season, "  ", homeClubName, " ", awayClubName, " ", eMail);

    axios
      .post(
        `http://127.0.0.1:5000/api/matches/${season}/${homeClubName}/${awayClubName}/writereview/`,
        {
          review: review,
          rating: Number(rating),
          email: eMail,
        }
      )
      .then((res) => {
        console.log("worked");
        window.location.reload();
      })
      .catch((err) => {
        alert("you already have a review");
      });
  }
  render() {
    var loggd_in = sessionStorage.getItem("logged_in");
    return loggd_in !== null ? (
      <>
        <Col span={9}>
          <form onSubmit={this.handleReviewSubmit}>
            <label>
              Rating:
              <br />
              <Radio.Group name="rating" defaultValue={0}>
                <Radio value={1}>1</Radio>
                <Radio value={2}>2</Radio>
                <Radio value={3}>3</Radio>
                <Radio value={4}>4</Radio>
                <Radio value={5}>5</Radio>
                <Radio value={6}>6</Radio>
                <Radio value={7}>7</Radio>
                <Radio value={8}>8</Radio>
                <Radio value={9}>9</Radio>
                <Radio value={10}>10</Radio>
              </Radio.Group>
            </label>
            <br />
            <label>
              <br />
              <TextArea name="review" placeholder="Enter Review" row={4} />
            </label>
            <br />

            <input type="submit" value="Submit" />
          </form>
        </Col>

        <Card title="Reviews for this match">
          <Reviews data={this.state.reviews} />
        </Card>
      </>
    ) : (
      <p> You need to log in!</p>
    );
  }
}
export default ReviewForm;

{
  /* <div>
<Form onSubmit={this.handFormSubmit}>
    <Form.Item label="Rating">
        <Input name='rating' placeholder="Enter rating from 1 to 10" />
    </Form.Item>
    <Form.Item label="Review">
        <Input name='review' placeholder="Enter Review" />
    </Form.Item>
        <Button value="review" type='submit'>Submit</Button>
    </Form.Item>
</Form>
</div> */
}
