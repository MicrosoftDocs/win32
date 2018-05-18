---
title: ClusNetwork.NetInterfaces property
description: ClusNetworkNetInterfaces collection providing access to the network interfaces in the network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dbb51326-42a1-4b93-b7ab-a9b645c1ef8f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["NetInterfaces property Failover Cluster", "NetInterfaces property Failover Cluster , ClusNetwork object", "ClusNetwork object Failover Cluster , NetInterfaces property"]
topic_type:
- apiref
api_name:
- ClusNetwork.NetInterfaces
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNetwork.NetInterfaces property

\[The **NetInterfaces** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusNetworkNetInterfaces**](clusnetworknetinterfaces-collection.md) collection providing access to the [network interfaces](network-interfaces.md) in the [network](networks.md).

This property is read-only.

## Syntax


```VB
ClusNetwork.NetInterfaces
```



## Property value

A [**ClusNetworkNetInterfaces**](clusnetworknetinterfaces-collection.md) collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetwork is defined as F2E606F2-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusNetwork**](clusnetwork-object.md)
</dt> <dt>

[**ClusNetworkNetInterfaces**](clusnetworknetinterfaces-collection.md)
</dt> <dt>

[**Cluster Object**](cluster-object.md)
</dt> </dl>

 

 





