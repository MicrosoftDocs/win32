---
title: Word Breaking
description: Word Breaking
ms.assetid: 'ed2e0887-080c-414c-96a1-baa6a841a234'
---

# Word Breaking

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Word breaking is the decomposition of text into individual text tokens, or words. Many languages, especially those with Roman alphabets, have an array of word separators (such as white space) and punctuation that are used to discern words, phrases, and sentences. Word breakers must rely on accurate language heuristics to provide reliable and accurate results.

Word breaking is more complex for character-based systems of writing or script-based alphabets, where the meaning of individual characters is determined from context. For example, in Japanese, a query that contains the term "京" ("Kyouto") does not match a document that contains "東京" ("Tokyo"). The word breaker does not separate the characters in "東京" ("Tokyo"), so the erroneous term "京" ("Kyouto") is not in the index.

For more information about linguistic considerations that may affect your word breaker implementation, see [Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md).

 

 




