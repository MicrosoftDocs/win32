---
Description: Content queries search text-type properties of documents.
ms.assetid: 47f2e318-642f-4a3a-a62b-b3ec8a2b0237
title: Content Queries
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Content Queries

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Content queries search text-type properties of documents. Content queries process the textual content of a sequence of words in one of two ways. A series of words such as "Web server administrator" can be treated as a phrase, where the proximity of words and the word order is significant (no intervening words, and words must appear in a specific order). Alternatively, the words can be treated independently, ignoring the order and proximity of the words.

To handle both cases, phrase and non-phrase (free-text) interpretation of textual content, Dialect 2 has two modes for content queries: phrase and freetext. It uses the two following text interpretation tags.

``` syntax
{phrase} text {/phrase}
{freetext} text {/freetext}
```

The {phrase} tag specifies the use of the phrase mode, and the text within the tags is considered to be a single entity. The search engine treats the word sequence and position as significant. The {freetext} tag specifies the use of free-text mode, where the word sequence and position are insignificant, and which includes word stemming. The {phrase} and {freetext} tags are mutually exclusive and cannot be embedded or nested. The default mode of Dialect 2, if no tag is used, is free-text mode. (In Dialect 1, the default mode is phrase mode.) To indicate free-text mode in the short form, either leave off any enclosing quote marks around the text or use the dollar sign ($) with the Contents property.

The following table summarizes the text modes and their long and short forms.



| Text Mode           | Long Form                                | Short Form                                                    |
|---------------------|------------------------------------------|---------------------------------------------------------------|
| phrase<br/>   | {phrase} *text* {/phrase}<br/>     | " *text* "<br/>                                         |
| freetext<br/> | {freetext} *text* {/freetext}<br/> | *text*<br/> —Or—<br/> $contents *text*<br/> |



 

The following table illustrates examples of the use of text modes in content queries.



| To Search For                             | Example                                                                                                                                                          | Results                                                                 |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Documents that match a phrase.<br/> | {phrase} big red truck {/phrase}<br/> —Or—<br/> "big red truck"<br/>                                                                           | Documents that contain the phrase *big red truck*.<br/>           |
| Documents that match terms.<br/>    | {freetext} Why is the sky blue? {/freetext}<br/> —Or—<br/> Why is the sky blue?<br/> —Or—<br/> $contents Why is the sky blue?<br/> | Documents about the blue sky, ranked by estimated relevance.<br/> |



 

In Dialect 2, the query

@contents Why is the sky blue?

without quotes around the text is a phrase-mode query equivalent to

@contents "Why is the sky blue?"

 

 




