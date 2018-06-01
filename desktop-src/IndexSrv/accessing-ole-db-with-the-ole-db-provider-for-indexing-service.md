---
Description: Accessing OLE DB with the OLE DB Provider for Indexing Service
ms.assetid: 9f0e2224-f652-4645-bcce-d8e82dbf6682
title: Accessing OLE DB with the OLE DB Provider for Indexing Service
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Accessing OLE DB with the OLE DB Provider for Indexing Service

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This section includes information on how to access OLE DB through the OLE DB Provider for Indexing Service.

Indexing Service supports command-tree extensions for OLE DB, which are a part of OLE DB 2.5. To enable command-tree definitions in Oledb.h, define the constant OLEDBVER in program source files before including Oledb.h:


```
#define OLEDBVER 0x250
```



For more information on property sets supported by this provider, see [Property Sets and Property Groups](https://msdn.microsoft.com/windows/desktop/4307e19f-e34e-4cd2-af15-8a67f7e8c24c).

The OLE DB provider for Indexing Service provides read-only access to the content and property indexes created by the indexing process. Clients of Indexing Service are OLE DB consumers of the Indexing Service data source object (DSO) that represents the content and property indexes.

The class identifier (CLSID) for the Indexing Service DSO is [CLSID\_INDEX\_SERVER\_DSO](data-source-object-constant.md). Consumers use the CLSID to create instances of provider DSOs that expose the initialization interfaces that allow the consumers to connect to the underlying Indexing Service indexes.

The following example illustrates this.


```
#include "Ntquery.h"
IDBInitialize *pIDBInit;
HRESULT hr;
 
hr = CoCreateInstance( CLSID_INDEX_SERVER_DSO,
                       0,
                       CLSCTX_INPROC_SERVER,
                       IID_IDBInitialize,
                       (void **) &amp;pIDBInit );
If (FAILED(hr))
(
  // Display error
) 
```



 

 



