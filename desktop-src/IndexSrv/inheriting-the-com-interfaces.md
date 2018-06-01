---
Description: Inheriting the COM Interfaces
ms.assetid: ab419547-87f8-41fe-a8f2-a538b835d8b5
title: Inheriting the COM Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Inheriting the COM Interfaces

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The filter-class factory inherits the [IClassFactory](https://www.bing.com/search?q=IClassFactory) interface. The filter class inherits the [IFilter](/windows/desktop/api/Filter/nn-filter-ifilter) interface and one or more derived [IPersist](https://www.bing.com/search?q=IPersist) interfaces. These interfaces are declared in files included from the mssdk\\include directory and have predefined interface identifiers (IIDs).

The filter class can inherit one or more of the [IPersistFile](https://www.bing.com/search?q=IPersistFile), [IPersistStorage](https://www.bing.com/search?q=IPersistStorage), and [IPersistStream](https://www.bing.com/search?q=IPersistStream) interfaces. The content-indexing client queries the filter through its [IUnknown](https://www.bing.com/search?q=IUnknown) interface to determine which of these interfaces to use when filtering content.

 

 



