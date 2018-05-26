---
title: Filter DLLs
description: Filter DLLs
ms.assetid: 6f7fac27-df98-4277-9e45-62ca41189ca3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Filter DLLs

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Filter DLLs allow a client to extract text information from the persistent representation of the contents and properties of a file. The Indexing Service filtering process CiDaemon.exe binds to the persistent handler for the [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) interface implementation for the COM class of a file or for its registered file name extension. For details about how this occurs, see [Persistent Handlers](persistent-handlers.md).

Every time it starts, Indexing Service registers DLLs, including persistent handlers, if they are listed in the registry key **HKLM\\system\\currentcontrolset\\control\\contentindex\\DllsToRegister**.

To remove a filter DLL, delete the **PersistentHandler** registry entry associated with a document type and the filter DLL registry entry. (See [Finding the Filter DLL for a File](finding-the-filter-dll-for-a-file.md) for more information). Once you have found the correct **PersistentHandler** entry, you can unregister it with the following syntax:

**Regsvr32.exe /u filter.dll**

This section contains topics that describe how to use the filter DLLs:

-   [Indexing Service Implementations of IFilter](indexing-service-implementations-of-ifilter.md). A summary of the filter DLLs supplied with Indexing Service.
-   [Persistent Handlers](persistent-handlers.md). A brief description of how you bind to an [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) implementation to call its methods and properties.
-   [Finding the Filter DLL for a File](finding-the-filter-dll-for-a-file.md). A description of how to find the filter DLL for a specific file type.

 

 




