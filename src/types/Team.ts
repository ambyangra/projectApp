import { LeagueAdmin } from "./LeagueAdmin";
import { Tournament } from "./Tournament";

export interface Team {
  id: number;
  team_name: string;
  team_size: number;
  league_admin: LeagueAdmin;
  is_eliminated: boolean;
  tournament?: Tournament;
}
