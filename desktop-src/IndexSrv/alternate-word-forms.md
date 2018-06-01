---
Description: Alternate Word Forms
ms.assetid: 41b75168-0cd8-4066-998d-154a565cd408
title: Alternate Word Forms
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Alternate Word Forms

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Dialect 2 provides an effective, but imperfect, mechanism to create alternate word-form, or "fuzzy", queries. These queries take an input word and create alternate forms of the word when submitting the query. This feature goes beyond simple pattern-matching support and uses linguistic or other advanced technologies to generate the alternate word forms.

Alternate word-form query expressions are created using the {generate} tag and specifying a method as an attribute.

{generate method=*value*} *query terms* {/generate}

The method attribute specifies the algorithm to be used to generate alternate words for searching. Currently, the valid values for method are prefix and inflect. When prefix is specified, all words beginning with the query terms are found. When inflect is specified, linguistic inflection is performed.

In the short form, the one or two asterisk characters are appended to a word to specify generation of alternate word forms. A single asterisk specifies prefix generation, and a double asterisk specifies inflection generation.

The following table gives examples of alternate word-form queries.



| To Search For                                                 | Example                                                                                                                 | Results                                                                           |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Documents containing a term as a prefix.<br/>           | {prop name=contents} {generate method=prefix} dog {/generate}<br/>  Or <br/> @contents dog\*<br/>     | Documents containing *dog*, *dogs*, *doghouse*, *dogma*, and so forth.<br/> |
| Documents containing inflectional forms of a term.<br/> | prop name=contents} {generate method=inflect} swim {/generate}<br/>  Or <br/> @contents swim\*\*<br/> | Documents containing *swim*, *swam*, or *swum*.<br/>                        |



 

Indexing Service provides only inflectional, not derivational, generation. Therefore, only words in the same family (noun, verb, adjective, adverb, and so forth) are generated. For example, gerunds are not generated from nouns. Stemming "swim" generates swim, swam, swum, since these are all verbs   but not nouns such as swimmer and swimmers.

Some search engines may provide other forms of generation on words, such as derivational morphology or soundex. There is no short form for these extended features. The long form must be used.

 

 




