---
Description: Site Server Predefined Views
ms.assetid: bd87090a-0af4-45e0-9fa3-90b6afb5a46b
title: Site Server Predefined Views
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Site Server Predefined Views

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The SQL extensions include several predefined views that you can use without writing an explicit [CREATE VIEW statement](create-view-statement.md). Because the predefined view names are permanent, they do not need to be preceded by the number sign (\#).

The following table lists the predefined views for Site Server, which are always available, regardless of the catalog you are currently using.



| Predefined View     | Properties                                                              | Description                  |
|---------------------|-------------------------------------------------------------------------|------------------------------|
| SSWEBINFO           | URL, DocTitle, Rank, size, write                                        | Standard Site Server results |
| SSEXTENDED\_WEBINFO | URL, DocTitle, Rank, HitCount, DocAuthor, Characterization, size, write | Extended Site Server results |



 

## Related topics

<dl> <dt>

[CREATE VIEW Statement](create-view-statement.md)
</dt> <dt>

[Indexing Service Predefined Views](indexing-service-predefined-views.md)
</dt> </dl>

 

 



