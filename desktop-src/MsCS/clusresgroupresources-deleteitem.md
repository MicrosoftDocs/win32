---
title: ClusResGroupResources.DeleteItem method
description: Removes a resource from a ClusResGroupResources collection and deletes it from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bfd908a3-b968-4729-8ca4-feb687108249'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DeleteItem method Failover Cluster", "DeleteItem method Failover Cluster , ClusResGroupResources class", "ClusResGroupResources class Failover Cluster , DeleteItem method"]
topic_type:
- apiref
api_name:
- ClusResGroupResources.DeleteItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroupResources.DeleteItem method

\[The **DeleteItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a [resource](resources.md) from a [**ClusResGroupResources**](clusresgroupresources-collection.md) collection and deletes it from the [*cluster*](c-gly.md#-wolf-cluster-gly).

## Syntax


```VB
ClusResGroupResources.DeleteItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** that identifies a resource in the collection by name or numeric index. Index numbers range from 1 to [**ClusResGroupResources.Count**](clusresgroupresources-count.md).

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                  |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>        |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>      |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>      |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>      |
| IID<br/>                      | IID\_ISClusResGroupResources is defined as F2E606EA-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResGroupResources**](clusresgroupresources-collection.md)
</dt> <dt>

[**ClusResGroupResources.Count**](clusresgroupresources-count.md)
</dt> </dl>

 

 





