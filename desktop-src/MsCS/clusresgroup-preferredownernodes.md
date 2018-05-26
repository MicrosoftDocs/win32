---
title: ClusResGroup.PreferredOwnerNodes property
description: Returns a ClusResGroupPreferredOwnerNodes collection providing access to all nodes on which a group prefers to run.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5e2872a4-72db-4cd8-9fce-34c1bd701706
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PreferredOwnerNodes property Failover Cluster
- PreferredOwnerNodes property Failover Cluster , ClusResGroup class
- ClusResGroup class Failover Cluster , PreferredOwnerNodes property
topic_type:
- apiref
api_name:
- ClusResGroup.PreferredOwnerNodes
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResGroup.PreferredOwnerNodes property

\[The **PreferredOwnerNodes** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection providing access to all [nodes](nodes.md) on which a [group](groups.md) prefers to run.

This property is read-only.

## Syntax


```VB
ClusResGroup.PreferredOwnerNodes
```



## Property value

A [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md)
</dt> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> </dl>

 

 





