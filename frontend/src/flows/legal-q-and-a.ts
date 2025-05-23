"use server";

import { z } from "zod";

const LegalQAndAInputSchema = z.object({
  question: z.string().describe("A pergunta jurídica feita pelo usuário."),
});
export type LegalQAndAInput = z.infer<typeof LegalQAndAInputSchema>;

const LegalQAndAOutputSchema = z.object({
  answer: z.string().describe("Resposta da IA."),
  disclaimer: z
    .string()
    .describe("Aviso legal de que a resposta não substitui um advogado."),
  resources: z.string().describe("Links relevantes em formato Markdown."),
});
export type LegalQAndAOutput = z.infer<typeof LegalQAndAOutputSchema>;

export async function legalQAndA(
  input: LegalQAndAInput,
  historico: { role: string; content: string }[]
): Promise<LegalQAndAOutput> {
  const API_URL = "http://localhost:8000/consultar";

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        pergunta: input.question,
        historico,
      }),
    });

    if (!res.ok) {
      throw new Error(`Erro da API: ${res.statusText}`);
    }

    const data = await res.json();

    const resourcesMarkdown = Array.isArray(data.resources)
      ? data.resources
          .filter((f: any) => !!f.link)
          .map((f: any) => `- [${f.titulo || f.link}](${f.link})`)
          .join("\n")
      : "";

    return {
      answer: data.answer,
      disclaimer: data.disclaimer,
      resources: resourcesMarkdown,
    };
  } catch (error) {
    console.error("[legalQAndA] Erro ao consultar backend:", error);
    return {
      answer: "❌ Ocorreu um erro ao buscar a resposta jurídica.",
      disclaimer:
        "Esta resposta é gerada por IA e não substitui a orientação de um advogado.",
      resources: "",
    };
  }
}
