---
title: Creating IP Address Resources
description: The following code demonstrates the creation of an IP Address resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a082bb24-859d-4eae-9a83-967dd24929fa
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- resources Failover Cluster ,creating,IP Address
- IP Address resource type Failover Cluster ,resources,creating
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating IP Address Resources

The following code demonstrates the creation of an [IP Address](ip-address.md) resource.


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESCREATEIPADDRESS_CPP
#define _CLUSDOCEX_RESCREATEIPADDRESS_CPP


//--------------------------------------------------------------------
//  ClusDocEx_ResCreateIPAddress
//
//  Creates an IP Address resource and sets its 
//  required private properties.
//
//  Arguments:
//   IN HGROUP hGroup          Handle to the group in which to create the resource
//   IN LPWSTR lpszResName     Name of the new IP Address resource
//   IN LPWSTR lpszAddress     IP address supported by the resource
//   IN LPWSTR lpszNetwork     Network supported by the resource
//   IN LPWSTR lpszSubnetMask  Subnet mask supported by the resource
//
//  Return Value:
//     Resource handle (if successful) or NULL (if unsuccessful)
//--------------------------------------------------------------------
HRESOURCE ClusDocEx_ResCreateIPAddress
(
    IN HGROUP hGroup,
    IN LPWSTR lpszResName,
    IN LPWSTR lpszAddress,
    IN LPWSTR lpszNetwork,
    IN LPWSTR lpszSubnetMask
)
{
    HRESOURCE hIPRes;

    DWORD dwResult    = ERROR_SUCCESS;
    DWORD dwPropCount = 3;

    DWORD cb;
    DWORD cbPosition = 0;
    DWORD cbAddressEntrySize = 0;
    DWORD cbNetworkEntrySize = 0;
    DWORD cbMaskEntrySize = 0;
    DWORD cbPropListSize = 0;

    LPVOID lpAddressEntry;
    LPVOID lpNetworkEntry;
    LPVOID lpMaskEntry;
    LPVOID lpPropList;

    CLUSPROP_BUFFER_HELPER cbh_read, cbh_write;

//  Create the resource.

    hIPRes = CreateClusterResource( hGroup,
                                    lpszResName,
                                    L"IP Address",
                                    0 );

    if( hIPRes == NULL )
    {
        goto endf;
    }

//  Create a property list to set the required private properties.
//  This example uses ClusDocEx_CreatePropertyListEntry, which
//  is listed under "Creating Property Lists."

    lpAddressEntry = ClusDocEx_CreatePropertyListEntry(
                      L"Address",
                      CLUSPROP_SYNTAX_LIST_VALUE_SZ,
                      (lstrlenW( lpszAddress ) + 1 ) * sizeof( WCHAR ),  
                      (LPVOID) lpszAddress,
                      &amp;cbAddressEntrySize );

    lpNetworkEntry = ClusDocEx_CreatePropertyListEntry(
                      L"Network",
                      CLUSPROP_SYNTAX_LIST_VALUE_SZ,
                      (lstrlenW( lpszNetwork ) + 1 ) * sizeof( WCHAR ),  
                      (LPVOID) lpszNetwork,
                      &amp;cbNetworkEntrySize );

    lpMaskEntry = ClusDocEx_CreatePropertyListEntry(
                      L"SubnetMask",
                      CLUSPROP_SYNTAX_LIST_VALUE_SZ,
                      (lstrlenW( lpszSubnetMask ) + 1 ) * sizeof( WCHAR ),  
                      (LPVOID) lpszSubnetMask ,
                      &amp;cbMaskEntrySize );


    cbPropListSize = sizeof( DWORD ) + 
                     cbAddressEntrySize +
                     cbNetworkEntrySize +
                     cbMaskEntrySize ;

    lpPropList = LocalAlloc( LPTR, cbPropListSize );


//  Use cbh to write the property count (3) and the entries
//  to the property list buffer.

    cbh_write.pb = (PBYTE) lpPropList;

    *cbh_write.pdw = dwPropCount;

    cbPosition = sizeof( DWORD );

    cbh_read.pb = (PBYTE) lpAddressEntry;

    for( cb = 0 ; cb < cbAddressEntrySize ; cb++, cbPosition++ )
        cbh_write.pb[cbPosition] = cbh_read.pb[cb];

    cbh_read.pb = (PBYTE) lpNetworkEntry;

    for( cb = 0 ; cb < cbNetworkEntrySize ; cb++, cbPosition++ )
        cbh_write.pb[cbPosition] = cbh_read.pb[cb];

    cbh_read.pb = (PBYTE) lpMaskEntry;

    for( cb = 0 ; cb < cbMaskEntrySize ; cb++, cbPosition++ )
        cbh_write.pb[cbPosition] = cbh_read.pb[cb];

    dwResult = ClusterResourceControl( 
                   hIPRes,
                   NULL,
                   CLUSCTL_RESOURCE_SET_PRIVATE_PROPERTIES,
                   lpPropList,
                   cbPropListSize,
                   NULL,
                   0,
                   NULL );

endf:

    if( dwResult != ERROR_SUCCESS )
    {
        if( hIPRes )
        {
            DeleteClusterResource( hIPRes );
            CloseClusterResource( hIPRes );
            hIPRes = NULL;
        }
    }

    LocalFree( lpPropList );
    LocalFree( lpAddressEntry );
    LocalFree( lpNetworkEntry );
    LocalFree( lpMaskEntry );

    SetLastError( dwResult );

    return hIPRes;
}
//  end ClusDocEx_ResCreateIPAddress
//--------------------------------------------------------------------
#endif
```



 

 




