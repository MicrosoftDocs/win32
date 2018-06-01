---
Description: Persistent Handlers
ms.assetid: a4407ef9-7a1d-49f0-800a-1a19ade94a6d
title: Persistent Handlers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Persistent Handlers

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service uses a special binding procedure to access [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface implementations because the CiDaemon.exe process operates on the persistent image of an object and does not, as in the more common OLE case, bind to an in-memory image of an object. Using a persistent handler allows the CiDaemon.exe process to bind to only the **IFilter** interface for a file instead of being registered as the COM server for all clients that want to access the file.

Persistent handlers can be registered for a class identifier (CLSID) that represents a COM class and also for a file name extension. Persistent handlers registered for a file name extension take precedence over the persistent handler for a CLSID.

Indexing Service supplies [helper functions](functions.md) that implement a subset of the COM persistent handler functionality. You can use these functions to access the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface implementations for embedded or linked objects.

A persistent handler provides the same service for the persistent image of an object that the OLE running object table provides for the loaded, in-memory image. The persistent handler is the broker between the persistent state of an object and clients wishing to access that state. It is responsible for coordinating multiple-client access to the persistent state of an object.

Multiple handlers can be defined to provide behavior for a single persistent object. Each interface can specify a unique handler for only that interface. Potentially, multiple handlers that are ignorant of each other can all operate on the persistent image of the same object. It is the responsibility of the persistent handler to load the correct implementation for each interface.

The following registry entries are sufficient to load the implementation of the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface for objects of type SampleObject. In addition, a persistent handler can be registered for a file name extension that overrides the persistent handler registered for the class.

-   [Persistent Handlers Registered for a Class](persistent-handlers-registered-for-a-class.md)
-   [Persistent Handlers Registered for a File Extension](persistent-handlers-registered-for-a-file-extension.md)

 

 



