export interface User {
  id: number;
  username: string;
  user_type?: "coach" | "player" | "league_admin";
  is_coach?: boolean;
  is_player?: boolean;
  is_admin?: boolean;
}
