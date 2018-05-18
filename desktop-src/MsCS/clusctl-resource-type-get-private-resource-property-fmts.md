---
title: CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_RESOURCE\_PROPERTY\_FMTS control code
description: Returns a property list describing the format of each resource private property. Applications use this control code as a parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cc3dc11a-1019-4449-87da-45b1b254fec4'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_TYPE_GET_PRIVATE_RESOURCE_PROPERTY_FMTS control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_TYPE_GET_PRIVATE_RESOURCE_PROPERTY_FMTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_RESOURCE\_PROPERTY\_FMTS control code

Returns a [property list](property-lists.md) describing the format of each resource [private property](private-properties.md). Applications use this [control code](about-control-codes.md) as a parameter.


```C++
ClusterResourceTypeControl( hCluster                                // cluster handle
                            lpszResTypeName,                        // resource type name
                            hHostNode,                              // optional node handle
                            CLUSCTL_RESOURCE_TYPE_GET_PRIVATE_PROPERTY_FMTS, // this control code
                            NULL,                                   // input buffer (not used)
                            0,                                      // input buffer size (not used)
                            lpOutBuffer,                            // output buffer: property list
                            cbOutBufferSize,                        // output buffer size (bytes)
                            lpcbBytesReturned );                    // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceTypeControl**](clusterresourcetypecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) describing the format of each resource private property.

</dd> </dl>

## Return value

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md) returns one of the following values:

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

The property list returned by CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_RESOURCE\_PROPERTY\_FMTS contains one entry for each resource private property, formatted as follows:

-   A [**CLUSPROP\_PROPERTY\_NAME**](clusprop-property-name.md) structure describing the property name.
-   Alignment padding (see [**ALIGN\_CLUSPROP**](align-clusprop.md)).
-   A [**CLUSPROP\_WORD**](clusprop-word.md) structure describing the format of the property value.
-   A [**CLUSPROP\_SYNTAX**](clusprop-syntax.md) structure set to **CLUSPROP\_SYNTAX\_ENDMARK**.

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_TYPE\_GET\_PRIVATE\_RESOURCE\_PROPERTY\_FMTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                               |
|---------------------------|------------------|---------------------------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE\_TYPE** (0x2)<br/>                   |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                              |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                               |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                           |
| Type bit<br/>       | 20<br/>    | External (0x1)<br/>                                           |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_GET\_PRIVATE\_RESOURCE\_PROPERTY\_FMTS** (0x91)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                             |



 

### Resource DLL Support

Required. For more information on the [**ResourceTypeControl**](resourcetypecontrol.md) entry point function, see [Implementing ResourceTypeControl](implementing-resourcetypecontrol.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceTypeControl**](clusterresourcetypecontrol.md)
</dt> <dt>

[**ResourceTypeControl**](resourcetypecontrol.md)
</dt> </dl>

 

 





