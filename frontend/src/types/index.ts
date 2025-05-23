export interface LegalQAndAOutput {
  answer: string;
  disclaimer: string;
  resources: string;
}

export interface ChatEntry {
  id: string;
  role: "user" | "ai";
  content: string;
  timestamp: Date;
  isLoading?: boolean;
  isError?: boolean;
  fullResponse?: LegalQAndAOutput;
}
