---
Description: Surrogate Pairs
ms.assetid: 2e1077e3-d2f4-4f81-8fc3-320a736d6b62
title: Surrogate Pairs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Surrogate Pairs

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Surrogate pairs are character representations in source code that represent a single character that consists of a sequence of two Unicode values. In a coded pair, the first value is a high surrogate and the second is a low surrogate. A high surrogate is a character in the range U+D800 through U+DBFF. A low surrogate is a character in the range U+DC00 through U+DFFF. Surrogate pairs extend the character set beyond the Unicode character. When you create a word breaker, it is recommended that, when the word breaker handles surrogate pairs, the word breaker consider the following rules:

-   A high surrogate must precede a low surrogate.
-   A low surrogate must follow a high surrogate.
-   A high or low surrogate without a corresponding value has no meaning.

Word breakers must consider any pairs and generate the pairs as such in the index.

For more information, see [Surrogates and Supplementary Characters](https://msdn.microsoft.com/windows/desktop/0dea39e2-a2b4-47fc-b44a-56af8ba1e346).

 

 



