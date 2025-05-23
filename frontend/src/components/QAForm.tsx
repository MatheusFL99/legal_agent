"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

type QAFormProps = {
  onQuestionSubmit: (question: string) => Promise<void>;
  isProcessing: boolean;
};

export function QAForm({ onQuestionSubmit, isProcessing }: QAFormProps) {
  const [input, setInput] = useState("");

  const handleSubmit = async () => {
    if (!input.trim()) return;
    await onQuestionSubmit(input.trim());
    setInput("");
  };

  return (
    <div className="space-y-3">
      <Textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSubmit();
          }
        }}
        placeholder="Digite sua pergunta jurídica aqui..."
        rows={3}
        disabled={isProcessing}
      />
      <Button
        onClick={handleSubmit}
        disabled={isProcessing || input === ""}
        className="w-full"
      >
        {isProcessing ? "Processando..." : "Enviar"}
      </Button>
    </div>
  );
}
