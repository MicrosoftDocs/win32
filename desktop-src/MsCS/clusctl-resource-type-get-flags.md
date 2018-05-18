---
title: CLUSCTL\_RESOURCE\_TYPE\_GET\_FLAGS control code
description: Retrieves the flags that are set for a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a7ed60d5-cafe-4436-8cd3-e95eb89677a8'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_GET_FLAGS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_GET_FLAGS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_GET\_FLAGS control code

Retrieves the flags that are set for a [resource type](resource-types.md). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceTypeControl**](resourcetypecontrol.md) callback function.


```C++
ClusterResourceTypeControl( hCluster,            // cluster handle
                            lpszResTypeName,     // resource type name
                            hHostNode,           // optional host node
                            CLUSCTL_RESOURCE_TYPE_GET_FLAGS, // control code
                            NULL,                // input buffer (not used)
                            0,                   // input buffer size (not used)
                            lpOutBuffer,         // output buffer: DWORD bitmask
                            cbOutBufferSize,     // allocated buffer size
                            lpcbBytesReturned ); // size of returned data
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) or [**ResourceTypeControl**](resourcetypecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, contains a **DWORD** bitmask describing flags set for the resource type, as follows.



| Flag    | Description                                                                                  |
|---------|----------------------------------------------------------------------------------------------|
| 0       | No flags are defined for the resource type.                                                  |
| Nonzero | Indicates a user-defined flag created by a third party developer for a custom resource type. |



 

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values.

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

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_GET\_FLAGS as follows:



| Component                 | Bit location     | Value                                             |
|---------------------------|------------------|---------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>             |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                         |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_GET\_FLAGS** (0x9)<br/>            |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>           |



 

For more information, see [Control Code Architecture](control-code-architecture.md)

### Resource DLL Support

Optional. Support CLUSCTL\_RESOURCE\_TYPE\_GET\_FLAGS only if you define flags specific to the resource type. The [Failover Cluster API](the-server-cluster-api.md) reserves only the lower 16 bits of the **DWORD** bitmask. Use the upper 16 bits to define your own resource type-specific flags. Be sure to document or otherwise communicate what your flags do and how they should be used.

If you do not define resource type-specific flags, return **ERROR\_INVALID\_FUNCTION** to let the [Resource Monitor](resource-monitor.md) handle the operation. The Resource Monitor will read the Flags value from the resource type key in the [cluster database](cluster-database.md).

For more information on the [**ResourceTypeControl**](resourcetypecontrol.md) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Type Control Codes](external-resource-type-control-codes.md)
</dt> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> </dl>

 

 





