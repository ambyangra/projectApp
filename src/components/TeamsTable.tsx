import React from "react";
import { Table } from "react-bootstrap";
import { Team } from "../types/Team";

export interface TeamsTableProps {
  data: {
    teams?: Team[];
  };
}

export default function TeamsTable({ data }: TeamsTableProps) {
  return (
    <div>
      <h2>Teams</h2>
      <Table striped bordered hover responsive size="sm">
        <thead>
          <tr>
            <th>Team Name</th>
            <th>Team Size</th>
            <th>League Admin</th>
          </tr>
        </thead>
        <tbody>
          {data?.teams?.map((team, index) => (
            <tr key={index}>
              <td>{team.team_name}</td>
              <td>{team.team_size}</td>
              <td>{team.league_admin.name}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}
