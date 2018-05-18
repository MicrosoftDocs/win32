---
title: Creating Network Name Resources
description: The following code demonstrates the creation of a Network Name resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2730daaf-6daf-4e9f-b794-710cda1ba22e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resources Failover Cluster ,creating, Network Name", "Network Name resource type Failover Cluster ,resources,creating"]
---

# Creating Network Name Resources

The following code demonstrates the creation of a [Network Name](network-name.md) resource.


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef CLUSDOCEX_RESCREATENETWORKNAME_CPP
#define CLUSDOCEX_RESCREATENETWORKNAME_CPP
//--------------------------------------------------------------------
//
//  ClusDocEx_ResCreateNetworkName
//
//  Creates a Network Name resource, 
//  sets its required private properties, 
//  and establishes a dependency on an IP Address resource.
//
//  Arguments:
//     IN HGROUP    hGroup         Group handle.
//     IN HRESOURCE hIPDependency  Handle to the IP Address dependency.
//     IN LPWSTR    lpszResName    Name of the new Network Name 
//                                 resource (the resource name).
//     IN LPWSTR    lpszNetName    Specifies the name of the network 
//                                 for which the Network Name resource
//                                 is being created. This value will
//                                 be used to set the Name private 
//                                 property.
//
//  Return Value:
//     Resource handle (if successful) or NULL (if unsuccessful)
//
//--------------------------------------------------------------------
HRESOURCE ClusDocEx_ResCreateNetworkName
(
    IN HGROUP    hGroup,
    IN HRESOURCE hIPDependency,
    IN LPWSTR    lpszResName,
    IN LPWSTR    lpszNetName
)
{
    HRESOURCE hNetNameRes = NULL;
    LPVOID lpPropList = NULL;
    LPVOID lpNameEntry = NULL;

    DWORD cb;
    DWORD cbPosition = 0;
    DWORD cbNameEntrySize = 0;
    DWORD cbPropListSize = 0;
    DWORD dwResult = ERROR_SUCCESS;

    CLUSPROP_BUFFER_HELPER cbh_read, cbh_write;

    hNetNameRes = CreateClusterResource( 
                      hGroup,
                      lpszResName,
                      L"Network Name",
                      0 );

    if( hNetNameRes == NULL )
    {
        dwResult = GetLastError();
        goto endf;
    }


//  Create a property list to set the Name private property.
//  This example uses ClusDocEx_CreatePropertyListEntry, which
//  is listed under "Creating Property Lists."

    lpNameEntry = ClusDocEx_CreatePropertyListEntry(
                      L"Name",
                      CLUSPROP_SYNTAX_LIST_VALUE_SZ,
                      (lstrlenW( lpszNetName ) + 1 ) * sizeof( WCHAR ),  
                      (LPVOID) lpszNetName,
                      &amp;cbNameEntrySize );


//  This is a single-value property list, thus the size is just
//  the size of the entry plus the size of the property count.

    cbPropListSize = sizeof( DWORD ) + cbNameEntrySize;

    lpPropList = LocalAlloc( LPTR, cbPropListSize );


//  Use cbh to write the property count (1) and the single entry
//  to the property list buffer.

    cbh_write.pb = (PBYTE) lpPropList;

    cbh_read.pb = (PBYTE) lpNameEntry;

    *cbh_write.pdw = 1;

    cbPosition = sizeof( DWORD );

    for( cb = 0 ; cb < cbNameEntrySize ; cb++, cbPosition++ )
        cbh_write.pb[cbPosition] = cbh_read.pb[cb];

    dwResult = ClusterResourceControl( 
                   hNetNameRes,
                   NULL,
                   CLUSCTL_RESOURCE_SET_PRIVATE_PROPERTIES,
                   lpPropList,
                   cbPropListSize,
                   NULL,
                   0,
                   NULL );

    if( dwResult != ERROR_SUCCESS )
    {
        goto endf;
    }


//  Establish the IP Address dependency.

    dwResult = AddClusterResourceDependency( 
                   hNetNameRes, 
                   hIPDependency );

endf:

    if( dwResult != ERROR_SUCCESS )
    {
        if( hNetNameRes != NULL )
        {
            DeleteClusterResource( hNetNameRes );
            CloseClusterResource( hNetNameRes );
            hNetNameRes = NULL;
        }
    }

    if( lpNameEntry != NULL ) LocalFree( lpNameEntry );
    if( lpPropList != NULL ) LocalFree( lpPropList );

    SetLastError( dwResult );

    return hNetNameRes;
}
//  end ClusDocEx_ResCreateNetworkName
//--------------------------------------------------------------------
#endif
```



 

 




