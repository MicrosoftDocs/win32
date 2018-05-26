---
title: ClusResTypePossibleOwnerNodes.Count property
description: Returns the number of objects in the collection (the number of possible owner nodes listed for a resource type).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3dd07ddc-e07d-483a-b26b-754cea1bd2f2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Count property Failover Cluster
- Count property Failover Cluster , ClusResTypePossibleOwnerNodes class
- ClusResTypePossibleOwnerNodes class Failover Cluster , Count property
topic_type:
- apiref
api_name:
- ClusResTypePossibleOwnerNodes.Count
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResTypePossibleOwnerNodes.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of objects in the collection (the number of [*possible owner*](p-gly.md#-wolf-possible-owner-gly) [nodes](nodes.md) listed for a [resource type](resource-types.md)).

This property is read-only.

## Syntax


```VB
ClusResTypePossibleOwnerNodes.Count
```



## Property value

**Long** indicating the number of objects in the collection.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                          |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>              |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>              |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>              |
| IID<br/>                      | IID\_ISClusResTypePossibleOwnerNodes is defined as F2E60718-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResTypePossibleOwnerNodes**](clusrestypepossibleownernodes-collection.md)
</dt> </dl>

 

 





