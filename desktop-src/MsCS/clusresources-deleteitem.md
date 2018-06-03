---
title: ClusResources.DeleteItem method
description: Deletes a resource from the cluster and removes it from a ClusResources collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 200783e7-a2e6-489f-8271-36b8b6496b8e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DeleteItem method Failover Cluster
- DeleteItem method Failover Cluster , ClusResources collection
- ClusResources collection Failover Cluster , DeleteItem method
topic_type:
- apiref
api_name:
- ClusResources.DeleteItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResources.DeleteItem method

\[The **DeleteItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a [resource](resources.md) from the [*cluster*](https://www.bing.com/search?q=*cluster*) and removes it from a [**ClusResources**](clusresources-collection.md) collection.

## Syntax


```VB
ClusResources.DeleteItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

Integer that identifies an object in the collection by name or numeric index. Index numbers range from 1 to [**ClusResources.Count**](clusresources-count.md).

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResources is defined as F2E6070C-2631-11D1-89F1-00A0C90D061E<br/>    |



## See also

<dl> <dt>

[**ClusResources**](clusresources-collection.md)
</dt> <dt>

[**ClusResources.Count**](clusresources-count.md)
</dt> </dl>

 

 





