---
title: Querying Component
description: Querying Component
ms.assetid: a6582e7a-5020-4aab-9b23-54a9a7c3b6bf
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Querying Component

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The Querying component takes a search string from a client composed in one of the supported query languages and, after appropriate processing, passes it to a query processor that searches the catalog to find matches.

The following files make up the Querying component.



| File Name   | Description                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Idq.dll     | [ISAPI extensions](programming-apis.md#-idxs-isapi-extensions-api) for Indexing Service.                                             |
| Ixsso.dll   | [Query Helper](programming-apis.md#-idxs-query-helper-api) automation objects ([Query](iixssoquery.md), [Utility](iixssoutil.md)). |
| msad\*.dll  | Microsoft [ActiveX Data Objects](programming-apis.md#-idxs-activex-data-objects-api) (ADOs).                                         |
| Ntquery.lib | [OLE DB Helper](programming-apis.md#-idxs-ole-db-helper-api) functions.                                                              |
| Query.dll   | [OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md).                                                     |



 

 

 




