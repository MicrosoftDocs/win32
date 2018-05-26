---
title: Support for Multiple Languages
description: Support for Multiple Languages
ms.assetid: 6bf12187-b8b0-4e83-aee5-bee03fab3370
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Support for Multiple Languages

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Because IIS can search documents in many languages, multilingual indexing and querying features are a standard feature of Indexing Service. The query system is designed to address localization considerations. The query system is completely modular and can dynamically load and unload language-specific utilities. These utilities include word breakers, stemmers, and normalizers. These [language resource](about-language-resources.md) components are available for several languages.

Indexing Service can index multilingual documents and switch between languages as required (for example, index an English paragraph, index a French paragraph, and switch back to English). All index information is stored as Unicode characters, and all queries are converted to Unicode before they are processed.

Indexing Service does not distinguish between language once the words have been entered into the index. It is possible to return documents written in a language different from the language posted in the query. In many cases this is appropriate. For example a query for *Windows 95* will return a French document that contains the English phrase *Windows 95*. In some cases languages contain words known as *homologues*, words that are spelled the same in two or more languages but have very different meanings. Indexing Service does not distinguish these cases because Indexing Service does not perform any language translation.

Finally, you should know that mixing languages can yield unpredictable results. For example, if you set the multilanguage form to German and query for English words, the results likely will not be the same if the identical query were posted with the language set to English. This is because Indexing Service is using the German linguistics modules to analyze the query field to determine which words and phrases to search for (that is, it is trying to perform German word breaking on English text). The German word breaker assumes German grammar when it breaks textual characters into words, so it often generates wrong word-break results when breaking non-German text.

This section contains:

-   [Querying a Site Without Language Resources:](querying-a-site-without-language-resources.md) Lists the languages shipped with Indexing Service and describes the effect of issuing queries to sites without language resources.
-   [Setting Language Codes in HTML Files:](setting-language-codes-in-html-files.md) Tells how to use the **MS.Locale** property in HTML files.
-   [Getting Browsers to Recognize Different Languages:](getting-browsers-to-recognize-different-languages.md) Explains the effects of the HTTP\_ACCEPT\_LANGUAGE variable on [CiLocale](variables-in-forms-and-in-idq-files.md#-idxs-cilocale-var) variable settings.
-   [Displaying Results Correctly:](displaying-results-correctly.md) Tells how to get browsers to display correct results in the correct language through the variable [CiCodepage](variables-in-forms-and-in-idq-files.md#-idxs-cicodepage-var).

 

 




