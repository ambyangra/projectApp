import React, { useContext } from "react";
import "./App.css";
import { Spinner } from "react-bootstrap";
import { UserProvider, UserContext } from "./context/UserContext";
import LeagueAdmin from "./pages/LeagueAdmin";
import PlayerPage from "./pages/PlayerPage";
import CoachPage from "./pages/CoachPage";

function App() {
  return (
    <UserProvider>
      <AppContent />
    </UserProvider>
  );
}

const AppContent = () => {
  const { user, isLoading, error } = useContext(UserContext);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!user) {
    return <Spinner />;
  }

  if (user.is_coach) {
    return <CoachPage />;
  } else if (user.is_player) {
    return <PlayerPage />;
  } else if (user.is_admin) {
    return <LeagueAdmin />;
  } else {
    return <div>Unknown User</div>;
  }
};

export default App;
