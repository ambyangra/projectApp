import React from "react";
import { Table } from "react-bootstrap";
import { LeagueAdminProps } from "./LeagueAdminPage";

export default function PlayersTable({ data }: LeagueAdminProps) {
  return (
    <div>
      <h2>Players</h2>
      <Table striped bordered hover responsive size="sm">
        <thead>
          <tr>
            <th>Name</th>
            <th>Team</th>
            <th>Games Participated</th>
            <th>Average Score</th>
          </tr>
        </thead>
        <tbody>
          {data?.players?.map((player, index) => (
            <tr key={index}>
              <td>{player.name}</td>
              <td>{player.team}</td>
              <td>{player.games_participated}</td>
              <td>{player.average_score}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}
