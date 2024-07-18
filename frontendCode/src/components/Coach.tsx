import React from "react";
import { ListGroup, Tab, Tabs } from "react-bootstrap";
import PlayersTable from "./PlayersTable";
import Scoreboard from "./Scoreboard";
import { CoachDetails } from "../types/CoachDetails";

interface CoachProps {
  data: CoachDetails;
}

export default function Coach({ data }: CoachProps) {
  return (
    <div>
      <h2>Coach Details</h2>
      <Tabs defaultActiveKey="home" id="admin-tabs" className="mb-3">
        <Tab eventKey="home" title="Home">
          <h3>Home Page</h3>
          <Scoreboard />
        </Tab>
        <Tab eventKey="team" title="Team Details">
          <TeamDetails data={data}></TeamDetails>
        </Tab>
        <Tab eventKey="players" title="Players Details">
          <PlayersTable data={data}></PlayersTable>
        </Tab>
      </Tabs>
    </div>
  );
}

function TeamDetails({ data }: CoachProps) {
  return (
    <ListGroup className="team-details-container">
      <h3>Your Details Below</h3>
      <ListGroup.Item variant="dark">
        Team Name:{data?.team?.team_name}
      </ListGroup.Item>
      <ListGroup.Item variant="light">
        Team Size:{data?.team?.team_size}
      </ListGroup.Item>
    </ListGroup>
  );
}
