---
title: CLUSCTL\_NETWORK\_GET\_ID control code
description: Retrieves the cluster database subkey identifier for a network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c62818db-0766-4962-a8be-9b64ef348503
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_NETWORK_GET_ID control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_NETWORK_GET_ID
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_NETWORK\_GET\_ID control code

Retrieves the [cluster database](cluster-database.md) subkey identifier for a [network](networks.md). Applications use this [control code](about-control-codes.md) as a [**ClusterNetworkControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetworkcontrol) parameter.


```C++
ClusterNetworkControl( 
  hNetwork,                // network handle
  hHostNode,               // optional host node
  CLUSCTL_NETWORK_GET_ID,  // this control code
  NULL,                    // input buffer (not used)
  0,                       // input buffer size (not used)
  lpOutBuffer,             // output buffer: string (GUID)
  cbOutBufferSize,         // allocated buffer size (bytes)
  lpcbBytesReturned        // actual size of resulting data (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNetworkControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetworkcontrol).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a NULL-terminated Unicode string containing the **GUID** that identifies the network.

</dd> </dl>

## Return value

[**ClusterNetworkControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetworkcontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation Completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

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

The **GUID** string returned in *lpOutBuffer* resides in the cluster database under **HKEY\_LOCAL\_MACHINE\\Cluster\\Networks**.

ClusAPI.h defines the 32 bits of CLUSCTL\_NETWORK\_GET\_ID as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                      |
|----------------|--------------|--------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_NETWORK** (0x5)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>     |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>      |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>  |
| Type bit       | 20           | External (0x0)<br/>                  |
| Operation code | 0 23         | **CLCTL\_GET\_ID** (0x39)<br/>       |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>    |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Network Control Codes](network-control-codes.md)
</dt> <dt>

[**ClusterNetworkControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetworkcontrol)
</dt> </dl>

 

 





