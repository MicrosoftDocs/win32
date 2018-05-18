---
title: ClusResPossibleOwnerNodes.Count property
description: Returns the number of possible owner nodes listed for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '09c2aa3a-f431-48da-81ee-3ce347491b45'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Count property Failover Cluster", "Count property Failover Cluster , ClusResPossibleOwnerNodes class", "ClusResPossibleOwnerNodes class Failover Cluster , Count property"]
topic_type:
- apiref
api_name:
- ClusResPossibleOwnerNodes.Count
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResPossibleOwnerNodes.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of [*possible owner*](p-gly.md#-wolf-possible-owner-gly) [nodes](nodes.md) listed for a [resource](resources.md).

This property is read-only.

## Syntax


```VB
ClusResPossibleOwnerNodes.Count
```



## Property value

**Long** indicating the number of nodes in the collection.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                      |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>            |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>          |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>          |
| IID<br/>                      | IID\_ISClusResPossibleOwnerNodes is defined as F2E6070E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md)
</dt> </dl>

 

 





