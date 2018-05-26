---
title: CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX control code
description: Retrieves information about a particular storage class resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 64463e16-e4c3-4e18-9302-1af259a16545
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO_EX control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO_EX
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX control code

Retrieves information about a particular [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function. Unlike the [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md) control code, the [value list](value-lists.md) returned can contain [**CLUSPROP\_PARTITION\_INFO\_EX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info_ex?branch=master) structures.


```C++
ClusterResourceControl( hResource,                                 // resource handle
                        hHostNode,                                 // optional host node
                        CLUSCTL_RESOURCE_STORAGE_GET_DISK_INFO_EX, // this control code
                        NULL,                                      // not used
                        0,                                         // not used
                        lpOutBuffer,                               // output buffer: value list
                        cbOutBufferSize,                           // allocated buffer size (bytes)
                        lpcbBytesReturned );                       // size of output data (bytes)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) or [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [value list](value-lists.md) describing the storage class resource. For information on the format of this list see Remarks.

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

The value list returned in the output buffer pointed to by the *lpOutBuffer* parameter begins with either a **CLUSPROP\_SYNTAX\_DISK\_SIGNATURE** value that specifies the disk signature of an MBR partitioned disk, or if the disk is a **GUID** partitioning table (GPT) disk, a **CLUSPROP\_SYNTAX\_DISK\_GUID** value that specifies the disk **GUID**. Following this value the value list may contain the following values in any order:

-   A **CLUSPROP\_SYNTAX\_SCSI\_ADDRESS** value containing a [**CLUS\_SCSI\_ADDRESS**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_scsi_address?branch=master) structure that specifies the SCSI address of the device that is represented by the storage class resource, if applicable.
-   A **CLUSPROP\_SYNTAX\_DISK\_NUMBER** value containing a [**CLUSPROP\_DISK\_NUMBER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_dword?branch=master) structure that specifies the disk number of the storage class resource, if applicable.
-   A **CLUSPROP\_SYNTAX\_DISK\_SIZE** value containing a **ULARGE\_INTEGER** that specifies the total size of the disk, in bytes, of the storage class resource.
-   One or more **CLUSPROP\_SYNTAX\_PARTITION\_INFO\_EX** values, each containing a [**CLUSPROP\_PARTITION\_INFO\_EX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_partition_info_ex?branch=master) structure for each partition that has a basic volume that is assigned to the storage class resource, if applicable.

The value list is by a **CLUSPROP\_SYNTAX\_ENDMARK** value.

Do not use the CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX as follows.



| Component                 | Bit location     | Value                                                      |
|---------------------------|------------------|------------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                     |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                      |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                  |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                  |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_STORAGE\_GET\_DISK\_INFO\_EX** (0x1f1)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                    |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> <dt>

[CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md)
</dt> </dl>

 

 





