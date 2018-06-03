---
title: Enumerating Cluster Objects
description: Enumeration is the process of listing all objects of a given type that are contained by, or that relate to, another object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 391b87d1-6765-45fd-bd27-37a1127e639a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster , enumerating
- enumerating objects Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Cluster Objects

Enumeration is the process of listing all [objects](cluster-objects.md) of a given type that are contained by, or that relate to, another object. For example, typical enumeration routines list all of the [resources](resources.md) in a [group](groups.md), all of the [dependencies](resource-dependencies.md) of a resource, or all of the [nodes](nodes.md) in a cluster. Enumeration allows you to search for objects with specific attributes or create and display object inventories.

The following table lists the kinds of information available through enumeration and the API element(s) used to perform the enumeration.



| Objects to enumerate                                                                | Function                                                              |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [dependencies](resource-dependencies.md) of a [resource](resources.md)<br/> | [**ClusterResourceEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum)<br/>         |
| dependents of a resource<br/>                                                 | [**ClusterResourceEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum)<br/>         |
| [groups](groups.md) in the cluster<br/>                                      | [**ClusterEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_enum)<br/>                         |
| [network interfaces](network-interfaces.md) available to a network<br/>      | [**ClusterNetworkEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_network_enum)<br/>           |
| network interfaces in a node<br/>                                             | [**ClusterNodeEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_node_enum)<br/>                 |
| [networks](networks.md) in the cluster<br/>                                  | [**ClusterEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_enum)<br/>                         |
| [nodes](nodes.md) in a cluster<br/>                                          | [**ClusterEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_enum)<br/>                         |
| possible owner nodes of a resource<br/>                                       | [**ClusterResourceEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum)<br/>         |
| possible owner nodes of a resource type<br/>                                  | [**ClusterResourceTypeEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_enum)<br/> |
| preferred owner nodes of a group<br/>                                         | [**ClusterGroupEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum)<br/>               |
| [resource types](resource-types.md) in a cluster<br/>                        | [**ClusterEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_enum)<br/>                         |
| [resources](resources.md) in a group<br/>                                    | [**ClusterGroupEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum)<br/>               |
| resources in a cluster<br/>                                                   | [**ClusterEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_enum)<br/>                         |
| network interfaces in a cluster<br/>                                          | [**ClusterEnum**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_enum)<br/>                         |



 

The following generalized procedure applies to the enumeration functions of any object. Substitute the name of the object (that is, node, network, group, or resource) for *Object*.

**To enumerate objects associated with *Object***

1.  Allocate an output buffer to receive the names of the objects to be enumerated. Note that the size of the buffer, passed as an input parameter, must be expressed as a count of characters and not a count of bytes.
2.  Open an enumeration handle by calling **Cluster*Object*OpenEnum**, specifying the objects to be enumerated in the *dwType* parameter.
3.  Execute a loop, performing the following steps with each iteration:

    1.  Call **Cluster*Object*Enum** to retrieve the name of the next object into the *lpszName* output buffer.
    2.  If **Cluster*Object*Enum** returns **ERROR\_MORE\_DATA**, reallocate the output buffer based on the count of characters returned in the *lpcchName* parameter. Note that the terminating **NULL** is not included in the count.
    3.  If **Cluster*Object*Enum** returns **ERROR\_NO\_MORE\_ITEMS**, terminate the loop.
    4.  Use the *lpszName* parameter according to the needs of the application. For example, *lpszName* could be used to open a handle to the object, which could then be used to retrieve the object's properties.
    5.  Increment the *dwIndex* parameter.

4.  Close the enumeration handle by calling **Cluster*Object*CloseEnum**.
5.  Deallocate the output buffer.

## Example Code

