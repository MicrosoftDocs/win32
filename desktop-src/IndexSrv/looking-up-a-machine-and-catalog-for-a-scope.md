---
title: Looking Up a Machine and Catalog for a Scope
description: Looking Up a Machine and Catalog for a Scope
ms.assetid: db25f11d-725f-493f-b014-41d74a1b5055
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Looking Up a Machine and Catalog for a Scope

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following code segment from the **LookupCatalog** function of the sample uses the [**LocateCatalogs**](/windows/win32/Ntquery/nf-ntquery-locatecatalogsa?branch=master) function of the [OLE DB Helper API](programming-apis.md#-idxs-ole-db-helper-api) to find a catalog and machine matching the specified scope.


```C++
...
    HRESULT hr = LocateCatalogs( pwcScope,       // scope to lookup
                                 0,              // go with the first match
                                 pwcMachine,     // returns the machine
                                 &amp;cwcMachine,    // buffer size in/out
                                 pwcCatalog,     // returns the catalog
                                 &amp;cwcCatalog );  // buffer size in/out
...
```



 

 




