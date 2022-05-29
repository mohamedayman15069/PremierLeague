import React from "react";
import { List, Avatar } from "antd";

const Reviews = (props) => {
  return (
    <List
      itemLayout="vertical"
      size="large"
      pagination={{
        onChange: (page) => {
          console.log(page);
        },
        pageSize: 10,
      }}
      dataSource={props.data}
      renderItem={(item) => (
        <List.Item key={item.userEmail}>
          <List.Item.Meta
            avatar={<Avatar src={item.image} />}
            title={item.userEmail}
            description={"Rating: " + item.rating}
          />
          {item.textReview}
        </List.Item>
      )}
    />
  );
};

export default Reviews;
