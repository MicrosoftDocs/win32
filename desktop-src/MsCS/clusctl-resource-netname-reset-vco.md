---
title: CLUSCTL\_RESOURCE\_NETNAME\_RESET\_VCO control code
description: Resets the password for a security principal on a client based on the client's alternate computer name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2560bf1a-6a02-4f71-8fb3-2303b77fe8ce'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_NETNAME_RESET_VCO control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_NETNAME_RESET_VCO
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_NETNAME\_RESET\_VCO control code

Resets the password for a security principal on a client based on the client's alternate computer name.

Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](clusterresourcecontrol.md) function.


```C++
ClusterResourceControl( hResource,                          // cluster handle
                        hHostNode,                          // optional node handle
                        CLUSCTL_RESOURCE_NETNAME_RESET_VCO, // this control code
                        lpInBuffer,                         // input buffer alternate computer name
                        nInBufferSize,                      // input buffer size
                        lpOutBuffer,                        // output buffer: NULL(not used)
                        cbOutBufferSize,                    // output buffer size
                        lpcbBytesReturned );                // returned data size
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md).

<dl></dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_NETNAME\_RESET\_VCO (0x01000185) as follows:



| Component                 | Bit location     | Value                                             |
|---------------------------|------------------|---------------------------------------------------|
| Object code<br/>    | 24–31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>       |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>            |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                 |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>         |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                         |
| Operation code<br/> | 0–23<br/>  | **CLCTL\_NETNAME\_RESET\_VCO** (0x185)<br/> |
| Access code<br/>    | 0–1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>           |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

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

 

 





