---
title: ClusResource.PossibleOwnerNodes property
description: The nodes specified as possible owners of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 591b0508-f963-4c62-afb8-1c9224299cc0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PossibleOwnerNodes property Failover Cluster
- PossibleOwnerNodes property Failover Cluster , ClusResource class
- ClusResource class Failover Cluster , PossibleOwnerNodes property
topic_type:
- apiref
api_name:
- ClusResource.PossibleOwnerNodes
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResource.PossibleOwnerNodes property

\[The **PossibleOwnerNodes** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the [nodes](nodes.md) specified as possible owners of a [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResource.PossibleOwnerNodes
```



## Property value

A [**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md) collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResource**](clusresource-object.md)
</dt> <dt>

[**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md)
</dt> </dl>

 

 





