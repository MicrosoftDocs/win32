---
title: CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS control code
description: Retrieves the intrinsic characteristics of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 02de0119-76af-445f-b107-f0ffa57e5ade
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_CHARACTERISTICS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_CHARACTERISTICS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS control code

Retrieves the intrinsic characteristics of a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) function.


```C++
ClusterResourceControl( 
  hResource,                            // resource handle
  hHostNode,                            // optional host node
  CLUSCTL_RESOURCE_GET_CHARACTERISTICS, // this control code
  NULL,                                 // input buffer (not used)
  0,                                    // input buffer size (not used)
  lpOutBuffer,                          // output buffer: DWORD bitmask
  cbOutBufferSize,                      // allocated buffer size (bytes)
  lpcbBytesReturned );                  // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) or [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, contains a **DWORD** bitmask describing the resource's characteristics as any combination of the following values enumerated from the [**CLUS\_CHARACTERISTICS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_characteristics) enumeration.

<dt>

<span id="CLUS_CHAR_UNKNOWN"></span><span id="clus_char_unknown"></span>

<span id="CLUS_CHAR_UNKNOWN"></span><span id="clus_char_unknown"></span>**CLUS\_CHAR\_UNKNOWN** (0x00000000)


</dt> <dd>

The resource has no known characteristics.

</dd> <dt>

<span id="CLUS_CHAR_QUORUM"></span><span id="clus_char_quorum"></span>

<span id="CLUS_CHAR_QUORUM"></span><span id="clus_char_quorum"></span>**CLUS\_CHAR\_QUORUM** (0x00000001)


</dt> <dd>

The resource can be selected as the quorum resource for the cluster.

</dd> <dt>

<span id="CLUS_CHAR_DELETE_REQUIRES_ALL_NODES"></span><span id="clus_char_delete_requires_all_nodes"></span>

<span id="CLUS_CHAR_DELETE_REQUIRES_ALL_NODES"></span><span id="clus_char_delete_requires_all_nodes"></span>**CLUS\_CHAR\_DELETE\_REQUIRES\_ALL\_NODES** (0x00000002)


</dt> <dd>

The resource cannot be deleted unless all nodes are active.

</dd> <dt>

<span id="CLUS_CHAR_LOCAL_QUORUM"></span><span id="clus_char_local_quorum"></span>

<span id="CLUS_CHAR_LOCAL_QUORUM"></span><span id="clus_char_local_quorum"></span>**CLUS\_CHAR\_LOCAL\_QUORUM** (0x00000004)


</dt> <dd>

The resource can be selected as the quorum resource in clusters configured using the **-localquorum** switch.

</dd> <dt>

<span id="CLUS_CHAR_REQUIRES_STATE_CHANGE_REASON"></span><span id="clus_char_requires_state_change_reason"></span>

<span id="CLUS_CHAR_REQUIRES_STATE_CHANGE_REASON"></span><span id="clus_char_requires_state_change_reason"></span>**CLUS\_CHAR\_REQUIRES\_STATE\_CHANGE\_REASON** (0x00000010)


</dt> <dd>

The [resource DLL](resource-dlls.md) will receive the [CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON](clusctl-resource-state-change-reason.md) control code.

</dd> <dt>

<span id="CLUS_CHAR_SINGLE_CLUSTER_INSTANCE"></span><span id="clus_char_single_cluster_instance"></span>

<span id="CLUS_CHAR_SINGLE_CLUSTER_INSTANCE"></span><span id="clus_char_single_cluster_instance"></span>**CLUS\_CHAR\_SINGLE\_CLUSTER\_INSTANCE** (0x00000040)


</dt> <dd>

Only one instance of this resource type is allowed in a cluster.

</dd> <dt>

<span id="CLUS_CHAR_SINGLE_GROUP_INSTANCE"></span><span id="clus_char_single_group_instance"></span>

<span id="CLUS_CHAR_SINGLE_GROUP_INSTANCE"></span><span id="clus_char_single_group_instance"></span>**CLUS\_CHAR\_SINGLE\_GROUP\_INSTANCE** (0x00000080)


</dt> <dd>

Only one instance of this resource type is allowed in a group.

</dd> </dl> </dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

Implementations of [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

Requests that the [Resource Monitor](resource-monitor.md) perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

Do not use the CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                            |
|----------------|--------------|--------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>      |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>           |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>            |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>        |
| Type bit       | 20           | External (0x0)<br/>                        |
| Operation code | 0 23         | **CLCTL\_GET\_CHARACTERISTICS** (0x5)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>          |



 

### Resource DLL Support

Optional. If you support CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS, use the output buffer to specify a value that accurately describes the resource.

-   If the resource is quorum-capable and you want users and applications to be able to select it as the quorum resource for the cluster, specify **CLUS\_CHAR\_QUORUM**. Note that if a resource that is not quorum-capable is selected as the quorum resource, the cluster becomes unusable.
-   If you want to prevent the resource from being deleted unless all nodes are active, specify **CLUS\_CHAR\_DELETE\_REQUIRES\_ALL\_NODES**. Attempts to delete the resource will fail and return **ERROR\_HOST\_NODE\_NOT\_AVAILABLE** unless all nodes are active.
-   If you want your resource DLL to receive the [CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON](clusctl-resource-state-change-reason.md) control code, specify **CLUS\_CHAR\_REQUIRES\_STATE\_CHANGE\_REASON**.

If you do not support this control code, return **ERROR\_INVALID\_FUNCTION** to allow the following default processing to occur.

-   If your resource DLL has [**Arbitrate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-parbitrate_routine) and [**Release**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-prelease_routine) entry points, the [Resource Monitor](resource-monitor.md) sets the **CLUS\_CHAR\_QUORUM** characteristic for the resource.
-   If your resource DLL does not have [**Arbitrate**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-parbitrate_routine) and [**Release**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-prelease_routine) entry points, the Resource Monitor clears the **CLUS\_CHAR\_QUORUM** characteristic for the resource.

For more information on the [**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine) entry point, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> <dt>

[**CLUS\_CHARACTERISTICS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_characteristics)
</dt> </dl>

 

 





