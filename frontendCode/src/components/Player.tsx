import React from "react";
import { Tab, Tabs } from "react-bootstrap";
import Scoreboard from "./Scoreboard";
import { PlayerType } from "../types/Player";
import PlayersInfo from "./PlayersInfo";

export interface PlayerProps {
  data?: PlayerType;
}

function Player({ data }: PlayerProps) {
  return (
    <div>
      <h2>Players Page</h2>
      <Tabs defaultActiveKey="home" id="admin-tabs" className="mb-3">
        <Tab eventKey="home" title="Home">
          <Scoreboard />
        </Tab>
        <Tab eventKey="player" title="Your Details">
          <PlayersInfo data={data}></PlayersInfo>
        </Tab>
      </Tabs>
    </div>
  );
}

export default Player;
