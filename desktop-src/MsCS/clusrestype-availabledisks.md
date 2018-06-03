---
title: ClusResType.AvailableDisks property
description: Returns the collection representing the Physical Disks available to the resource type. A Physical Disk is available if it is cluster-capable and is currently not being used as a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fc700541-793b-423b-bea6-ad04deddb16a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AvailableDisks property Failover Cluster
- AvailableDisks property Failover Cluster , ClusResType object
- ClusResType object Failover Cluster , AvailableDisks property
topic_type:
- apiref
api_name:
- ClusResType.AvailableDisks
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResType.AvailableDisks property

\[The **AvailableDisks** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the collection representing the [Physical Disks](physical-disk.md) available to the resource type. A Physical Disk is available if it is [*cluster-capable*](https://www.bing.com/search?q=*cluster-capable*) and is currently not being used as a [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResType.AvailableDisks As ClusDisks
```



## Property value

## Access

Read-only

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResType is defined as F2E60710-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**ClusResType**](clusrestype-object.md)
</dt> <dt>

[**ClusDisks**](clusdisks-collection.md)
</dt> </dl>

 

 





