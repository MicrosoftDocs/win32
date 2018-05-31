---
title: Compound Phrases
description: Compound Phrases
ms.assetid: 1d647a87-ce3c-4563-9606-318982441aaa
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Compound Phrases

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Some languages, such as Korean, contain complex phrases that can be broken in a number of different ways. A Korean phrase consists of *content words*, such as nouns, pronouns, verbs, and adjectives, followed by *functional words*. Functional words are found in post-positions and endings. Post-positions indicate the functional role of the noun or pronoun in a sentence; endings indicate the functional role of the verb or adjective.

One phrase can have the several analyses, and each analysis can consist of several content words. For example, the phrase "Á¦ÀÛÀÚÀÇ" ("producer's," as in the producer of a movie) has two separate decompositions. One is "Á¦ÀÛÀÚ" ("producer") and the functional word "ÀÇ" (genitive case). The second is "Á¦ÀÛ" ("production") and "ÀÚÀÇ" ("volition"). The word breaker must employ language-specific heuristics to determine, from context, how much weight to give to different analyses. The word breaker may determine which decomposition to use based on the number of resulting component words. Some word breakers may favor short sequences of longer terms, whereas other word breakers may favor long sequences of smaller words.

Another consideration is that in Korean, nouns and pronouns can be the stored in the index without their corresponding functional words. Korean is an [agglutinative language](agglutinative-languages.md) and combines numerous word endings with verbs and adjectives to form countless inflected forms. Verbs and adjectives identified in phrases are saved with their endings in the index, but the word breaker does not generate new forms.

 

 




