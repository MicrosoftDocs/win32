---
title: CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_NUMBER\_INFO control code
description: Retrieves the disk number of a physical disk resource in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09E0E0EF-57FF-4C6D-B79A-5173D9349510
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_STORAGE_GET_DISK_NUMBER_INFO control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_STORAGE_GET_DISK_NUMBER_INFO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_NUMBER\_INFO control code

Retrieves the disk number of a physical disk resource in a cluster. Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) parameter.


```C++
ClusterResourceControl( 
  hResource,                       // resource handle
  hHostNode,                       // optional node handle
  CLUSCTL_RESOURCE_STORAGE_GET_DISK_NUMBER_INFO,   // this control code
  lpInBuffer,                      // input buffer
  cbInBufferSize,                  // input buffer size (bytes)
  lpOutBuffer,                     // output buffer
  cbOutBufferSize,                 // output buffer size (bytes)
  lpcbBytesReturned );             // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [value list](value-lists.md) that contains the disk number.

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

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_NUMBER\_INFO (0x010001A1) as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                          |
|----------------|--------------|----------------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                    |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                         |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                          |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                      |
| Type bit       | 20           | External (0x0)<br/>                                      |
| Operation code | 0 23         | **CLCTL\_STORAGE\_GET\_DISK\_NUMBER\_INFO** (0x1A1)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                        |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                       |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**CLUS\_DISK\_NUMBER\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_clus_disk_number_info?branch=master)
</dt> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[Control Codes](about-control-codes.md)
</dt> </dl>

 

 





