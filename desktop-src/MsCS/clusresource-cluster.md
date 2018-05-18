---
title: ClusResource.Cluster property
description: cluster associated with the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b8658f84-a025-4f04-bf91-e6ca264c10fe'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Cluster property Failover Cluster", "Cluster property Failover Cluster , ClusResource class", "ClusResource class Failover Cluster , Cluster property"]
topic_type:
- apiref
api_name:
- ClusResource.Cluster
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResource.Cluster property

\[The **Cluster** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [*cluster*](c-gly.md#-wolf-cluster-gly) associated with the [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.Cluster
```



## Property value

Object that receives the [**Cluster**](cluster-object.md) object.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





