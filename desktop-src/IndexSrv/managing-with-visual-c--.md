---
title: Managing with Visual C++
description: Managing with Visual C++
ms.assetid: 60e35eef-579c-4931-9b1d-eb8691fd5d61
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing with Visual C++

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

With Visual C++ and the [OLE DB Helper API](https://www.bing.com/search?q=OLE DB Helper API), you can locate the appropriate computer and catalog for a specified scope, query the state of a selected catalog, and control the state of a selected catalog.

The [ChgState Sample](chgstate-sample.md) illustrates using the OLE DB Helper API to manage Indexing Service. The following code segment uses the [CICAT\_\* constants](cicat-constants.md) and the [SetCatalogState](/windows/desktop/api/Ntquery/nf-ntquery-setcatalogstate) function to get or set the catalog state as specified by the input arguments to the application.


```C++
...
    if ( !wcscmp( pwcsAction, L"RO" ) )          // ReadOnly
        dwNewState = CICAT_READONLY;
    else if ( !wcscmp( pwcsAction, L"RW" ) )     // ReadWrite
        dwNewState = CICAT_WRITABLE;
    else if ( !wcscmp( pwcsAction, L"Stop" ) )   // Stop
        dwNewState = CICAT_STOPPED;
    else if ( !wcscmp( pwcsAction, L"GetState" ) ) // Get the current state
        dwNewState = CICAT_GET_STATE;
    else
    {
        fprintf( stderr, "Action undefined!\n" );
        exit(-1);
    }

    // call the API
    sc = SetCatalogState ( pwcsCatalog,
                           pwcsMachine,  
                           dwNewState,
                           &amp;dwOldState );
...
```



 

 




