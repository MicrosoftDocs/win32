---
title: Using Visual C++ with Indexing Service APIs
description: Using Visual C++ with Indexing Service APIs
ms.assetid: e310c803-fea6-4fd6-b535-12c5033f31b1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Visual C++ with Indexing Service APIs

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When you use Indexing Service APIs with Visual C++, you typically have a choice of using the [OLE DB Provider API](https://www.bing.com/search?q=OLE DB Provider API) or the [OLE DB Helper API](https://www.bing.com/search?q=OLE DB Helper API). For the fastest execution, you usually will use the OLE DB Provider API. For information about using it with Indexing Service, see [Using OLE DB Provider for Indexing Service](using-ole-db-provider-for-indexing-service.md).

For easier programming, you usually use the OLE DB Helper API or a combination of that API and the OLE DB Provider API. With the OLE DB Helper API, you need to include the header file Ntquery.h in any source files in which you use the [Helper functions](functions.md). You also need to link the Ntquery.lib library with your application.

When you use any [programming elements from the OLE DB Provider API](ole-db-provider-for-indexing-service-reference.md), you may also need to include the following header files.

-   ledberr.h
-   ledb.h
-   mdtree.h

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 




