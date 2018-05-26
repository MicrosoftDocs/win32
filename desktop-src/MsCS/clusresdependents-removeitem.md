---
title: ClusResDependents.RemoveItem method
description: Removes a resource from the ClusResDependents collection but does not delete it from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 70cee9b9-4d21-4237-8262-211e1b87923f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RemoveItem method Failover Cluster
- RemoveItem method Failover Cluster , ClusResDependents class
- ClusResDependents class Failover Cluster , RemoveItem method
topic_type:
- apiref
api_name:
- ClusResDependents.RemoveItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResDependents.RemoveItem method

\[The **RemoveItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a [resource](resources.md) from the [**ClusResDependents**](clusresdependents-collection.md) collection but does not delete it from the [*cluster*](c-gly.md#-wolf-cluster-gly).

## Syntax


```VB
ClusResDependents.RemoveItem( _
  ByVal varIndex _
)
```



## Parameters

<dl> <dt>

*varIndex* 
</dt> <dd>

A **Variant** that identifies a resource in the collection by name or numeric index. Index numbers range from 1 to [**ClusResDependents.Count**](clusresdependents-count.md).

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>              |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>  |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>  |
| IID<br/>                      | IID\_ISClusResDependents is defined as F2E6072E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResDependents**](clusresdependents-collection.md)
</dt> <dt>

[**ClusResDependents.Count**](clusresdependents-count.md)
</dt> </dl>

 

 





