---
title: Architecture of Indexing Service
description: Architecture of Indexing Service
ms.assetid: 0a9f3e0d-b69e-4f4e-80c1-af174fecf93e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Architecture of Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The architecture of Indexing Service is designed around documents. It gathers and filters documents and then indexes the resulting words and properties from the documents into a catalog. Concurrently, Indexing Service processes queries for specified words and properties and then returns references to the documents in the catalog that contain the specified items.

This section illustrates the architecture of Indexing Service by describing the characteristics of documents; the components of Indexing Service that perform indexing on and querying of documents; and the flow of information from documents through the components of Indexing Service. The section consists of the following topics.

-   [Properties of Documents](properties-of-documents.md)
-   [Components of Indexing Service](components-of-indexing-service.md)
-   [Processing in Indexing Service](processing-in-indexing-service.md)

 

 




