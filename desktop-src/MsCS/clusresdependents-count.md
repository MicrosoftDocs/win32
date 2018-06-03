---
title: ClusResDependents.Count property
description: Number of resources in the ClusResDependents collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ab02c5ba-d63f-4eab-bad4-804760a8a40b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Count property Failover Cluster
- Count property Failover Cluster , ClusResDependents class
- ClusResDependents class Failover Cluster , Count property
topic_type:
- apiref
api_name:
- ClusResDependents.Count
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResDependents.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of [resources](resources.md) in the [**ClusResDependents**](clusresdependents-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusResDependents.Count
```



## Property value

**Long** indicating the number of resources in the collection.

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
</dt> </dl>

 

 





