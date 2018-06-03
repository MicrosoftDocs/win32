---
title: Cluster.ResourceTypes property
description: Returns a ClusResTypes collection providing access to the resource types in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 73a9ca85-0da2-4978-965a-47bdee4ded6c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResourceTypes property Failover Cluster
- ResourceTypes property Failover Cluster , Cluster object
- Cluster object Failover Cluster , ResourceTypes property
topic_type:
- apiref
api_name:
- Cluster.ResourceTypes
- ISCluster.get_ResourceTypes
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster.ResourceTypes property

\[The **ResourceTypes** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusResTypes**](clusrestypes-collection.md) collection providing access to the [resource types](resource-types.md) in a [*cluster*](https://www.bing.com/search?q=*cluster*).

This property is read-only.

## Syntax


```VB
Cluster.ResourceTypes
```



## Property value

A [**ClusResTypes**](clusrestypes-collection.md) collection that receives the resource types.

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

[**Cluster**](cluster-object.md)
</dt> <dt>

[**ClusResTypes**](clusrestypes-collection.md)
</dt> </dl>

 

 





