import React, { useState, useEffect } from "react";
import axios from "axios";
import { Table } from "react-bootstrap";
import { Team } from "../types/Team";

interface Game {
  id: number;
  team_a: Team;
  team_b: Team;
  score_a: number;
  score_b: number;
  date: string;
}

export interface ScoreboardProps {
  games: Game[];
}

function Scoreboard() {
  const [gamesPlayed, setGamesPlayed] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/scoreboard/")
      .then((response) => {
        setGamesPlayed(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <ScoreboardTable games={gamesPlayed} />
    </div>
  );
}

function ScoreboardTable({ games }: ScoreboardProps) {
  return (
    <div>
      <h2>Scoreboard</h2>
      <Table striped bordered hover responsive size="sm">
        <thead>
          <tr>
            <th>Game ID</th>
            <th>First Team</th>
            <th>First Team Score</th>
            <th>Second Team Score</th>
            <th>Second Team</th>
            <th>Game Date</th>
          </tr>
        </thead>
        <tbody>
          {games?.map((game) => (
            <tr key={game.id}>
              <td>{game.id}</td>
              <td>{game.team_a.team_name}</td>
              <td>{game.score_a}</td>
              <td>{game.score_b}</td>
              <td>{game.team_b.team_name}</td>
              <td>{game.date}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default Scoreboard;
