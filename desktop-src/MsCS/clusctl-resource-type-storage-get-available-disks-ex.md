---
title: CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX control code
description: Retrieves information about storage class devices supported by a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e95877af-762c-4fce-95e5-cfa86cb27c9e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_STORAGE_GET_AVAILABLE_DISKS_EX control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_STORAGE_GET_AVAILABLE_DISKS_EX
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX control code

Retrieves information about storage class devices supported by a [resource type](resource-types.md). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) callback function. Unlike the [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md) control code, the [value list](value-lists.md) returned contains [**CLUSPROP\_PARTITION\_INFO\_EX**](clusprop-partition-info-ex.md) structures.


```C++
ClusterResourceTypeControl( hCluster,                  // cluster handle
                            lpszResTypeName,           // resource type name
                            hHostNode,                 // optional host node
                            CLUSCTL_RESOURCE_TYPE_STORAGE_GET_AVAILABLE_DISKS_EX,
                            NULL,                      // input buffer (not used)
                            0,                         // input buffer size (not used)
                            lpOutBuffer,               // output buffer: value list
                            cbOutBufferSize,           // allocated buffer size
                            lpcbBytesReturned );       // size of returned data
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [**ResourceTypeControl**](resourcetypecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a value list describing all available storage class devices in the cluster supported by the resource type specified by *lpszResTypeName*.

-   For information on the format of this list see [Value Lists for Storage Class Resources](value-lists-for-storage-class-resources.md).
-   A storage class device is available if it is not currently owned by a node. Because resources are always owned by a node at any point in time, storage class devices configured as resources will not be included in the returned value list.
-   Any given storage class resource can appear more than once in the list.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

Implementations of [**ResourceTypeControl**](resourcetypecontrol.md) can return the above values or the following value:

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX (0x020001f5) as follows.



| Component                 | Bit location     | Value                                                            |
|---------------------------|------------------|------------------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>                |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                           |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                            |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                        |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                        |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX** (0x1f5)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                          |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

### Resource DLL Support

Conditional. If your DLL handles [*quorum-capable resource*](q-gly.md#-wolf-quorum-capable-resource-gly) storage class resources, you must support the CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX control code. Create and return a value list formatted as described under *lpOutBuffer*. For more information, see [Creating a Value List](creating-value-lists.md) and [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

Otherwise, return **ERROR\_INVALID\_FUNCTION**.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md)
</dt> </dl>

 

 





