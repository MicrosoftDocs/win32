---
title: ClusResDependencies.RemoveItem method
description: Removes a resource from the dependency collection but does not delete it from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '904556e2-7d0b-4c03-8cf5-795342263045'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["RemoveItem method Failover Cluster", "RemoveItem method Failover Cluster , ClusResDependencies class", "ClusResDependencies class Failover Cluster , RemoveItem method"]
topic_type:
- apiref
api_name:
- ClusResDependencies.RemoveItem
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResDependencies.RemoveItem method

\[The **RemoveItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a [resource](resources.md) from the [*dependency*](d-gly.md#-wolf-dependency-gly) collection but does not delete it from the [*cluster*](c-gly.md#-wolf-cluster-gly).

## Syntax


```VB
ClusResDependencies.RemoveItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** that identifies a resource in the collection by name or numeric index. Index numbers range from 1 to [**ClusResDependencies.Count**](clusresdependencies-count.md).

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>      |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>    |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>    |
| IID<br/>                      | IID\_ISClusResDependencies is defined as F2E60704-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResDependencies**](clusresdependencies-collection.md)
</dt> <dt>

[**ClusResDependencies.Count**](clusresdependencies-count.md)
</dt> </dl>

 

 





