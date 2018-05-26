---
title: CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTY\_FMTS control code
description: Retrieves a property list describing the format of each cluster common property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 29f87a9c-98e2-46c0-94a0-634924e07930
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_GET_COMMON_PROPERTY_FMTS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_GET_COMMON_PROPERTY_FMTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTY\_FMTS control code

Retrieves a [property list](property-lists.md) describing the format of each cluster [common property](cluster-common-properties.md). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) function.


```C++
ClusterControl( hCluster,                               // cluster handle
                hHostNode,                              // optional node handle
                CLUSCTL_CLUSTER_GET_COMMON_PROPERTY_FMTS,  // this control code
                NULL,                                   // input buffer (not used)
                0,                                      // input buffer size (not used)
                lpOutBuffer,                            // output buffer: property list
                cbOutBufferSize,                        // output buffer size (bytes)
                lpcbBytesReturned );                    // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) describing the format of each [common property](cluster-common-properties.md).

</dd> </dl>

## Return value

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) returns one of the following values.

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

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTY\_FMTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                    |
|---------------------------|------------------|----------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_CLUSTER** (0x7)<br/>               |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                   |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                    |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_GET\_COMMON\_PROPERTY\_FMTS** (0x65)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                  |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master)
</dt> </dl>

 

 





