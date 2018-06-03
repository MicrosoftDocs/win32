---
title: Creating Failover Cluster Instances
description: To implement high availability for a server application or any other resource normally accessed by a computer name, you should configure the resource to run in the context of a failover cluster instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a9b44a2b-c2e7-4e4d-9bab-062e0a001208
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- virtual servers Failover Cluster , creating
- failover cluster instances Failover Cluster , creating
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Failover Cluster Instances

To implement high availability for a server application or any other resource normally accessed by a computer name, you should configure the resource to run in the context of a failover cluster instance. This task can be left to administrators, or you can write code to create a failover cluster instance specific to the needs of your application.

**To create a failover cluster instance**

1.  Create a [group](groups.md) (see [Creating Groups](creating-groups.md)) that contains an [IP Address](ip-address.md) resource, an [IPv6 Address](ipv6-address.md) resource, and/or an [IPv6 Tunnel Address](ipv6-tunnel-address.md) resource, a [Network Name](network-name.md) resource, your resource, and any other resources that must be in the same group.
2.  Call [**AddClusterResourceDependency**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_dependency) to establish the following dependencies:

    1.  Add the [IP Address](ip-address.md) resource, [IPv6 Address](ipv6-address.md) resource, and/or [IPv6 Tunnel Address](ipv6-tunnel-address.md) resource as dependencies of the [Network Name](network-name.md) resource.
    2.  Add either the [IP Address](ip-address.md) resource, [IPv6 Address](ipv6-address.md) resource, and/or [IPv6 Tunnel Address](ipv6-tunnel-address.md) resource or the [Network Name](network-name.md) resource as a dependencies of your resource.
    3.  Add other dependencies based on the requirements of your resource.

3.  Configure all required and other properties. See [Configuring Resources](configuring-resources.md).

## Example Code

The following code demonstrates the creation of a "bare bones" failover cluster instance—a group with an [IP Address](ip-address.md) resource and a [Network Name](network-name.md) resource. This example calls other example functions presented elsewhere in this documentation. To locate these example functions, see the [Index of Examples](index-of-examples.md).


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef CLUSDOCEX_GRPCREATEVIRTUALSERVER_CPP
#define CLUSDOCEX_GRPCREATEVIRTUALSERVER_CPP
//--------------------------------------------------------------------
//  ClusDocEx_GrpCreateVirtualServer
//
//  Configures a group as a failover cluster instance.
//
//  Arguments:
//    IN HCLUSTER hCluster         Cluster handle.
//    IN LPWSTR   lpszGroupName    Name of the new instance.
//    IN LPWSTR   lpszIPResName    Name of the IP Address resource
//    IN LPWSTR   lpszNetResName   Name of the Network Name resource
//    IN LPWSTR   lpszAddress      IP address of the instance.
//    IN LPWSTR   lpszNetworkName  Network name of the instance.
//    IN LPWSTR   lpszSubnetMask   Subnet mask for the instance. 
//
//  Return Value:
//     Group handle (if successful) or NULL (if unsuccessful)
//--------------------------------------------------------------------
HGROUP ClusDocEx_GrpCreateVirtualServer
(
  IN HCLUSTER hCluster,
  IN LPWSTR   lpszGroupName,
  IN LPWSTR   lpszIPResName,
  IN LPWSTR   lpszNetResName,
  IN LPWSTR   lpszIPAddress,
  IN LPWSTR   lpszNetworkName,
  IN LPWSTR   lpszSubnetMask
)
{
  HGROUP    hGroup       = NULL;
  HRESOURCE hIPAddress   = NULL;
  HRESOURCE hNetworkName = NULL;
  DWORD     dwResult     = ERROR_SUCCESS;


//  Create the group.

  hGroup = CreateClusterGroup( hCluster, lpszGroupName );
    
  if( hGroup == NULL )
   {
    dwResult = GetLastError();
    goto endf;
   }

  if( hGroup != NULL )
   {

    //  Create the IP Address resource.

    hIPAddress = ClusDocEx_ResCreateIPAddress( hGroup,
                                               lpszIPResName,
                                               lpszIPAddress,
                                               lpszNetworkName,
                                               lpszSubnetMask );

    if( hIPAddress == NULL )
     {
      dwResult = GetLastError();
      goto endf;
     }

    //  Create the Network Name resource.

    hNetworkName = ClusDocEx_ResCreateNetworkName( hGroup,
                                                   hIPAddress,
                                                   lpszNetResName,
                                                   lpszNetworkName );

    if( hNetworkName == NULL )
     {
      dwResult = GetLastError();
      goto endf;
     }
   }

endf:

  if( dwResult != ERROR_SUCCESS )
   {
    if( hNetworkName != NULL )
     {
      DeleteClusterResource( hNetworkName );

      //  Must always close handles after deletion. 

      CloseClusterResource( hNetworkName );
      hNetworkName = NULL;
     }

    if( hIPAddress != NULL )
     {
      DeleteClusterResource( hIPAddress);
      CloseClusterResource( hIPAddress);
      hIPAddress = NULL;
     }

    if( hGroup != NULL )
     {
      DeleteClusterGroup( hGroup );
      CloseClusterGroup( hGroup );
      hGroup = NULL;
     }
   }


  //  Close resource handles. 

  if( hNetworkName != NULL )
   {
    CloseClusterResource( hNetworkName );
   }
  if( hIPAddress != NULL )
   {
    CloseClusterResource( hIPAddress);
   }
    

  SetLastError( dwResult );

  return hGroup;
 }
//  end ClusDocEx_GrpCreateVirtualServer
//--------------------------------------------------------------------
#endif
```



 

 




