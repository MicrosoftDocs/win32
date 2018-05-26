---
title: ClusterNames.Item property
description: Returns a name of a cluster from the ClusterNames collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c54eceef-4814-4161-8ad6-9323fdb16503
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusterNames collection
- ClusterNames collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusterNames.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusterNames.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a name of a [*cluster*](c-gly.md#-wolf-cluster-gly) from the [**ClusterNames**](clusternames-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusterNames.Item( _
  ByVal varIndex _
)
```



## Property value

**String** that receives the name of a cluster in the collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusterNames is defined as F2E606EC-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusterNames**](clusternames-collection.md)
</dt> <dt>

[**ClusterNames.Count**](clusternames-count.md)
</dt> </dl>

 

 





