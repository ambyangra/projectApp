import React, { useState, useEffect } from "react";
import axios, { AxiosError } from "axios";
import LeagueAdminPage, {
  LeagueAdminProps,
} from "../components/LeagueAdminPage";

function LeagueAdmin() {
  const [data, setData] = useState<LeagueAdminProps["data"]>({
    teams: undefined,
    players: undefined,
  });
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/league-admin/")
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
      <LeagueAdminPage data={data} />
    </div>
  );
}

export default LeagueAdmin;
