---
title: DBBYGUID
description: DBBYGUID
ms.assetid: 2126f665-7bac-49b2-b0b9-edd70e269c06
keywords:
- DBBYGUID
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBBYGUID

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBBYGUID** structure supplies supplementary information for a node.

``` syntax
typedef struct tagDBBYGUID { 
  BYTE *   pbInfo;  // extra node information, provider-specific
  DBLENGTH cbInfo;  // size of the data in pbInfo
  GUID     guid;    // this node's GUID
} DBBYGUID;
```

### Remarks

The information stored in the **pbInfo** member is provider-specific, and provides for operation extensibility.

 

 




