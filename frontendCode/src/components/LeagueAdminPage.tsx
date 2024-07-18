import React from "react";
import { Tab, Tabs } from "react-bootstrap";
import PlayersTable from "./PlayersTable";
import TeamsTable from "./TeamsTable";
import Scoreboard from "./Scoreboard";
import { Team } from "../types/Team";
import { PlayerType } from "../types/Player";

export interface LeagueAdminProps {
  data: {
    teams?: Team[];
    players?: PlayerType[];
  };
}

const LeagueAdminPage: React.FC<LeagueAdminProps> = ({ data }) => {
  return (
    <div>
      <h2>Leage Admin Page</h2>
      <Tabs defaultActiveKey="home" id="admin-tabs" className="mb-3">
        <Tab eventKey="home" title="Home">
          <Scoreboard />
        </Tab>
        <Tab eventKey="player" title="Players">
          <PlayersTable data={data} />
        </Tab>
        <Tab eventKey="team" title="Teams">
          <TeamsTable data={data} />
        </Tab>
      </Tabs>
    </div>
  );
};

export default LeagueAdminPage;
