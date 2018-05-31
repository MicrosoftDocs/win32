---
title: CONTAINS Operator
description: CONTAINS Operator
ms.assetid: 5d576ba2-00ad-4b84-ab94-c44a664b2e9c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CONTAINS Operator

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **CONTAINS** operator indicates a search for any of the specified words or phrases within a particular property. If no operator is specified, the **CONTAINS** operator is assumed. The **CONTAINS** operator contrasts with the relational operator "equals to" (=), which requires a match of the specified words or phrases and only those words or phrases. The **CONTAINS** operator is available only in its English spelling.

The following examples illustrate the use of the **CONTAINS** operator.



| To Search For                                       | Example                                                                                                                                                                                      | Results                                                                                   |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Documents that contain any of the terms.<br/> | {prop name=Contents} Contains {freetext} big red truck {/freetext}<br/>  Or <br/> $Contents contains big red truck<br/>  Or <br/> $Contents big red truck<br/> | Documents whose contents property contains the terms *big*, *red*, or *truck*.<br/> |
| Documents that contain a phrase.<br/>         | {prop name=All} Contains {phrase} big red truck {/phrase}{/prop}<br/>  Or <br/> @All contains "big red truck"<br/>  Or <br/> @All "big red truck"<br/>         | Documents with any property that contains the phrase *big red truck*.<br/>          |



 

 

 





