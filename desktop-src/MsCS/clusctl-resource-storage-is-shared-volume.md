---
title: CLUSCTL\_RESOURCE\_STORAGE\_IS\_SHARED\_VOLUME control code
description: Verifies that a storage class resource is a Cluster Shared Volume (CSV).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9CA2ED7A-21CD-4B0B-B252-0543C2E9B344
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_IS_SHARED_VOLUME control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_IS_SHARED_VOLUME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_STORAGE\_IS\_SHARED\_VOLUME control code

Verifies that a [*storage class resource*](https://www.bing.com/search?q=*storage class resource*) is a Cluster Shared Volume (CSV). Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) function.


```C++
ClusterResourceControl( hResource,     // resource handle
  hHostNode,                           // node handle
  CLUSCTL_RESOURCE_GET_FAILURE_INFO,   // this control code
  lpInBuffer,                          // input buffer
  cbInBufferSize,                      // input buffer size
  lpOutBuffer,                         // output buffer
  cbOutBufferSize,                     // output buffer
  lpBytesReturned );                   // resulting data size
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*hResource* \[in\]
</dt> <dd>

A handle to the affected resource.

</dd> <dt>

*hHostNode* \[in, optional\]
</dt> <dd>

A handle to the node that is to perform the operation. If **NULL**, the node that owns the resource identified by the *hResource* parameter will perform the operation.

</dd> <dt>

*lpInBuffer* \[in, optional\]
</dt> <dd>

A pointer to the input buffer that contains the data for the operation, or **NULL** if no information is needed.

</dd> <dt>

*cbInBufferSize* \[in\]
</dt> <dd>

The allocated size of of the *lpInBuffer* parameter, in bytes.

</dd> <dt>

*lpOutBuffer* \[out, optional\]
</dt> <dd>

A pointer to the output buffer that receives the data retrieved by the operation, or **NULL** if no data will is retrieved.

</dd> <dt>

*cbOutBufferSize* \[in\]
</dt> <dd>

The allocated size of of the *lpOutBuffer* parameter, in bytes.

</dd> <dt>

*lpBytesReturned* \[out, optional\]
</dt> <dd>

The actual size of the data retrieved by the operation, in bytes.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0 (0x0)

The operation completed successfully. The *lpBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**ERROR\_HOST\_NODE\_NOT\_RESOURCE\_OWNER**
</dt> <dd>

5015 (0x1397)

The node specified by the *hNode* parameter is not the node that owns the resource specified by the *hResource* parameter.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_IS\_SHARED\_VOLUME (0x010002A5) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                     |
|----------------|--------------|-----------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>               |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                    |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                     |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                 |
| Type bit       | 20           | External (0x0)<br/>                                 |
| Operation code | 0 23         | **CLCTL\_STORAGE\_IS\_SHARED\_VOLUME** (0x29B)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                   |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> </dl>

 

 





