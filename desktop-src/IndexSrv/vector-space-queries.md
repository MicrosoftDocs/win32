---
Description: Vector-Space Queries
ms.assetid: cd650438-0a47-4f8c-9496-3f3832385563
title: Vector-Space Queries
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Vector-Space Queries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Vector-space queries return documents that match a list of words and phrases. The rank of each document indicates how well the document matches the query. To specify a vector-space query, use the following syntax.

For Dialect 1

*method,term,term*

For Dialect 2

{vector RankMethod = *method*} {ve} *query terms* {/vector}

For Dialect 2, a vector-space query specification must be closed with the {/vector} tag. The RankMethod attribute specifies the ranking algorithm to use to evaluate the rank of a query match. The following table shows supported ranking methods for each dialect.



| Method              | Dialect 1   | Dialect 2          |
|---------------------|-------------|--------------------|
| Jaccard coefficient | --Jaccard-- | RankMethod=Jaccard |
| Dice coefficient    | --Dice--    | RankMethod=Dice    |
| Inner product       | --Inner--   | RankMethod=Inner   |
| Minimum             | --Minimum-- | RankMethod=Minimum |
| Maximum             | --Maximum   | RankMethod=Maximum |



 

If any other method is specified, it is ignored and the engine uses the default ranking algorithm, the Jaccard coefficient.

The {ve} tag is a vector element tag. It specifies that the following query specification is an element of the vector query. All the text following the {ve} tag up to the next {ve} tag is interpreted as a query. There is no closing tag for {ve}.

The following table gives several examples of vector-space queries.



| To Search For                                                                                           | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Results                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Documents containing a list of specified words.<br/>                                              | **Dialect 1**<br/> --Maximum--, light, bulb <br/> **Dialect 2**<br/> {vector RankMethod=Jaccard} {ve} light {ve} bulb {/vector}<br/> —Or—<br/> light, bulb<br/>                                                                                                                                                                                                                                                                | Documents with one or both words. Documents with both words are ranked higher than those with only one.<br/>                                                                                                                                                  |
| Documents containing a list of specified prefixes, words, and phrases.<br/>                       | **Dialect 1**<br/> —Jaccard--, invent\*, light\[333\], bulb\[100\], "light bulb"\[600\]<br/> **Dialect 2**<br/> {vector RankMethod=Jaccard} {ve} {generate method=prefix} invent {/generate} {ve} {weight value=0.3} light {weight value=0.1} bulb {weight value=0.6} {phrase} light bulb {/phrase} {/vector}<br/> —Or—<br/> invent\*, {weight value=0.3} light, {weight value=0.1} bulb, {weight value=0.6} "light bulb"<br/> | Documents containing words prefixed by *invent*, the words *light* and *bulb*, and the phrase *light bulb*. Documents containing the phrase *light bulb* are ranked before those containing *light*, which precede those containing *bulb*.<br/>              |
| Documents containing a complex list of words, phrases, property values, and inflected forms.<br/> | {vector RankMethod=Jaccard} {ve} {weight value=0.2} printers **‹**OR{coerce} "print driver" **›**{ve} {prop name = DocTitle} {freetext} Hewlett Packard HP laserjet laser printer {/freetext} {ve} @contents hang\*\* {/vector}<br/>                                                                                                                                                                                                                         | Documents containing the word *printers***‹** or the phrase *print driver***›**; the value-type property DocTitle, which contains any of the words *Hewlett*, *Packard*, *HP*, *laserjet*, *laser*, *printer*; or inflectional forms of the word *hang*.<br/> |



 

 

 




