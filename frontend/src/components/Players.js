import React from "react";
import { List, Avatar } from "antd";

const Players = (props) => {
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
        <List.Item key={item.playerName}>
          <List.Item.Meta
            avatar={<Avatar src={item.main_picture} />}
            title={
              <a href={`/players/${item.playerName.replace(" ", ".")}`}>
                Player Name: {item.playerName}
              </a>
            }
          />
          {"Nationality: " + item.nationality}
        </List.Item>
      )}
    />
  );
};

export default Players;
