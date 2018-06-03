---
title: ClusResGroup.Delete method
description: Deletes a group from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b1831340-67b9-458c-8669-c8e5e4973c28
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Delete method Failover Cluster
- Delete method Failover Cluster , ClusResGroup class
- ClusResGroup class Failover Cluster , Delete method
topic_type:
- apiref
api_name:
- ClusResGroup.Delete
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroup.Delete method

\[The **Delete** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes a [group](groups.md) from the [*cluster*](https://www.bing.com/search?q=*cluster*).

## Syntax


```VB
ClusResGroup.Delete()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

A group cannot be deleted while it contains resources.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> </dl>

 

 





