---
title: ClusResPossibleOwnerNodes.Modified property
description: Reports whether this instance of the collection has been modified since it was created.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5aceabdb-3c11-4e3b-8c8f-04d814ea014c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Modified property Failover Cluster
- Modified property Failover Cluster , ClusResPossibleOwnerNodes class
- ClusResPossibleOwnerNodes class Failover Cluster , Modified property
topic_type:
- apiref
api_name:
- ClusResPossibleOwnerNodes.Modified
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResPossibleOwnerNodes.Modified property

\[The **Modified** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Reports whether this instance of the collection has been modified since it was created.

This property is read-only.

## Syntax


```VB
ClusResPossibleOwnerNodes.Modified
```



## Property value

A **Variant** that receives flag indicating whether the collection has been modified. If *Flag* is set to **TRUE**, the collection has been modified. If *Flag* is set to **FALSE**, the collection has not been modified.

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                      |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>            |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>          |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>          |
| IID<br/>                      | IID\_ISClusResPossibleOwnerNodes is defined as F2E6070E-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md)
</dt> </dl>

 

 





