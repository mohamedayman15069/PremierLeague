import React from "react";
import { List, Avatar } from "antd";

// CAST

const Stadiums = (props) => {
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
        <List.Item key={item.clubName}>
          <List.Item.Meta
            avatar={<Avatar src={item.main_picture} />}
            title={
              <a href={`/stadiums/${item.stadiumName.replace(" ", "-")}`}>
                Stadium Name: {item.stadiumName}
              </a>
            }
          />
          {"Adress Postal Code: " + item.addressPostalCode}
        </List.Item>
      )}
    />
  );
};

export default Stadiums;
