---
title: Compound Words
description: Compound Words
ms.assetid: e3035226-b066-4528-9110-36f936d824b4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Compound Words

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

In some languages, such as German, nouns are compounded from simpler nouns. These compound nouns are too specific in meaning for reasonable query recall. For example, without decomposition, a query for "Versicherung" ("insurance") does not match "Lebensversicherungsgesellschaft" ("life-insurance salesman"). In cases such as this, it is recommended that word breakers break these compound words into base components during both index creation and query time. The German word breaker breaks "Lebensversicherungsgesellschaft" into the component words "Leben," "Versicherung," and "Gesellschaft." It applies the same decomposition at query time, along with optional stemming for each of the resultant terms.

 

 




