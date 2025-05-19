export type ChatEntry = {
  id: string;
  role: "user" | "assistant";
  content: string;
  isLoading?: boolean;
  isError?: boolean;
  timestamp: Date;
};
