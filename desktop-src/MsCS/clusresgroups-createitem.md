---
title: ClusResGroups.CreateItem method
description: Creates a group in the cluster and adds it to the ClusResGroups collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b43a7d4-db08-402d-9910-464ba3ea8d18
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CreateItem method Failover Cluster
- CreateItem method Failover Cluster , ClusResGroups collection
- ClusResGroups collection Failover Cluster , CreateItem method
topic_type:
- apiref
api_name:
- ClusResGroups.CreateItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroups.CreateItem method

\[The **CreateItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a [group](groups.md) in the [*cluster*](https://www.bing.com/search?q=*cluster*) and adds it to the [**ClusResGroups**](clusresgroups-collection.md) collection.

## Syntax


```VB
ClusResGroups.CreateItem( _
  ByVal GroupName _
)
```



## Parameters

<dl> <dt>

*GroupName* 
</dt> <dd>

**String** containing the name of the group to create.

</dd> </dl>

## Return value

A [**ClusResGroup**](clusresgroup-object.md) object that receives the new group.

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

[**ClusResGroup**](clusresgroup-object.md)
</dt> <dt>

[**ClusResGroups**](clusresgroups-collection.md)
</dt> </dl>

 

 





