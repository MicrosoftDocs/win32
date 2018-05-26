---
title: ClusNetwork.NetworkID property
description: Unique network identifier for a network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c9091461-c6cf-4b2f-97ad-3fb639a09f5e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- NetworkID property Failover Cluster
- NetworkID property Failover Cluster , ClusNetwork object
- ClusNetwork object Failover Cluster , NetworkID property
topic_type:
- apiref
api_name:
- ClusNetwork.NetworkID
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusNetwork.NetworkID property

\[The **NetworkID** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the unique network identifier for a [network](networks.md).

This property is read-only.

## Syntax


```VB
ClusNetwork.NetworkID
```



## Property value

**String** that receives the **GUID** identifying the network.

## Remarks

The**NetworkID** of a network is stored in the [cluster database](cluster-database.md) under **HKEY\_LOCAL\_MACHINE**\\**Cluster**\\**Networks**\\.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetwork is defined as F2E606F2-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[CLUSCTL\_NETWORK\_GET\_ID](clusctl-network-get-id.md)
</dt> <dt>

[**ClusNetwork**](clusnetwork-object.md)
</dt> </dl>

 

 





