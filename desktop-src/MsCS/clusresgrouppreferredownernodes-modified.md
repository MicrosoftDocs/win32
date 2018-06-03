---
title: ClusResGroupPreferredOwnerNodes.Modified property
description: Reports whether an instance of the ClusResGroupPreferredOwnerNodes collection has been modified since it was created.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05a5f903-ea0d-4058-9806-3d9a9ef38e15
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Modified property Failover Cluster
- Modified property Failover Cluster , ClusResGroupPreferredOwnerNodes class
- ClusResGroupPreferredOwnerNodes class Failover Cluster , Modified property
topic_type:
- apiref
api_name:
- ClusResGroupPreferredOwnerNodes.Modified
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroupPreferredOwnerNodes.Modified property

\[The **Modified** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Reports whether an instance of the [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md) collection has been modified since it was created.

This property is read-only.

## Syntax


```VB
ClusResGroupPreferredOwnerNodes.Modified( _
  ByVal varFlag _
)
```



## Property value

A **Variant** that receives a flag that indicates whether the collection has been modified. If *Flag* is set to **TRUE**, the collection has been modified. If *Flag* is set to **FALSE**, the collection has not been modified.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                            |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                  |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>                |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>                |
| IID<br/>                      | IID\_ISClusResGroupPreferredOwnerNodes is defined as F2E606E8-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md)
</dt> </dl>

 

 





