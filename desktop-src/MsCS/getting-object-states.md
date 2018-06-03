---
title: Getting Object States
description: The state of a cluster object indicates the operational status and availability of the object with respect to the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: de1d4ad2-3531-467e-a2e6-24d22514ce6e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster , retrieving states
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Object States

The state of a [cluster object](cluster-objects.md) indicates the operational status and availability of the object with respect to the [*cluster*](https://www.bing.com/search?q=*cluster*). Applications can check an object's state to verify that a requested state change has taken place, to determine whether an object is available for use, or simply to display the information to a user.

**To check an object's state**

1.  Use one of the following API elements to obtain state information about an object.

    

    | Cluster object                              | Function                                                           |
    |---------------------------------------------|--------------------------------------------------------------------|
    | [**Cluster**](cluster-object.md)           | [**GetNodeClusterState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_node_cluster_state)                 |
    | [Group](groups.md)                         | [**GetClusterGroupState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_group_state)               |
    | [Network](networks.md)                     | [**GetClusterNetworkState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_network_state)           |
    | [Network Interface](network-interfaces.md) | [**GetClusterNetInterfaceState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_net_interface_state) |
    | [Resource](resources.md)                   | [**GetClusterResourceState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state)         |

    

     

2.  The function will return an enumerated constant describing the object's state. If your routine will display the information to users, translate the numeric value into a meaningful message.

## Example Code

The following example calls [**GetClusterResourceState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state) and returns a string describing the state of a resource.


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESDESCRIBESTATE_CPP
#define _CLUSDOCEX_RESDESCRIBESTATE_CPP
//--------------------------------------------------------------------
//
//  ClusDocEx_ResDescribeState
//
//  Returns a description of the current state of a resource.
//  Callers must call LocalFree on the returned pointer.
//
//  Arguments:
//      IN HRESOURCE hResource    Handle to the resource to poll.
//
//  Return Value
//      String describing the state of the resource.  Call LocalFree
//      on the returned pointer.
//
//--------------------------------------------------------------------
LPWSTR
ClusDocEx_ResDescribeState( HRESOURCE hResource )
{
    DWORD dwState;

    LPWSTR lpszStatus = (LPWSTR) LocalAlloc( LPTR, ClusDocEx_DEFAULT_CB );

    dwState = GetClusterResourceState( hResource,
                                       NULL,
                                       NULL,
                                       NULL,
                                       NULL );

    if( lpszStatus != NULL )
    {
        switch( dwState )
        {
        case ClusterResourceInitializing:
            lpszStatus = L"Initializing: The resource is performing initialization.";
            break;

        case ClusterResourceOnline:
            lpszStatus = L"Online: The resource is operational and functioning normally.";
            break;

        case ClusterResourceOffline:
            lpszStatus = L"Offline: The resource is not operational.";
            break;

        case ClusterResourceFailed:
            lpszStatus = L"Failed: The resource not operational.";
            break;

        case ClusterResourcePending:
            lpszStatus = L"Pending: The resource is in the process of coming online or going offline.";
            break;

        case ClusterResourceOnlinePending:
            lpszStatus = L"Online Pending: The resource is in the process of coming online.";
            break;

        case ClusterResourceOfflinePending:
            lpszStatus = L"Offline Pending: The resource is in the process of going offline.";
            break;

        default:
            lpszStatus = L"Unknown state";
            break;
        }
    }

    return lpszStatus;
}    
//  end ClusDocEx_ResDescribeState
//--------------------------------------------------------------------
#endif
```



 

 




