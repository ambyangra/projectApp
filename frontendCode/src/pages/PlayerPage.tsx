import React, { useState, useEffect } from "react";
import axios, { AxiosError } from "axios";
import Player from "../components/Player";
import { PlayerType } from "../types/Player";

function PlayerPage() {
  const [data, setData] = useState<PlayerType | undefined>(undefined);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/players/")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        if (axios.isAxiosError(error)) {
          const axiosError = error as AxiosError;
          setError(axiosError.message);
        } else {
          setError("An unexpected error occurred while fetching player data.");
        }
      });
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Player data={data} />
    </div>
  );
}

export default PlayerPage;
