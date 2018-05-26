---
title: Using Object Handles
description: Most of the Cluster Object Management Functions require an object handle as an input parameter. Therefore, one of the first steps in any object management routine is to obtain a handle to the object, and one of the last steps is to close the handle.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 709effda-5ff1-439e-805a-9169ca63c182
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- handles Failover Cluster ,using
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Object Handles

Most of the [Cluster Object Management Functions](cluster-object-management-functions.md) require an [object](cluster-objects.md) handle as an input parameter. Therefore, one of the first steps in any object management routine is to obtain a handle to the object, and one of the last steps is to close the handle.

The following table lists cluster object handles and the functions used to obtain the handles (note that the [Failover Cluster API](the-server-cluster-api.md) does not define handles for [resource types](resource-types.md)).



| Handle                                      | Function                                                                                                                                      |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [*Cluster*](c-gly.md#-wolf-cluster-gly)    | [**OpenCluster**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster?branch=master)<br/> [**CloseCluster**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster?branch=master)<br/>                                                 |
| [Node](nodes.md)                           | [**OpenClusterNode**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_node?branch=master)<br/> [**CloseClusterNode**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_node?branch=master)<br/>                                 |
| [Network](networks.md)                     | [**OpenClusterNetwork**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_network?branch=master)<br/> [**CloseClusterNetwork**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_network?branch=master)<br/>                     |
| [Network interface](network-interfaces.md) | [**OpenClusterNetInterface**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_net_interface?branch=master)<br/> [**CloseClusterNetInterface**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_net_interface?branch=master)<br/> |
| [Group](groups.md)                         | [**OpenClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_group?branch=master)<br/> [**CloseClusterGroup**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_group?branch=master)<br/>                             |
| [Resource](resources.md)                   | [**OpenClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_resource?branch=master)<br/> [**CloseClusterResource**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_resource?branch=master)<br/>                 |



 

The following generalized procedure applies to opening a handle to any object. Substitute the name of the object (that is, [node](nodes.md), [network](networks.md), [network interface](network-interfaces.md), [group](groups.md), or [resource](resources.md)) for &lt;Object&gt;.

**To open an object handle**

1.  Review the [recommendations and cautions](recommendations-and-cautions.md) related to object handles. See [LPC and RPC Handles](lpc-and-rpc-handles.md).
2.  Open a cluster handle by calling [**OpenCluster**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster?branch=master)
3.  Open the object handle by calling [**OpenCluster**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster?branch=master). Pass the cluster handle obtained from step 1 as well as the name of the object.
4.  Be sure to close any handles you no longer need. However, never close a cluster handle while object handles obtained from it are still in use.

## Example

The following example provides two functions: *ClusDocEx\_OpenLocalClusterWithName* and *ClusDocEx\_ResAddPossibleOwner*. The first function returns an RPC cluster handle by using [**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295) to supply a name for [**OpenCluster**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster?branch=master). The second function illustrates a call to [**AddClusterResourceNode**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_add_cluster_resource_node?branch=master), which requires a resource handle and a node handle.


```C++

//////////////////////////////////////////////////////////////////////


#ifndef _CLUSDOCEX_OPENLOCALCLUSTERWITHNAME
#define _CLUSDOCEX_OPENLOCALCLUSTERWITHNAME

//--------------------------------------------------------------------
//
//  ClusDocEx_OpenLocalClusterWithName
//
//  Gets the name of the local node, then 
//  uses this name to open a cluster handle.
//
//  Returns an RPC cluster handle or NULL if unsuccessful.
//
//--------------------------------------------------------------------
HCLUSTER ClusDocEx_OpenLocalClusterWithName()
{

  HCLUSTER hCluster        = NULL;
  DWORD    dwResult        = ERROR_SUCCESS;
  DWORD    cchNameSize     = MAX_COMPUTERNAME_LENGTH + 1;
  LPWSTR   lpszClusterName = (LPWSTR) LocalAlloc( LPTR, 
                                                  cchNameSize * sizeof( WCHAR ) );

  if( lpszClusterName != NULL )
  {

    //  Get the name of the local node.
    //  Using a name instead of NULL in OpenCluster 
    //  creates an RPC handle.

    if( GetComputerName( lpszClusterName, &amp;cchNameSize ) )
      hCluster = OpenCluster( lpszClusterName );

    dwResult = GetLastError();
        
    LocalFree( lpszClusterName );
  }

  SetLastError( dwResult );

  return hCluster;
}
//  end ClusDocEx_OpenLocalClusterWithName
//--------------------------------------------------------------------
#endif


//////////////////////////////////////////////////////////////////////


#ifndef _CLUSDOCEX_RESADDPOSSIBLEOWNER_CPP
#define _CLUSDOCEX_RESADDPOSSIBLEOWNER_CPP
//--------------------------------------------------------------------
//  ClusDocEx_ResAddPossibleOwner()
//
//  Adds a node to a resource's list of possible owner nodes.
//
//  Arguments:
//      IN LPWSTR lpszResourceName  Name of the resource.
//      IN LPWSTR lpszNodeName      Name of the new possible owner.
//      IN LPWSTR lpszClusterName   Specifies the cluster name
//                                  Can be NULL.
//
//  Return Value:
//      Returns ERROR_SUCCESS if successful, 
//      otherwise returns a system error code.
//--------------------------------------------------------------------
DWORD ClusDocEx_ResAddPossibleOwner( IN LPWSTR lpszResourceName,
                               IN LPWSTR lpszNodeName,
                               IN LPWSTR lpszClusterName
)
{

  HCLUSTER  hCluster  = NULL;
  HNODE     hNode     = NULL;
  HRESOURCE hResource = NULL;
  DWORD     dwResult  = ERROR_SUCCESS;

//  Using a name produces an RPC handle.

  if( lpszClusterName == NULL )
    hCluster = ClusDocEx_OpenLocalClusterWithName();
  else
    hCluster = OpenCluster( lpszClusterName );

//  Verify handle before proceeding.

  if( hCluster == NULL )
  {
    //  Handle error.
    dwResult = GetLastError();
    goto endf;
  }

  hResource = OpenClusterResource( hCluster, lpszResourceName );

  if( hResource == NULL )
  {
    //  Handle error.
    dwResult = GetLastError();
    goto endf;
  }

  hNode = OpenClusterNode( hCluster, lpszNodeName );

  if( hNode == NULL )
  {
    //  Handle error.
    dwResult = GetLastError();
    goto endf;
  }


//  Add the node to the resource's possible owners list.

  dwResult = AddClusterResourceNode( hResource, hNode );

//  Note that hResource and hNode were obtained from the 
//  same cluster handle. Thus they are both guaranteed 
//  to be LPC or RPC handles. The cluster handle in this
//  implementation will always be an RPC handle.

endf:

//  Close all handles. Close the cluster handle last.

  if( hNode!= NULL )     CloseClusterNode( hNode );
  if( hResource!= NULL ) CloseClusterResource( hResource );
  if( hCluster!= NULL )  CloseCluster( hCluster );

  return dwResult;

}
//  end ClusDocEx_ResAddPossibleOwner
#endif
```



 

 





