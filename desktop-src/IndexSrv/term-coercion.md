---
Description: Term Coercion
ms.assetid: 625ee0e6-fcae-49fe-a946-0c4659ba9a13
title: Term Coercion
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Term Coercion

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Term coercion allows a particular clause to force documents matching that clause to appear higher in the results ranking. Term coercion is similar to numeric input-term weighting, but it has been called out as a separate operator to allow search engines to implement coercion differently than input-term weighting. The implementation and exact behavior of coercion is left up to the query engine.

To coerce a clause in the query, specify the coerce tag as follows.

{coerce} *query-term*

> [!Note]  
> The coercion tag is a unary operator which works on the term to the right of the tag. No short-form representation is available and no close tag is specified or required.

 

 

 



