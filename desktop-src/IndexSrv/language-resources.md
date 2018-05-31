---
title: Language Resources
description: Language Resources
ms.assetid: f4a3c509-44cf-4df9-8a3c-906959105a92
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Language Resources

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Components for language resources process text strings in the context of a native language and locale for both the Indexing component and the [Querying component](querying-component.md). For indexing, text extracted from filters passes through *word breakers* to identify grammatical constructs. It also passes through *noise word* removal procedures before it is merged into the index. (In English, words such as "the" and "and" are removed; in French, words such as "la" and "et" are removed; and so forth). For querying, in addition to language-specific word breakers and noise word removal, words pass through a stemming process before the query command passes to the query resolution process. (In English, "swim" expands to include terms "swimming", "swam", "swum," and others).

Indexing Service provides language resources for the following languages:

-   Simplified Chinese
-   Traditional Chinese
-   U.S. and Western European languages: Dutch, English (US/UK), French, German, Italian, Spanish, and Swedish
-   Korean
-   Japanese
-   Thai

For more information about extending language resources for Indexing Service, see [Extending Language Resources for Indexing Service](extending-language-resources-for-indexing-service.md).

 

 




