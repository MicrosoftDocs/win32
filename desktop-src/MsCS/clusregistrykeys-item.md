---
title: ClusRegistryKeys.Item property
description: Returns a single registry key from a ClusRegistryKeys collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e24239a4-feeb-468e-99b4-ca3093d8cfd0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusRegistryKeys class
- ClusRegistryKeys class Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusRegistryKeys.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusRegistryKeys.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a single registry key from a [**ClusRegistryKeys**](clusregistrykeys-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusRegistryKeys.Item( _
  ByVal varIndex _
)
```



## Property value

A string that receives the specified registry key.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusRegistryKeys is defined as F2E6072A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusRegistryKeys**](clusregistrykeys-collection.md)
</dt> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**ClusRegistryKeys.Count**](clusregistrykeys-count.md)
</dt> </dl>

 

 





