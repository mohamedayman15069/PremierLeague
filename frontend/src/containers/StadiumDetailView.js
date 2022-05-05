import React from "react";
import axios from "axios";
import { Card, Image, Row, Col } from "antd";
import { Link } from "react-router-dom";
import { Form, Input, Button, Radio } from "antd";

const ColoredLine = ({ color }) => (
    <hr       

        style={{
            color: color,
            backgroundColor: color,
            height: 5,
            textAlign: "center"
        }}
    />
);

class StadiumDetail extends React.Component {
  state = {
    stadiumInfo : {}
  };

  componentDidMount() {
    const stadium = this.props.match.params.StadiumName;
    console.log(stadium)
    
    if(stadium == 'Wembley-Stadium')
        {   
            axios
      .get(`http://127.0.0.1:5000/api/stadium/`)
            .then((res) => {
                this.setState({
                    stadiumInfo: res.data[0],
                });
                console.log(this.state.stadiumInfo)
            })
            .catch((error) => {
                console.log(error);
            });
        }
    else {
    axios
      .get(`http://127.0.0.1:5000/api/stadium/${stadium}`)
      .then((res) => {
        this.setState({
            stadiumInfo: res.data[0],
        });
        console.log(this.state.stadiumInfo)
      })
      .catch((error) => {
        console.log(error);
      });
    }

    
  }


  render() {
    return (
      <Card title={this.state.stadiumInfo.StadiumName} style = {{textAlign: "center"}}>
        <Row>
          <Col span={15}>
            { this.state.stadiumInfo.clubName != null ? 
            (
                <>Home Team: {this.state.stadiumInfo.clubName}
                    <ColoredLine color="#5F9EA0" />
                </>
            ): 
                null
            
              
            } 
            <p> Stadium Name: {this.state.stadiumInfo.stadiumName}</p>
            <ColoredLine color="#5F9EA0" />
            <p>Address Postal Code: {this.state.stadiumInfo.addressPostalCode}</p>
            <ColoredLine color="#5F9EA0" />
            <p>Address City: {this.state.stadiumInfo.addressCity}</p>
            <ColoredLine color="#5F9EA0" />
            <p>Address Street: {this.state.stadiumInfo.addressStreet}</p>
            <ColoredLine color="#5F9EA0" />
            <p>Building Date: {this.state.stadiumInfo.buildingDate}</p>
            <ColoredLine color="#5F9EA0" />
            <p>Length Bitch Size: {this.state.stadiumInfo.lengthBitchSize}</p>
            <ColoredLine color="#5F9EA0" />
            <p>Width Bitch Size: {this.state.stadiumInfo.widthBitchSize}</p>
            <ColoredLine color="#5F9EA0" />
            <p>Record League Attendance: {this.state.stadiumInfo.recordLeagueAttendance}</p>
            <ColoredLine color="#5F9EA0" />
            <p>Capacity: {this.state.stadiumInfo.capacity}</p>

          </Col>
        </Row>
       
      </Card>
    );
  }
}

export default StadiumDetail;
