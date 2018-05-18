---
title: CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTY\_FMTS control code
description: Retrieves a property list describing the format of each resource type private property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ddc3d89d-83ca-4d6f-92f5-0ad3917fdd1b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_GET_PRIVATE_PROPERTY_FMTS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_GET_PRIVATE_PROPERTY_FMTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTY\_FMTS control code

Retrieves a [property list](property-lists.md) describing the format of each resource type [private property](private-properties.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) parameter.


```C++
ClusterResourceTypeControl( hCluster,                                         // cluster handle
                            lpszResTypeName,                                  // resource type name
                            hHostNode,                                        // optional node handle
                            CLUSCTL_RESOURCE_TYPE_GET_PRIVATE_PROPERTY_FMTS,  // this control code
                            NULL,                                             // input buffer (not used)
                            0,                                                // input buffer size (not used)
                            lpOutBuffer,                                      // output buffer: property list
                            cbOutBufferSize,                                  // output buffer size (bytes)
                            lpcbBytesReturned );                              // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) describing the format of each [private property](private-properties.md).

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

By default, failover clusters do not define any private properties for resource types. CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTY\_FMTS does not retrieve information about unknown properties.

The property list returned by CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTY\_FMTS contains one entry for each resource type private property, formatted as follows.

-   A [**CLUSPROP\_PROPERTY\_NAME**](clusprop-property-name.md) structure describing the property name.
-   Alignment padding (see [**ALIGN\_CLUSPROP**](align-clusprop.md)).
-   A [**CLUSPROP\_WORD**](clusprop-word.md) structure describing the format of the property value.
-   A [**CLUSPROP\_SYNTAX**](clusprop-syntax.md) structure set to **CLUSPROP\_SYNTAX\_ENDMARK**, an enumerator from the [**CLUSTER\_PROPERTY\_SYNTAX**](cluster-property-syntax.md) enumeration.

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_PROPERTY\_FMTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                     |
|---------------------------|------------------|-----------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>         |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                    |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                     |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                 |
| Type bit<br/>       | 20<br/>    | External (0x1)<br/>                                 |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_GET\_PRIVATE\_PROPERTY\_FMTS** (0x8d)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                   |



 

### Resource DLL Support

Required if you define private properties for your resource type. Otherwise return **ERROR\_INVALID\_FUNCTION**. For more information on the [**ResourceTypeControl**](resourcetypecontrol.md) entry point, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

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
</dt> </dl>

 

 





