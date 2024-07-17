import { Team } from "./Team";

export interface Tournament {
  id: number;
  name: string;
  start_date: string;
  end_date: string;
  current_round: number;
  winning_team?: Team;
}
