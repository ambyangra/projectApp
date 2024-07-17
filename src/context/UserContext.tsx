import React, { createContext, useState, useEffect, ReactNode } from "react";
import axios from "axios";
import { User } from "../types/User";

export const UserContext = createContext<{
  user: User | null;
  isLoading: boolean;
  error: string | null;
}>({
  user: null,
  isLoading: false,
  error: null,
});

interface UserProviderProps {
  children: ReactNode;
}

export const UserProvider = ({ children }: UserProviderProps) => {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUserInfo = async () => {
      setIsLoading(true);
      try {
        const response = await axios.get<User>(
          "http://localhost:8000/api/users/",
        );
        console.log(response);
        setUser({
          id: response.data.id,
          username: response.data.username,
          user_type: response.data.user_type,
          is_coach: response.data.user_type === "coach",
          is_player: response.data.user_type === "player",
          is_admin: response.data.user_type === "league_admin",
        });
        setError(null);
      } catch (err) {
        console.error("Error fetching user info:", err);
        setError("Failed to fetch user information");
      } finally {
        setIsLoading(false);
      }
    };
    fetchUserInfo();
  }, []);

  return (
    <UserContext.Provider value={{ user, isLoading, error }}>
      {children}
    </UserContext.Provider>
  );
};
