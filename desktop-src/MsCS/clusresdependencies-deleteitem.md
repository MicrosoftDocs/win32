---
title: ClusResDependencies.DeleteItem method
description: Removes a resource from the dependency collection and deletes the resource from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 01706fd2-48cc-4d98-a296-58caecc5857b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DeleteItem method Failover Cluster
- DeleteItem method Failover Cluster , ClusResDependencies class
- ClusResDependencies class Failover Cluster , DeleteItem method
topic_type:
- apiref
api_name:
- ClusResDependencies.DeleteItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResDependencies.DeleteItem method

\[The **DeleteItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a [resource](resources.md) from the [*dependency*](d-gly.md#-wolf-dependency-gly) collection and deletes the resource from the [*cluster*](c-gly.md#-wolf-cluster-gly).

## Syntax


```VB
ClusResDependencies.DeleteItem( _
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
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                |
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

 

 





