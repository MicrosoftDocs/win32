---
title: ClusResType.Cluster property
description: Returns the Cluster object associated with the resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc9808fb-e517-4d59-a506-07abb9cecd4e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Cluster property Failover Cluster
- Cluster property Failover Cluster , ClusResType object
- ClusResType object Failover Cluster , Cluster property
topic_type:
- apiref
api_name:
- ClusResType.Cluster
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResType.Cluster property

\[The **Cluster** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [**Cluster**](cluster-object.md) object associated with the [resource type](resource-types.md).

This property is read-only.

## Syntax


```VB
ClusResType.Cluster
```



## Property value

Object that receives a [**Cluster**](cluster-object.md) object.

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

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





