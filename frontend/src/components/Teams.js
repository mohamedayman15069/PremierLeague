import React from "react";
import { List, Avatar } from "antd";

// CAST

const Teams = (props) => {
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
              <a href={`/teams/${item.clubName.replace(" ", "-")}`}>
                Team Name: {item.clubName}
              </a>
            }
          />
          {"Stadium Name: " + item.stadiumName}
        </List.Item>
      )}
    />
  );
};

export default Teams;
