"use client";

import * as React from "react";
import { QAForm } from "@/components/QAForm";
import { ChatMessageBubble } from "@/components/ChatMessageBubble";
import type { LegalQAndAInput, LegalQAndAOutput } from "@/flows/legal-q-and-a";
import { legalQAndA } from "@/flows/legal-q-and-a";
import type { ChatEntry } from "@/types";
import { Scale } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

export default function HomePage() {
  const [chatHistory, setChatHistory] = React.useState<ChatEntry[]>([]);
  const [isProcessing, setIsProcessing] = React.useState(false);
  const messagesEndRef = React.useRef<null | HTMLDivElement>(null);
  const { toast } = useToast();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  React.useEffect(() => {
    scrollToBottom();
  }, [chatHistory]);

  const handleQuestionSubmit = async (questionText: string) => {
    setIsProcessing(true);

    const userEntry: ChatEntry = {
      id: crypto.randomUUID(),
      role: "user",
      content: questionText,
      timestamp: new Date(),
    };

    const assistantEntryId = crypto.randomUUID();
    const assistantLoadingEntry: ChatEntry = {
      id: assistantEntryId,
      role: "ai",
      content: "",
      isLoading: true,
      timestamp: new Date(),
    };

    setChatHistory((prev) => [...prev, userEntry, assistantLoadingEntry]);

    let assistantResponse: LegalQAndAOutput | null = null;

    try {
      const input: LegalQAndAInput = { question: questionText };
      const response = await legalQAndA(input);
      console.log("[DEBUG] Resposta do backend:", response);
      assistantResponse = response;

      setChatHistory((prev) =>
        prev.map((entry) =>
          entry.id === assistantEntryId
            ? {
                ...entry,
                content: response.answer,
                fullResponse: response,
                isLoading: false,
                isError: false,
              }
            : entry
        )
      );
    } catch (error) {
      console.error("Error calling AI:", error);
      toast({
        title: "Erro ao processar pergunta",
        description:
          "Ocorreu um erro ao tentar obter a resposta. Tente novamente.",
        variant: "destructive",
      });
      setChatHistory((prev) =>
        prev.map((entry) =>
          entry.id === assistantEntryId
            ? {
                ...entry,
                content:
                  "Desculpe, não foi possível processar sua pergunta no momento.",
                isLoading: false,
                isError: true,
              }
            : entry
        )
      );
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-background">
      <header className="flex flex-col items-center text-center py-4 md:py-6 px-4 shadow-sm shrink-0 border-b border-border">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-primary-foreground rounded-full shadow-md border border-primary/20">
            <Scale className="h-8 w-8 text-primary" />
          </div>
          <div>
            <h1 className="text-2xl md:text-3xl font-bold tracking-tight text-primary">
              Assistente JusAI
            </h1>
            <p className="mt-1 text-xs md:text-sm text-muted-foreground max-w-md">
              Agente Jurídico Informativo com IA para apoio à cidadania.
            </p>
          </div>
        </div>
      </header>

      <main className="flex-1 overflow-y-auto p-4 md:p-6 w-full max-w-3xl mx-auto space-y-4">
        {chatHistory.length === 0 && !isProcessing && (
          <div className="text-center text-muted-foreground pt-10 flex flex-col items-center">
            <Scale size={48} className="mb-4 text-primary/50" />
            <p className="text-lg font-medium">
              Bem-vindo ao assistente jurídico JusAI!
            </p>
            <p>Comece fazendo uma pergunta sobre questões legais abaixo.</p>
          </div>
        )}
        {chatHistory.map((entry) => (
          <ChatMessageBubble key={entry.id} entry={entry} />
        ))}
        <div ref={messagesEndRef} />
      </main>

      <div className="shrink-0 p-3 md:p-4 border-t border-border bg-background w-full">
        <div className="max-w-3xl mx-auto">
          <QAForm
            onQuestionSubmit={handleQuestionSubmit}
            isProcessing={isProcessing}
          />
        </div>
      </div>
    </div>
  );
}
