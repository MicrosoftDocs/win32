---
title: CLUSCTL\_CLUSTER\_ENUM\_COMMON\_PROPERTIES control code
description: Retrieves a list of the read/write cluster common property names.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 03fadf36-9a76-496e-a48b-c083c958b870
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_CLUSTER_ENUM_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_CLUSTER_ENUM_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_CLUSTER\_ENUM\_COMMON\_PROPERTIES control code

Retrieves a list of the read/write cluster [common property](common-properties.md) names. Applications use this [control code](about-control-codes.md) as a [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) parameter.


```C++
ClusterControl( hCluster,                 // cluster handle
  hHostNode,                              // optional node handle
  CLUSCTL_CLUSTER_ENUM_COMMON_PROPERTIES, // this control code
  NULL,                                   // not used
  0,                                      // not used
  lpOutBuffer,                            // output buffer: array of strings
  cbOutBufferSize,                        // output buffer size (bytes)
  lpcbBytesReturned );                    // resulting data size (bytes)
```



## Parameters

The following [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) function parameter is specific to the CLUSCTL\_CLUSTER\_ENUM\_COMMON\_PROPERTIES [control code](about-control-codes.md).

<dl> <dt>

*lpOutBuffer* \[out, optional\]
</dt> <dd>

On a successful return, *lpOutBuffer* contains an array of **NULL**-terminated Unicode strings with an additional **NULL** terminator appended to the last string. Each string in the array contains the name of a read/write cluster [common property](cluster-common-properties.md).

</dd> </dl>

## Return value

When the CLUSCTL\_CLUSTER\_ENUM\_COMMON\_PROPERTIES [control code](about-control-codes.md) is used as a possible value for *dwControlCode*, [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0 (0x0)

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. This value is returned if the output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The CLUSCTL\_CLUSTER\_ENUM\_COMMON\_PROPERTIES [control code](about-control-codes.md) returns only property names, not property values. To retrieve values for common cluster properties, use [CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES](clusctl-cluster-get-common-properties.md) and [CLUSCTL\_CLUSTER\_GET\_RO\_COMMON\_PROPERTIES](clusctl-cluster-get-ro-common-properties.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_CLUSTER\_ENUM\_COMMON\_PROPERTIES as follows.



| Component      | Bit location | Value                                      |
|----------------|--------------|--------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_CLUSTER** (0x7)            |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)             |
| Type bit       | 20           | External (0x0)                             |
| Operation code | 0 23         | **CLCTL\_ENUM\_COMMON\_PROPERTIES** (0x51) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)               |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Cluster Control Codes](cluster-control-codes.md)
</dt> <dt>

[CLUSCTL\_CLUSTER\_GET\_COMMON\_PROPERTIES](clusctl-cluster-get-common-properties.md)
</dt> <dt>

[CLUSCTL\_CLUSTER\_GET\_RO\_COMMON\_PROPERTIES](clusctl-cluster-get-ro-common-properties.md)
</dt> <dt>

[**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master)
</dt> </dl>

 

 





