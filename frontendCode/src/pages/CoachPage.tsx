import React, { useState, useEffect } from "react";
import axios, { AxiosError } from "axios";
import Coach from "../components/Coach";
import { CoachDetails } from "../types/CoachDetails";

export default function CoachPage() {
  const [coachData, setCoachData] = useState<CoachDetails | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/coaches/")
      .then((response) => {
        setCoachData(response.data);
      })
      .catch((error) => {
        if (axios.isAxiosError(error)) {
          const axiosError = error as AxiosError;
          setError(axiosError.message);
        } else {
          setError("An unexpected error occurred while fetching coach data.");
        }
      });
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!coachData) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Coach data={coachData} />
    </div>
  );
}
