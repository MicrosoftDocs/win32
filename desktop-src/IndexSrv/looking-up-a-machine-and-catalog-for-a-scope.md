---
title: Looking Up a Machine and Catalog for a Scope
description: Looking Up a Machine and Catalog for a Scope
ms.assetid: db25f11d-725f-493f-b014-41d74a1b5055
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Looking Up a Machine and Catalog for a Scope

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following code segment from the **LookupCatalog** function of the sample uses the [**LocateCatalogs**](/windows/desktop/api/Ntquery/nf-ntquery-locatecatalogsa) function of the [OLE DB Helper API](https://www.bing.com/search?q=OLE DB Helper API) to find a catalog and machine matching the specified scope.


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



 

 




