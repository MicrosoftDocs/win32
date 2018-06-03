---
title: ClusRegistryKeys.Count property
description: Number of registry keys in the ClusRegistryKeys collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b28a0a0e-5b8c-4d81-b10d-ad203e280835
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Count property Failover Cluster
- Count property Failover Cluster , ClusRegistryKeys class
- ClusRegistryKeys class Failover Cluster , Count property
topic_type:
- apiref
api_name:
- ClusRegistryKeys.Count
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusRegistryKeys.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of registry keys in the [**ClusRegistryKeys**](clusregistrykeys-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusRegistryKeys.Count
```



## Property value

**Long** indicating the number of registry keys in the collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusRegistryKeys is defined as F2E6072A-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusRegistryKeys**](clusregistrykeys-collection.md)
</dt> </dl>

 

 





