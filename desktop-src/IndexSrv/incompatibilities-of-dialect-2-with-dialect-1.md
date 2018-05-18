---
title: Incompatibilities of Dialect 2 with Dialect 1
description: Query Language Dialect 1 is the original query language introduced with Index Server 1.0.
ms.assetid: '8ad068ae-f088-4d16-bfaa-4983d5a00eba'
---

# Incompatibilities of Dialect 2 with Dialect 1

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Query Language Dialect 1 is the original query language introduced with Index Server 1.0. In general, it corresponds to the short form of Query Language Dialect 2. This topic describes the incompatibilities between the syntax of the short form of Dialect 2 and Dialect 1. For a reference to the syntax of Dialect 1, see [Query-Language Dialects](query-language-dialects.md).

Incompatibilities exist in several features, including the default phrase mode, the syntax of vector values, the syntax of term weighting, and language localization. The following table describes these differences in detail.



| Dialect 2                                                                                                                              | Dialect 1                                                                                                                                        | Remark                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Freetext is the default mode.<br/>                                                                                               | Phrase is the default mode.<br/>                                                                                                           | Freetext became default in Dialect 2.<br/>                                     |
| Multi-element vector is specified as (a;b;…;z).<br/>                                                                             | Multi-element vector is specified as {a,b,…,z}.                                                                                                  | "(", ";", and ")" in Dialect 2 were "{", ",", and "}" in Dialect 1.<br/>       |
| Weights are in the range 0.0 to 1.0.<br/> A weight of 0.1 for term T is specified by {weight value = 0.1} T.<br/>          | Weights are in the range 0 to 1000.<br/> A weight of 100 for term T is specified by T\[100\].<br/>                                   | The range for Dialect 2 allows greater resolution.<br/>                        |
| Boolean and proximity operator keywords are available only in their English spellings (**AND**, **OR**, **NOT**, **NEAR**).<br/> | Localized Boolean and proximity operator keywords are also available when the browser locale is set to certain non-English languages.<br/> | Dialect 2 keywords will not be localized to accommodate future additions.<br/> |



 

The following table lists the non-English supported languages and the localized keywords for the Boolean and proximity operators (**AND**, **OR**, **NOT**, **NEAR**). These keywords and the short forms (&, \|, !, ~) function identically in all supported languages.



| Language | Keywords               |
|----------|------------------------|
| German   | UND, ODER, NICHT, NAH  |
| French   | ET, OU, SANS, PRES     |
| Spanish  | Y, O, NO, CERCA        |
| Dutch    | EN, OF, NIET, NABIJ    |
| Swedish  | OCH, ELLER, INTE, NÄRA |
| Italian  | E, O, NO, VICINO       |



 

 

 