The following example enumerates the [resources](resources.md) in a [group](groups.md) and returns the results in a [value list](value-lists.md). This example calls other example functions presented elsewhere in this documentation. To locate these example functions, see the [Index of Examples](index-of-examples.md). Among these example functions is **ClusDocEx\_ListEntrySize**, which is defined in [ClusDocEx.h](clusdocex-h.md).


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_GRPENUMRESOURCES
#define _CLUSDOCEX_GRPENUMRESOURCES
//--------------------------------------------------------------------
//
//  ClusDocEx_GrpEnumResources
//
//  Enumerates the resources in a group and returns the names
//  in a value list.
//
//    IN HGROUP hGroup            Group handle.
//    IN OUT LPVOID lpOutBuffer   Allocated buffer for value list.
//    IN DWORD  cbOutBufferSize   Byte size of out buffer.
//    OUT LPDWORD lpcbResultSize  Byte size of resulting data.
//
//  Return Value.....lpOutBuffer...lpcbResultSize
//  ERROR_SUCCESS    value list    byte size of list
//  ERROR_MORE_DATA  undefined     byte size of list
//  Other            undefined     undefined
//
//--------------------------------------------------------------------
DWORD ClusDocEx_GrpEnumResources(
    IN HGROUP hGroup,
    IN OUT LPVOID lpOutBuffer,
    IN DWORD  cbOutBufferSize,
    OUT LPDWORD lpcbResultSize
)
{

//  hGroup       Group handle
//  hGroupEnum   Enumeration handle
//  dwResult     Captures return values
//  dwIndex      Enumeration index
//  dwType       Type of object to enumerate
//  cbNameAlloc  Allocated size of the name buffer
//  cchNameSize  Size of the resulting name as a count of wchars
//  cbNameSize   Size of the resulting name buffer in bytes
//  cbEntrySize  Size of the value list entry containing lpszName
//  lpszName     Buffer to hold enumerated names
//  cbh          Value list builder

    HGROUPENUM hGroupEnum = NULL;

    DWORD dwResult = ERROR_SUCCESS;
    DWORD dwIndex  = 0; 
    DWORD dwType   = CLUSTER_GROUP_ENUM_CONTAINS;

    DWORD cbNameAlloc = ClusDocEx_DEFAULT_CB;
    DWORD cchNameSize = 0;
    DWORD cbNameSize  = 0;
    DWORD cbEntrySize = 0;

    CLUSPROP_BUFFER_HELPER cbh;

    *lpcbResultSize = 0;

    LPWSTR lpszName = (LPWSTR) LocalAlloc( LPTR, 
                                           cbNameAlloc );
    if ( lpszName == NULL )
    {
        dwResult = GetLastError();
        goto endf;
    }

//  Open enumeration handle.

    hGroupEnum = ClusterGroupOpenEnum( hGroup, dwType );

    if ( hGroupEnum == NULL )
    {
        dwResult = GetLastError();
        goto endf;
    }
 
//  Prepare to build value list.  See "Using CLUSPROP_BUFFER_HELPER"

    cbh.pb = (LPBYTE) lpOutBuffer;

//  Enumeration loop.

    while( dwResult == ERROR_SUCCESS )
    {

    //  Make sure cchNameSize correctly reports the allocated size.

        cchNameSize = cbNameAlloc / sizeof( WCHAR );

        dwResult = ClusterGroupEnum( hGroupEnum,
                                     dwIndex,
                                     &amp;dwType,
                                     lpszName,
                                     &amp;cchNameSize );

    //  Reallocation routine

       if ( dwResult == ERROR_MORE_DATA )
        {
            cchNameSize++;  // terminating NULL
                           
            cbNameAlloc = cchNameSize / sizeof( WCHAR );

            LocalFree( lpszName );
        
            lpszName = (LPWSTR) LocalAlloc( LPTR, 
                                            cbNameAlloc );

            if ( lpszName == NULL )
            {
                dwResult = GetLastError();
                goto endf;
            }

            dwResult = ClusterGroupEnum( hGroupEnum,
                                         dwIndex,
                                         &amp;dwType,
                                         lpszName,
                                         &amp;cchNameSize );
        }

        if( dwResult == ERROR_SUCCESS ) 
        {

        //  Calculate sizes

            cchNameSize++;  // terminating NULL

            cbNameSize = cchNameSize * sizeof( WCHAR );

        //  ClusDocEx_ListEntrySize is defined in ClusDocEx.h       

            cbEntrySize = ClusDocEx_ListEntrySize( cbNameSize );  

        //  Update required size

            *lpcbResultSize += cbEntrySize;

            if( *lpcbResultSize < cbOutBufferSize )
            {

            //  Add value list entry
                        
                cbh.pStringValue->Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;

                cbh.pStringValue->cbLength = cbNameSize;

                StringCbCopy( cbh.pStringValue->sz, cbNameSize, lpszName );

                cbh.pb += cbEntrySize;

            }

        }
        else if( dwResult == ERROR_NO_MORE_ITEMS )
        {

        //  Add the endmark

            *lpcbResultSize += sizeof( DWORD );
            
            if( *lpcbResultSize <= cbOutBufferSize )
                *cbh.pdw = CLUSPROP_SYNTAX_ENDMARK;
            
        }
        else // enum failed for another reason
        {
 
        //  We don't have a reliable size

            *lpcbResultSize = 0;
        }
      
        dwIndex++;
    }
    //  end while


endf:

    cbh.pb = NULL;
    
    LocalFree( lpszName );

    if ( hGroupEnum != NULL )
        ClusterGroupCloseEnum( hGroupEnum );

    if( *lpcbResultSize > cbOutBufferSize )
        dwResult = ERROR_MORE_DATA;

    return dwResult;

} 
//  end ClusDocEx_GrpEnumResources
//--------------------------------------------------------------------
#endif
```



 

 





