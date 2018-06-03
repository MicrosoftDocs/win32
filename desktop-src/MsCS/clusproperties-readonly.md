---
title: ClusProperties.ReadOnly property
description: Indicates whether the properties in a ClusProperties collection are read-only properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 879bd8a6-3203-4ff0-8277-88c92ea8dbf3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ReadOnly property Failover Cluster
- ReadOnly property Failover Cluster , ClusProperties collection
- ClusProperties collection Failover Cluster , ReadOnly property
topic_type:
- apiref
api_name:
- ClusProperties.ReadOnly
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusProperties.ReadOnly property

\[The **ReadOnly** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates whether the properties in a [**ClusProperties**](clusproperties-collection.md) collection are [read-only properties](read-only-properties.md).

This property is read-only.

## Syntax


```VB
ClusProperties.ReadOnly
```



## Property value

A **Variant** set to either **VARIANT\_TRUE** if the properties are read-only and **VARIANT\_FALSE** otherwise.

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

 

 





