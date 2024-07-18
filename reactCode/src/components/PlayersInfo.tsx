import React from "react";
import { ListGroup } from "react-bootstrap";
import { PlayerType } from "../types/Player";

export interface PlayerProps {
  data?: PlayerType;
}
function PlayersInfo({ data }: PlayerProps) {
  return (
    <ListGroup className="player-info-container">
      <ListGroup.Item variant="dark">Name: {data?.name}</ListGroup.Item>
      <ListGroup.Item variant="light">Team Name: {data?.team}</ListGroup.Item>
      <ListGroup.Item variant="dark">
        Your Average Score: {data?.average_score}
      </ListGroup.Item>
      <ListGroup.Item variant="light">
        Number of games played: {data?.games_participated}
      </ListGroup.Item>
    </ListGroup>
  );
}

export default PlayersInfo;
