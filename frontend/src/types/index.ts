export interface LegalQAndAOutput {
  answer: string;
  disclaimer: string;
  resources: string;
}

export type ChatEntry = {
  id: string;
  role: "user" | "ai";
  content: string;
  timestamp?: Date;
  isLoading?: boolean;
  isError?: boolean;
  fullResponse?: {
    answer: string;
    disclaimer: string;
    resources: string;
  };
};
