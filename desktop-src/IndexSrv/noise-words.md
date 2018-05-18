---
title: Noise Words
description: Noise Words
ms.assetid: 'f1c23576-e616-4703-adbd-a77f168f5fa4'
---

# Noise Words

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

You can configure Indexing Service to use noise word lists for specific languages. Indexing Service uses these lists when it invokes a word breaker for that language. Noise words, also known as stop words, are words that are not significant indicators for content. Indexing Service removes noise words from query terms and from content that is included in the full-text index. An *offset* is the occurrence of a word in a document or in a list of query terms. The offset of noise words in a document or query is recorded as blank. Removing noise words improves query performance by avoiding unnecessary index growth. It also improves the relevance of query results. For example, "the" in the English language occurs so often that it has little value as a unique key. "The" is in the noise word list, is not written to the content index, and, if queried for, returns no results.

Noise words act as placeholders in phrase queries. A document that contains the text "wag the dog" is stored in the index with "wag" at occurrence 1 and "dog" at occurrence 3. The phrase query "wag dog" does not match, but the phrase query "wag a dog" does, because the occurrence information matches. The phrase "wag purple dog" does not match because "purple" is not found in the index at occurrence 2. However, a query for "wag the dog" returns documents that contain "wag purple dog" because there is no way to efficiently determine whether the document had a non-noise word between "wag" and "dog."

 

 




