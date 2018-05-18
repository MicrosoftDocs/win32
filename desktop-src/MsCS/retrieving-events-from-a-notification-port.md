---
title: Retrieving Events from a Notification Port
description: To retrieve event notifications, set up a program loop that calls GetClusterNotify.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '63d705e2-59c8-43d3-916e-51701c6164c5'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["notification ports Failover Cluster , receiving events", "events Failover Cluster", "events Failover Cluster , receiving from a notification port"]
---

# Retrieving Events from a Notification Port

To retrieve event notifications, set up a program loop that calls [**GetClusterNotify**](getclusternotify.md). This function will return the type of event (*dwFilterType*), the event key or index (*dwNotifyKey*), and the name of the object affected (*lpszName*). Use this information to take appropriate action.

Note the potential for a race condition if multiple threads access the same notification port. For example, one thread could be calling [**CloseClusterNotifyPort**](closeclusternotifyport.md) to close the notification port while another thread, which has called [**GetClusterNotify**](getclusternotify.md), is waiting to retrieve information from the same port. Prevent this problem by having the thread that is calling **GetClusterNotify** check for a CLUSTER\_CHANGE\_HANDLE\_CLOSE event.

The following code fragment detects when a [resource](resources.md) is added to the [*cluster*](c-gly.md#-wolf-cluster-gly) and takes action if the new resource is a [Physical Disk](physical-disk.md).


```C++
// code fragment; all error handling omitted
while( 1 )
{
dwStatus = GetClusterNotify( hChange,
                             &amp;dwNotifyKey,
                             &amp;dwFilterType,
                             lpszObjName,
                             &amp;cchObjNameSize,
                             500 );
if( dwStatus == ERROR_SUCCESS )
{
    switch( dwNotifyKey )
    {
    case ResourceEvents:
        if( dwFilterType == CLUSTER_CHANGE_RESOURCE_ADDED )
        {
            // Use the object name to get a resource handle and check the resource type.
            hResource = OpenClusterResource( hCluster, lpszObjName );
            dwResult = ClusterResourceControl( hResource,
                                               NULL,
                                               CLUSCTL_RESOURCE_GET_RESOURCE_TYPE,
                                               NULL,
                                               0,
                                               lpszResType,
                                               cbAllocated,
                                               cbReturned );
            if( lstrcmpi( lpszResType, L"Physical Disk" ) == 0 )
            {
                // perform some action
            }
        }
        break;

    case 2:
    default:
        break;

    } // end switch
} // end if
} // end while
```



 

 




