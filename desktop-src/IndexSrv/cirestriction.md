---
Description: CiRestriction
ms.assetid: e6cc3b5f-027a-44e8-b9f0-000887f59aec
title: CiRestriction
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CiRestriction

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Format: **CiRestriction**=*Query*

Specifies the query for doing hit-highlighting. The query string must be in escaped form, which means that spaces and other special characters have been converted to their respective ASCII codes. In an .htx file, the restriction can be escaped by using the **EscapeURL** keyword, as demonstrated in [Adding a Hit Highlighting Link to a Results Page](adding-a-hit-highlighting-link-to-a-results-page.md). This parameter is required.

 

 



