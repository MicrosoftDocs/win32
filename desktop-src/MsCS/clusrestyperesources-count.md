---
title: ClusResTypeResources.Count property
description: Returns the number of objects in the collection (the number of resources of a particular type in the cluster).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ccd8739e-9309-4630-92cd-5b2894eb416a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Count property Failover Cluster
- Count property Failover Cluster , ClusResTypeResources class
- ClusResTypeResources class Failover Cluster , Count property
topic_type:
- apiref
api_name:
- ClusResTypeResources.Count
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResTypeResources.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of objects in the collection (the number of [resources](resources.md) of a particular [type](resource-types.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly)).

This property is read-only.

## Syntax


```VB
ClusResTypeResources.Count
```



## Property value

**Long** indicating the number of objects in the collection.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                 |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>     |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>     |
| IID<br/>                      | IID\_ISClusResTypeResources is defined as F2E60714-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResTypeResources**](clusrestyperesources-collection.md)
</dt> </dl>

 

 





