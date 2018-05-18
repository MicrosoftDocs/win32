---
title: CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTY\_FMTS control code
description: Retrieves a property list describing the format of each resource common property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c68decf7-45c0-4d15-a419-adc73a5683c0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_GET_COMMON_PROPERTY_FMTS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_COMMON_PROPERTY_FMTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTY\_FMTS control code

Retrieves a [property list](property-lists.md) describing the format of each [resource common property](resource-common-properties.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter.


```C++
ClusterResourceControl( 
 hResource,                                  // resource handle
 hHostNode,                                  // optional node handle
 CLUSCTL_RESOURCE_GET_COMMON_PROPERTY_FMTS,  // this control code
 NULL,                                       // input buffer (not used)
 0,                                          // input buffer size (not used)
 lpOutBuffer,                                // output buffer: property list
 cbOutBufferSize,                            // output buffer size (bytes)
 lpcbBytesReturned                           // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) describing the format of each [resource common property](resource-common-properties.md).

</dd> </dl>

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

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_COMMON\_PROPERTY\_FMTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                         |
|----------------|--------------|-----------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)              |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                   |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                    |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                |
| Type bit       | 20           | External (0x0)                                |
| Operation code | 0–23         | **CLCTL\_GET\_COMMON\_PROPERTY\_FMTS** (0x65) |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)                  |



 

### Resource DLL Support

Use default. Return **ERROR\_INVALID\_FUNCTION** to let the Resource Monitor create the property list. The Resource Monitor will return a version-appropriate list of common resource properties.

As a general guideline, the Resource Monitor should handle all of the control codes for [common properties](common-properties.md), while your DLL should handle all control codes for [private properties](private-properties.md).

For more information on the [**ResourceControl**](resourcecontrol.md) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> </dl>

 

 





