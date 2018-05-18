---
title: Inheriting the COM Interfaces
description: Inheriting the COM Interfaces
ms.assetid: 'ab419547-87f8-41fe-a8f2-a538b835d8b5'
---

# Inheriting the COM Interfaces

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The filter-class factory inherits the [IClassFactory](_com_iclassfactory) interface. The filter class inherits the [IFilter](ifilter.md) interface and one or more derived [IPersist](_com_ipersist) interfaces. These interfaces are declared in files included from the mssdk\\include directory and have predefined interface identifiers (IIDs).

The filter class can inherit one or more of the [IPersistFile](_com_ipersistfile), [IPersistStorage](_com_ipersiststorage), and [IPersistStream](_com_ipersiststream) interfaces. The content-indexing client queries the filter through its [IUnknown](_com_iunknown) interface to determine which of these interfaces to use when filtering content.

 

 




