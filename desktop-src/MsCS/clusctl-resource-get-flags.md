---
title: CLUSCTL\_RESOURCE\_GET\_FLAGS control code
description: Retrieves the flags that are set for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bee0f0c4-4d8a-4903-a9d0-6b5bc1fdfce4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_GET_FLAGS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_FLAGS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_GET\_FLAGS control code

Retrieves the flags that are set for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](resourcecontrol.md) callback function.


```C++
ClusterResourceControl( hResource,                  // resource handle
                        hHostNode,                  // optional host node
                        CLUSCTL_RESOURCE_GET_FLAGS, // this control code
                        NULL,                       // not used
                        0,                          // not used
                        lpOutBuffer,                // output buffer: DWORD bitmask
                        cbOutBufferSize,            // allocated buffer size (bytes)
                        lpcbBytesReturned );        // size of returned data (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md) or [**ResourceControl**](resourcecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, contains a **DWORD** bitmask describing flags set for the resource, as follows.

<dt>

0
</dt> <dd>

No flags are defined for the resource.

</dd> <dt>

<span id="CLUS_FLAG_CORE"></span><span id="clus_flag_core"></span>

<span id="CLUS_FLAG_CORE"></span><span id="clus_flag_core"></span>**CLUS\_FLAG\_CORE** (1)


</dt> <dd>

This flag of the [**CLUS\_FLAGS**](clus-flags.md) enumeration indicates that the resource or group is a [core resource](core-resources.md) essential to the cluster and cannot be deleted. Included in this group of essential resources are the cluster [IP Address](ip-address.md), the cluster [Network Name](network-name.md), and the [quorum resource](quorum-resource.md)

.

</dd> <dt>

<span id="Other_nonzero"></span><span id="other_nonzero"></span><span id="OTHER_NONZERO"></span>

<span id="Other_nonzero"></span><span id="other_nonzero"></span><span id="OTHER_NONZERO"></span>**Other nonzero**


</dt> <dd>

Indicates a user-defined flag created by a third party developer for a custom resource type.

</dd> </dl> </dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

Implementations of [**ResourceControl**](resourcecontrol.md) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Incorrect function. Requests that the [Resource Monitor](resource-monitor.md) perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

Do not use the CLUSCTL\_RESOURCE\_GET\_FLAGS control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_FLAGS as follows:



| Component                 | Bit location     | Value                                       |
|---------------------------|------------------|---------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>       |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>   |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                   |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_GET\_FLAGS** (0x9)<br/>      |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>     |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

### Resource DLL Support

Optional. Support CLUSCTL\_RESOURCE\_GET\_FLAGS only if you define flags specific to the resources supported by your DLL. The [Failover Cluster API](the-server-cluster-api.md) reserves only the lower 16 bits of the **DWORD** bitmask. Use the upper 16 bits to define your own resource-specific flags. Be sure to document or otherwise communicate what your flags do and how they should be used.

If you do not define resource-specific flags, return **ERROR\_INVALID\_FUNCTION** to let the [Resource Monitor](resource-monitor.md) handle the operation. The Resource Monitor will read the Flags value from the resource key in the [cluster database](cluster-database.md).

For more information on the [**ResourceControl**](resourcecontrol.md) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> <dt>

[**CLUS\_FLAGS**](clus-flags.md)
</dt> </dl>

 

 





