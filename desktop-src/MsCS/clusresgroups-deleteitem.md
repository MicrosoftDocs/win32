---
title: ClusResGroups.DeleteItem method
description: Deletes a group from the cluster as well as from the ClusResGroups collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '907364e7-cf9d-49f6-9c98-d16f6058ce5f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DeleteItem method Failover Cluster", "DeleteItem method Failover Cluster , ClusResGroups collection", "ClusResGroups collection Failover Cluster , DeleteItem method"]
topic_type:
- apiref
api_name:
- ClusResGroups.DeleteItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroups.DeleteItem method

\[The **DeleteItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a [group](groups.md) from the cluster as well as from the [**ClusResGroups**](clusresgroups-collection.md) collection.

## Syntax


```VB
ClusResGroups.DeleteItem( _
  ByVal index _
)
```



## Parameters

<dl> <dt>

*index* 
</dt> <dd>

[**ClusResGroups**](clusresgroups-collection.md) index value designating the [group](groups.md) object to delete.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroups is defined as F2E60708-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusResGroups**](clusresgroups-collection.md)
</dt> </dl>

 

 





