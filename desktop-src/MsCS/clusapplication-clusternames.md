---
title: ClusApplication.ClusterNames property
description: Names of all the clusters in a domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5c4d64e1-d8cb-4abb-b157-3ecdf02a6219'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusterNames property Failover Cluster", "ClusterNames property Failover Cluster , ClusApplication object", "ClusApplication object Failover Cluster , ClusterNames property"]
topic_type:
- apiref
api_name:
- ClusApplication.ClusterNames
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusApplication.ClusterNames property

\[The **ClusterNames** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the names of all the [*clusters*](c-gly.md#-wolf-cluster-gly) in a domain.

This property is read-only.

## Syntax


```VB
ClusApplication.ClusterNames( _
  ByVal strDomainName _
)
```



## Property value

A [**ClusterNames**](clusternames-collection.md) collection that receives the names of the clusters in the specified domain.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusApplication is defined as F2E606E6-2631-11D1-89F1-00A0C90D061E<br/>  |



## See also

<dl> <dt>

[**ClusApplication**](clusapplication-object.md)
</dt> <dt>

[**ClusterNames**](clusternames-collection.md)
</dt> </dl>

 

 





