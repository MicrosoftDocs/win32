---
title: CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO control code
description: Retrieves information about a particular storage class resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e80dfab7-448a-4d68-aae8-c6b42c5dc6f9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO control code

Retrieves information about a particular [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function.


```C++
ClusterResourceControl( hResource,                              // resource handle
                        hHostNode,                              // optional host node
                        CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO, // this control code
                        NULL,                                   // not used
                        0,                                      // not used
                        lpOutBuffer,                            // output buffer: value list
                        cbOutBufferSize,                        // allocated buffer size (bytes)
                        lpcbBytesReturned );                    // size of output data (bytes)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) or [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [value list](value-lists.md) describing the storage class resource. For information on the format of this list see [Value Lists for Storage Class Resources.](value-lists-for-storage-class-resources.md).

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

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

Implementations of [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) can return the above values or the following value:

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

Do not use the CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO (0x01000191) as follows.



| Component                 | Bit location     | Value                                                  |
|---------------------------|------------------|--------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>            |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                 |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                  |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>              |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                              |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_STORAGE\_GET\_DISK\_INFO** (0x191)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                |



 

For more information, see [Control Code Architecture](control-code-architecture.md)

### Resource DLL Support

Conditional. You must support the CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO control code if your resource DLL handles storage class resources such as [*quorum-capable resources*](q-gly.md#-wolf-quorum-capable-resource-gly). Return a value list that fully describes the storage class resource. For information on working with value lists, see [Using Value Lists](using-value-lists.md).

The [Resource Monitor](resource-monitor.md) does not provide default handling.

For more information on the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md)
</dt> </dl>

 

 





