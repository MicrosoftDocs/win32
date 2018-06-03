---
title: CLUSCTL\_RESOURCE\_TYPE\_GET\_CHARACTERISTICS control code
description: Retrieves the intrinsic characteristics of a resource type. Applications use this control code as a ClusterResourceTypeControl parameter, and resource DLLs receive the control code as a parameter to the ResourceTypeControl function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d968810f-cd95-43a8-8897-43ebf0bd6f08
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_TYPE_GET_CHARACTERISTICS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_GET_CHARACTERISTICS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_TYPE\_GET\_CHARACTERISTICS control code

Retrieves the intrinsic characteristics of a [resource type](resource-types.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) function.


```C++
ClusterResourceTypeControl( 
  hCluster,                                  // cluster handle
  lpszResTypeName,                           // resource type name
  hHostNode,                                 // optional host node
  CLUSCTL_RESOURCE_TYPE_GET_CHARACTERISTICS, // this control code
  NULL,                                      // input buffer (not used)
  0,                                         // input buffer size (not used)
  lpOutBuffer,                               // output buffer: DWORD bitmask
  cbOutBufferSize,                           // allocated buffer size (bytes)
  lpcbBytesReturned );                       // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) or [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, contains a **DWORD** bitmask describing the resource type's characteristics as one of the following values enumerated from the [**CLUS\_CHARACTERISTICS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_characteristics) enumeration.

<dt>

<span id="CLUS_CHAR_UNKNOWN"></span><span id="clus_char_unknown"></span>

<span id="CLUS_CHAR_UNKNOWN"></span><span id="clus_char_unknown"></span>**CLUS\_CHAR\_UNKNOWN** (0x00000000)


</dt> <dd>

Resources of this type have no known characteristics.

</dd> <dt>

<span id="CLUS_CHAR_QUORUM"></span><span id="clus_char_quorum"></span>

<span id="CLUS_CHAR_QUORUM"></span><span id="clus_char_quorum"></span>**CLUS\_CHAR\_QUORUM** (0x00000001)


</dt> <dd>

Resources of this type are capable of being the [quorum resource type](quorum-resource.md) for a cluster.

</dd> <dt>

<span id="CLUS_CHAR_DELETE_REQUIRES_ALL_NODES"></span><span id="clus_char_delete_requires_all_nodes"></span>

<span id="CLUS_CHAR_DELETE_REQUIRES_ALL_NODES"></span><span id="clus_char_delete_requires_all_nodes"></span>**CLUS\_CHAR\_DELETE\_REQUIRES\_ALL\_NODES** (0x00000002)


</dt> <dd>

Resources of this type cannot be deleted unless all nodes are active.

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

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_GET\_CHARACTERISTICS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                             |
|----------------|--------------|---------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>             |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit       | 20           | External (0x0)<br/>                         |
| Operation code | 0 23         | **CLCTL\_GET\_CHARACTERISTICS** (0x5)<br/>  |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>           |



 

### Resource DLL Support

Optional. If you do not support the control code, return **ERROR\_INVALID\_FUNCTION** to let the [Resource Monitor](resource-monitor.md) read the Characteristics value from the resource type key in the [cluster database](cluster-database.md).

If you do support CLUSCTL\_RESOURCE\_TYPE\_GET\_CHARACTERISTICS, return a value that accurately describes the [resources](resources.md) supported by the resource type. For more information, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](clusctl-resource-get-characteristics.md).

For more information on the [**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine) entry point function, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcetypecontrol)
</dt> <dt>

[**ResourceTypeControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_type_control_routine)
</dt> <dt>

[**CLUS\_CHARACTERISTICS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clus_characteristics)
</dt> </dl>

 

 





