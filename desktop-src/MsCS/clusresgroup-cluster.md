---
title: ClusResGroup.Cluster property
description: cluster associated with the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fb5f1ebd-8d30-4625-9cc1-ce7713e91da6'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Cluster property Failover Cluster", "Cluster property Failover Cluster , ClusResGroup class", "ClusResGroup class Failover Cluster , Cluster property"]
topic_type:
- apiref
api_name:
- ClusResGroup.Cluster
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroup.Cluster property

\[The **Cluster** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [*cluster*](c-gly.md#-wolf-cluster-gly) associated with the [group](groups.md).

This property is read-only.

## Syntax


```VB
ClusResGroup.Cluster
```



## Property value

A [**Cluster**](cluster-object.md) object that receives the group's [*cluster*](c-gly.md#-wolf-cluster-gly).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





