---
title: ClusProperties.Count property
description: Number of properties in the ClusProperties collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6988a8c6-b1ef-4dba-b95c-eab52f140fb3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Count property Failover Cluster
- Count property Failover Cluster , ClusProperties collection
- ClusProperties collection Failover Cluster , Count property
topic_type:
- apiref
api_name:
- ClusProperties.Count
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusProperties.Count property

\[The **Count** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the number of properties in the [**ClusProperties**](clusproperties-collection.md) collection.

This property is read-only.

## Syntax


```VB
ClusProperties.Count
```



## Property value

**Long** indicating the number of objects in the collection.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperties is defined as F2E60700-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> </dl>

 

 





