---
title: CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTY\_FMTS control code
description: Retrieves a property list describing the format of each resource private property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 755e1222-fd4c-40da-9ce4-d03192170c8d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_PRIVATE_PROPERTY_FMTS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_PRIVATE_PROPERTY_FMTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTY\_FMTS control code

Retrieves a [property list](property-lists.md) describing the format of each resource [private property](private-properties.md). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( hResource,                                  // cluster handle
                        hHostNode,                                  // optional node handle
                        CLUSCTL_RESOURCE_GET_PRIVATE_PROPERTY_FMTS, // this control code
                        NULL,                                       // input buffer (not used)
                        0,                                          // input buffer size (not used)
                        lpOutBuffer,                                // output buffer: property list
                        cbOutBufferSize,                            // output buffer size (bytes)
                        lpcbBytesReturned );                        // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) describing the format of each [private property](private-properties.md).

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

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

Implementations of [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Incorrect function. Requests that the [Resource Monitor](resource-monitor.md) perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

The property list returned by CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTY\_FMTS contains one entry for each resource private property, formatted as follows:

-   A [**CLUSPROP\_PROPERTY\_NAME**](/windows/previous-versions/ClusAPI/?branch=master) structure describing the property name.
-   Alignment padding (see [**ALIGN\_CLUSPROP**](/windows/previous-versions/ClusAPI/nf-clusapi-align_clusprop?branch=master)).
-   A [**CLUSPROP\_WORD**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_word?branch=master) structure describing the format of the property value.
-   A [**CLUSPROP\_SYNTAX**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_syntax?branch=master) structure set to **CLUSPROP\_SYNTAX\_ENDMARK**, an enumerator from the [**CLUSTER\_PROPERTY\_SYNTAX**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_property_syntax?branch=master) enumeration.

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTY\_FMTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                     |
|---------------------------|------------------|-----------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>               |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                    |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                     |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                 |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                 |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_GET\_PRIVATE\_PROPERTY\_FMTS** (0x8d)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                   |



 

### Resource DLL Support

Required. Return a [property list](property-lists.md) that describes the formats of all of your resource-specific private properties (see Remarks below).

As a general guideline, the Resource Monitor should handle all of the control codes for [common properties](common-properties.md), while your DLL should handle all control codes for [private properties](private-properties.md).

For more information on the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> </dl>

 

 





