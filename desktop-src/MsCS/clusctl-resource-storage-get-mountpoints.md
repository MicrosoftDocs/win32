---
title: CLUSCTL\_RESOURCE\_STORAGE\_GET\_MOUNTPOINTS control code
description: Retrieves a list of path names for the specified partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fb27b836-6222-44d8-b56b-734b0299d4af'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_STORAGE_GET_MOUNTPOINTS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_GET_MOUNTPOINTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_STORAGE\_GET\_MOUNTPOINTS control code

Retrieves a list of path names for the specified partition. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](resourcecontrol.md) function.


```C++
ClusterResourceControl( hResource,                                // resource handle
                        hHostNode,                                // optional host node
                        CLUSCTL_RESOURCE_STORAGE_GET_MOUNTPOINTS, // dwControlCode
                        lpInBuffer,                               // pointer to a DWORD
                        cbInBufferSize,                           // input buffer size (bytes)
                        lpOutBuffer,                              // output buffer: path names
                        cbOutBufferSize,                          // output buffer size (bytes)
                        lpcbBytesReturned );                      // size of output data (bytes)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md) or [**ResourceControl**](resourcecontrol.md).

<dl> <dt>

*lpInBuffer* \[in\]
</dt> <dd>

Pointer to a **DWORD** specifying the partition number.

</dd> <dt>

*cbInBufferSize* \[in\]
</dt> <dd>

The size (in bytes) of the input buffer. This must be at least `sizeof(DWORD)`.

</dd> <dt>

*lpOutBuffer* \[out\]
</dt> <dd>

On a successful return, points to a list of path names for the specified volume. For more information, see [**GetVolumePathNamesForVolumeName**](https://msdn.microsoft.com/library/windows/desktop/aa364998).

</dd> <dt>

*cbOutBufferSize* \[in\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

</dd> <dt>

*lpBytesReturned* \[out, optional\]
</dt> <dd>

Returns the actual size (in bytes) of the data resulting from the operation. If this information is not needed, pass **NULL** for *lpBytesReturned*.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values:

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

Implementations of [**ResourceControl**](resourcecontrol.md) can return the above values or the following value:

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

Do not use the CLUSCTL\_RESOURCE\_STORAGE\_GET\_MOUNTPOINTS control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_GET\_MOUNTPOINTS as follows.



| Component                 | Bit location     | Value                                                   |
|---------------------------|------------------|---------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>             |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                  |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                   |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>               |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                               |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_STORAGE\_GET\_MOUNTPOINTS** (0x211)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                 |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

### Resource DLL Support

Conditional. You must support the CLUSCTL\_RESOURCE\_STORAGE\_GET\_MOUNTPOINTS control code if your resource DLL handles storage class resources such as [*quorum-capable resources*](q-gly.md#-wolf-quorum-capable-resource-gly). Return a value list that fully describes the storage class resource. For information on working with value lists, see [Using Value Lists](using-value-lists.md).

The [Resource Monitor](resource-monitor.md) does not provide default handling.

For more information on the [**ResourceControl**](resourcecontrol.md) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> <dt>

[**GetVolumePathNamesForVolumeName**](https://msdn.microsoft.com/library/windows/desktop/aa364998)
</dt> </dl>

 

 





