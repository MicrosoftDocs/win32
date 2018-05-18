---
title: ClusResTypes.DeleteItem method
description: Deletes a resource type from the cluster and removes it from the ClusResTypes collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0a528b4e-8d6d-434b-b005-ca732c72c7a3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DeleteItem method Failover Cluster", "DeleteItem method Failover Cluster , ClusResTypes collection", "ClusResTypes collection Failover Cluster , DeleteItem method"]
topic_type:
- apiref
api_name:
- ClusResTypes.DeleteItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResTypes.DeleteItem method

\[The **DeleteItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a [resource type](resource-types.md) from the [*cluster*](c-gly.md#-wolf-cluster-gly) and removes it from the [**ClusResTypes**](clusrestypes-collection.md) collection.

## Syntax


```VB
ClusResTypes.DeleteItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

Integer that identifies an object in the collection by name or numeric index.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If there are any resources of the specified type present in the cluster, the **DeleteItem** method fails for that resource type. In other words, you cannot delete a resource type if there are resources of that type present in the cluster.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResTypes is defined as F2E60712-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResTypes**](clusrestypes-collection.md)
</dt> </dl>

 

 





