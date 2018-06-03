---
title: ISCluster Networks property
description: Returns a ClusNetworks collection providing access to the networks in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 352f186d-bf42-480a-9554-c764345dafe6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Networks property Failover Cluster
- Networks property Failover Cluster , Cluster object
- Cluster object Failover Cluster , Networks property
- Networks property Failover Cluster , ISCluster interface
- ISCluster interface Failover Cluster , Networks property
topic_type:
- apiref
api_name:
- Cluster.Networks
- ISCluster.Networks
- ISCluster.get_Networks
- ISCluster.get_Networks
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISCluster::Networks property

\[The **Networks** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusNetworks**](clusnetworks-collection.md) collection providing access to the [networks](networks.md) in a [*cluster*](https://www.bing.com/search?q=*cluster*).

This property is read-only.

## Syntax


```VB
Cluster.Networks
```



## Property value

A [**ClusNetworks**](clusnetworks-collection.md) collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[**ClusNetworks**](clusnetworks-collection.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





