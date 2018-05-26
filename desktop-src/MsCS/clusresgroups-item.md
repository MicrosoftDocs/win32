---
title: ClusResGroups.Item property
description: Retrieves a single group from a ClusResGroups collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e4391fe1-23d4-4f33-897a-6982422e9fb6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Item property Failover Cluster
- Item property Failover Cluster , ClusResGroups collection
- ClusResGroups collection Failover Cluster , Item property
topic_type:
- apiref
api_name:
- ClusResGroups.Item
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResGroups.Item property

\[The **Item** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves a single [group](groups.md) from a [**ClusResGroups**](clusresgroups-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResGroups.Item( _
  ByVal varIndex _
)
```



## Property value

A [**ClusResGroup**](clusresgroup-object.md) object that receives the specified group.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroups is defined as F2E60708-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusResGroups**](clusresgroups-collection.md)
</dt> <dt>

[**ClusResGroups.Count**](clusresgroups-count.md)
</dt> </dl>

 

 





