---
title: ClusApplication.OpenCluster method
description: Opens a connection to a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2501e921-5b0a-429f-aa7f-56191ab9795b'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["OpenCluster method Failover Cluster", "OpenCluster method Failover Cluster , ClusApplication object", "ClusApplication object Failover Cluster , OpenCluster method"]
topic_type:
- apiref
api_name:
- ClusApplication.OpenCluster
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusApplication.OpenCluster method

\[The **OpenCluster** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Opens a connection to a [*cluster*](c-gly.md#-wolf-cluster-gly).

## Syntax


```VB
ClusApplication.OpenCluster( _
  ByVal strClusterName _
)
```



## Parameters

<dl> <dt>

*strClusterName* 
</dt> <dd>

**String** containing the name of the cluster to open. If set to a zero-length string (""), the method will open a connection to the local [node's](nodes.md) cluster.

</dd> </dl>

## Return value

A [**Cluster**](cluster-object.md) object that receives the opened connection.

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

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





