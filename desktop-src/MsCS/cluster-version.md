---
title: Cluster.Version property
description: Returns a ClusVersion object describing the operating system and Cluster service versions running on the local node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '77abfb85-48fe-4b18-b79e-5641711f33d7'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Version property Failover Cluster", "Version property Failover Cluster , Cluster object", "Cluster object Failover Cluster , Version property"]
topic_type:
- apiref
api_name:
- Cluster.Version
- ISCluster.get_Version
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.Version property

\[The **Version** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusVersion**](clusversion-object.md) object describing the operating system and [Cluster service](cluster-service.md) versions running on the local [node](nodes.md).

This property is read-only.

## Syntax


```VB
Cluster.Version
```



## Property value

A [**ClusVersion**](clusversion-object.md) object that receives the version information.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[**Cluster**](cluster-object.md)
</dt> <dt>

[**ClusVersion**](clusversion-object.md)
</dt> </dl>

 

 





