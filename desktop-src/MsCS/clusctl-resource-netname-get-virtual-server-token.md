---
title: CLUSCTL\_RESOURCE\_NETNAME\_GET\_VIRTUAL\_SERVER\_TOKEN control code
description: Used by custom resources, services, and applications to get a token in the Network Names logon session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7a1033be-1b97-49d6-91f3-78f5efed1f4b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_NETNAME_GET_VIRTUAL_SERVER_TOKEN control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_NETNAME_GET_VIRTUAL_SERVER_TOKEN
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_NETNAME\_GET\_VIRTUAL\_SERVER\_TOKEN control code

Used by custom resources, services, and applications to get a token in the [Network Name](network-name.md)'s logon session. The token can then be used for impersonation. Applications use this [control code](about-control-codes.md) as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function.


```C++
ClusterResourceControl( hResource,                   // resource handle
  hHostNode,                                         // node handle
  CLUSCTL_RESOURCE_NETNAME_GET_VIRTUAL_SERVER_TOKEN, // this control code
  lpInBuffer,                                        // input buffer: CLUS_NETNAME_VS_TOKEN_INFO
  cbInBufferSize,                                    // input buffer size (bytes)
  lpOutBuffer,                                       // output buffer: HANDLE
  cbOutBufferSize,                                   // output buffer size (bytes)
  lpcbBytesReturned );                               // resulting data size (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*hHostNode* \[in, optional\]
</dt> <dd>

Handle to the local node to perform the operation. This operation will fail with **ERROR\_INVALID\_PARAMETER** if the node is remote.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

Points to a [**CLUS\_NETNAME\_VS\_TOKEN\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_netname_vs_token_info?branch=master) structure.

</dd> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a **HANDLE** to a duplicate of the token in the [Network Name](network-name.md)'s logon session.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

87 (0x57)

The node referenced by the *hHostNode* parameter is a remote node, the *cbInBufferSize* parameter is too small, or the *cbOutBufferSize* parameter is too small.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by the *lpOutBuffer* parameter was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of the *lpcbBytesReturned* parameter is unreliable.

</dd> </dl>

## Remarks

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_NETNAME\_GET\_VIRTUAL\_SERVER\_TOKEN as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                              |
|----------------|--------------|--------------------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>                        |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                             |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                              |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                          |
| Type bit       | 20           | External (0x0)<br/>                                          |
| Operation code | 0 23         | **CLCTL\_NETNAME\_GET\_VIRTUAL\_SERVER\_TOKEN** (0x16d)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                            |



 

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
</dt> <dt>

[**CLUS\_NETNAME\_VS\_TOKEN\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clus_netname_vs_token_info?branch=master)
</dt> </dl>

 

 





