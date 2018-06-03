---
title: ClusResGroup.Resources property
description: resources in a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 891a2126-774d-43c6-bd27-6a0e9d943383
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Resources property Failover Cluster
- Resources property Failover Cluster , ClusResGroup class
- ClusResGroup class Failover Cluster , Resources property
topic_type:
- apiref
api_name:
- ClusResGroup.Resources
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroup.Resources property

\[The **Resources** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [resources](resources.md) in a [group](groups.md).

This property is read-only.

## Syntax


```VB
ClusResGroup.Resources
```



## Property value

[**ClusResGroupResources**](clusresgroupresources-collection.md) collection that receives the resources in the group.

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

[**ClusResGroupResources**](clusresgroupresources-collection.md)
</dt> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> </dl>

 

 





