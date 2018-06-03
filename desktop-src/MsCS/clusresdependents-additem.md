---
title: ClusResDependents.AddItem method
description: Adds an existing cluster resource to the ClusResDependents collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f640b526-163d-4975-b135-6734569bf29a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AddItem method Failover Cluster
- AddItem method Failover Cluster , ClusResDependents class
- ClusResDependents class Failover Cluster , AddItem method
topic_type:
- apiref
api_name:
- ClusResDependents.AddItem
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResDependents.AddItem method

\[The **AddItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds an existing cluster [resource](resources.md) to the [**ClusResDependents**](clusresdependents-collection.md) collection.

## Syntax


```VB
ClusResDependents.AddItem( _
  ByVal objResource _
)
```



## Parameters

<dl> <dt>

*objResource* 
</dt> <dd>

The [**ClusResource**](clusresource-object.md) object to add to the collection.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Resources added to a [**ClusResDependents**](clusresdependents-collection.md) collection become [dependents](resource-dependencies.md) of the resource from which the collection was obtained.

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

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





