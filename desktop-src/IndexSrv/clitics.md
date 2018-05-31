---
title: Clitics
description: Clitics
ms.assetid: f0825585-864c-4444-aa0d-1e2c7ab9b903
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Clitics

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

A clitic is an unstressed word that is incapable of standing on its own and attaches to a stressed word to form a single unit. Clitics cannot be easily classified as phonological, syntactic, or morphological.

Clitics come in two types: *proclitics* and *enclitics*. Proclitics attach themselves to the beginning of a word. Enclitics attach themselves to the end of a word. For example, in French, proclitics include the pronouns "me" and "les" in "il me les a donnés" ("he has given them to me"). Enclitics include "les" in "donnez-les-moi" ("give them to me"). Other examples of French clitics include cases where the article is connected to a noun with an apostrophe, such as "l'orange" ("the orange"). In this case, it is recommended that the apostrophe be treated as a separator between the clitic and the word to which the clitic is attached. The word breaker generates "l" and "orange" so that queries for "orange" match "l'orange."

Clitics are more difficult to parse in languages such as Spanish. A Spanish verb may generate many surface forms, depending on the tense. For example, you can conjugate the irregular verb "ir" ("to go") as "nosotros \[or nosotras\] vamos" ("we go," "let's go"). You can also write "vamos" as "vámanos," where the pronoun "nosotros (or nosotras)" is represented in the clitic form. In this case, clitics should remain intact during both index creation and querying. Considerations must be made between removing the clitic during index creation and generating the surface forms through stemming at query time. Removing clitics in cases where the morphology of clitic composition is ambiguous can lead to unpredictable results. Generating a large number of surface forms for a word increases the size of the full-text index and may have a negative effect on query performance. It is recommended that the stemmer generate only a small number of surface forms.

 

 




