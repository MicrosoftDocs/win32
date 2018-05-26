---
title: Linked Objects
description: Linked Objects
ms.assetid: f39844ed-642f-47dd-b544-daeb7ea0a5c0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Linked Objects

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

An object can also be asked to enumerate the chunks of text "contained" in its linked objects. As with embedded objects, **IFilter** interface implementations are responsible for binding to the **IFilter** interface of linked objects, and then renumbering the chunks of the linked objects so that they appear to the original caller as chunks of the outer object. The same rules that apply to an embedding's chunks apply to a link's chunks. Use [IFILTER\_INIT\_SEARCH\_LINKS](/windows/win32/Filter/nf-filter-ifilter-init?branch=master) to control whether to search links.

The original source of a chunk (embedding, link, or top-level object) is not exposed by the **IFilter** interface. If the embedded or linked object cannot be filtered because it does not have a registered **IFilter** interface, the parent container should handle the situation gracefully by returning the error FILTER\_E\_EMBEDDING\_UNAVAILABLE and proceed to the next chunk.

 

 




