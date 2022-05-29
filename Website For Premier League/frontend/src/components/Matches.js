import React from "react";
import { List, Avatar } from "antd";

const Matches = (props) => {
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
        <List.Item key={item.season + item.homeClubName + item.awayClubName}>
          <List.Item.Meta
            avatar={<Avatar src={item.image} />}
            title={
              <a
                href={`/matches/${item.season.replace(
                  "/",
                  "-"
                )}/${item.homeClubName.replace(
                  " ",
                  "-"
                )}/${item.awayClubName.replace(" ", "-")}`}
              >
                {item.homeClubName} VS {item.awayClubName}{" "}
              </a>
            }
            description={"Season: " + item.season}
          />
          {item.description}
        </List.Item>
      )}
    />
  );
};

export default Matches;
