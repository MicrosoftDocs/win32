---
Description: Description of the EBNF Notation
ms.assetid: 225c8dea-ee94-4b36-9d28-4b3c5aefd36d
title: Description of the EBNF Notation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Description of the EBNF Notation

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Extended Backus-Naur Form (EBNF) notation is a means to specify the syntax of a language succinctly and precisely—in the present case, an Indexing Service query language. The syntax describes the allowable constructs of symbols (characters, or combinations of characters) that the query language recognizes and the query engine processes. The EBNF notation has four types of components:

-   [Terminal Symbol](terminal-symbol.md)
-   [Nonterminal Symbol](nonterminal-symbol.md)
-   [Production Rule](production-rule.md)
-   [Start Symbol](start-symbol.md)

The adopted EBNF notation is ISO/IEC 14977 *Extended BNF* with these minor modifications:

-   The notation does not use the usual concatenation symbol ",". It assumes implicit concatenation of adjacent symbols.
-   The notation uses the symbol "·" (without the quotes) to represent a required space symbol.
-   The notation uses boldface type (**a**) to signify terminal symbols rather than quoting them ('a' or "a").

 

 



