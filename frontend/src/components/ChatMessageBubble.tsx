"use client";

import * as React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  AlertTriangle,
  Link as LinkIcon,
  User,
  Sparkles,
  ExternalLink,
} from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";
import type { ChatEntry } from "@/types";

type ChatMessageBubbleProps = {
  entry: ChatEntry;
};

export function ChatMessageBubble({ entry }: ChatMessageBubbleProps) {
  const isUser = entry.role === "user";
  const isAi = entry.role === "ai";

  const MarkdownComponents: object = {
    a: ({ node, ...props }: any) => (
      <a
        {...props}
        target="_blank"
        rel="noopener noreferrer"
        className="text-primary hover:underline"
      >
        {props.children}{" "}
        <ExternalLink className="inline-block h-3 w-3 ml-0.5" />
      </a>
    ),
    p: ({ node, ...props }: any) => <p className="mb-2 last:mb-0" {...props} />,
  };

  if (isUser) {
    return (
      <div className="flex justify-end mb-4 animate-fadeIn">
        <Card className="max-w-[70%] bg-primary text-primary-foreground rounded-xl rounded-br-none shadow-md">
          <CardHeader className="pb-2 pt-3 px-4">
            <CardTitle className="text-sm font-semibold flex items-center gap-2">
              <User className="h-4 w-4" /> Você
            </CardTitle>
          </CardHeader>
          <CardContent className="text-sm px-4 pb-3">
            <p className="whitespace-pre-wrap">{entry.content}</p>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="flex justify-start mb-4 animate-fadeIn">
      <Card className="max-w-[85%] bg-card rounded-xl rounded-bl-none shadow-md border">
        <CardHeader className="pb-2 pt-3 px-4">
          <CardTitle className="text-sm font-semibold flex items-center gap-2 text-primary">
            <Sparkles className="h-4 w-4" /> JusAI
          </CardTitle>
        </CardHeader>
        <CardContent className="text-sm space-y-3 px-4 pb-3">
          {entry.isLoading ? (
            <div className="space-y-2 pt-1">
              <Skeleton className="h-4 w-[80%]" />
              <Skeleton className="h-4 w-[60%]" />
              <Skeleton className="h-4 w-[70%]" />
            </div>
          ) : entry.isError ? (
            <div className="text-destructive flex items-center gap-2">
              <AlertTriangle className="h-4 w-4" />
              <p>{entry.content}</p>
            </div>
          ) : (
            <>
              <div className="prose prose-sm max-w-none dark:prose-invert prose-p:my-1 prose-ul:my-1 prose-li:my-0.5">
                <ReactMarkdown
                  components={MarkdownComponents}
                  remarkPlugins={[remarkGfm]}
                >
                  {entry.content}
                </ReactMarkdown>
              </div>

              {entry.fullResponse?.disclaimer && (
                <div className="mt-3 pt-3 border-t border-border/50">
                  <h4 className="text-sm font-semibold flex items-center gap-1.5 mb-1 text-amber-600 dark:text-amber-500">
                    <AlertTriangle className="h-3.5 w-3.5" />
                    Aviso Importante:
                  </h4>
                  <p className="whitespace-pre-wrap text-sm text-muted-foreground/90 italic">
                    {entry.fullResponse.disclaimer}
                  </p>
                </div>
              )}
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
