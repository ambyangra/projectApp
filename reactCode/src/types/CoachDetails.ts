import { PlayerType } from "./Player";
import { Team } from "./Team";

export interface CoachDetails {
  team: Team;
  players: PlayerType[];
}
