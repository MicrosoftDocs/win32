---
title: ClusProperties.Modified property
description: Indicates whether any properties in the ClusProperties collection have been added or removed, or if any properties have been changed, since the last ClusProperties.Refresh or ClusProperties.SaveChanges operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5eaeffda-e2ce-420a-b3f5-da8dfbfdde24
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Modified property Failover Cluster
- Modified property Failover Cluster , ClusProperties collection
- ClusProperties collection Failover Cluster , Modified property
topic_type:
- apiref
api_name:
- ClusProperties.Modified
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusProperties.Modified property

\[The **Modified** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates whether any properties in the [**ClusProperties**](clusproperties-collection.md) collection have been added or removed, or if any properties have been changed, since the last [**ClusProperties.Refresh**](clusproperties-refresh.md) or [**ClusProperties.SaveChanges**](clusproperties-savechanges.md) operation.

This property is read-only.

## Syntax


```VB
ClusProperties.Modified
```



## Property value

A **Variant** set to **VARIANT\_TRUE** if any properties have been modified, added, or removed, and **VARIANT\_FALSE** otherwise.

## Remarks

To test whether a specific property has been modified, see [**ClusProperty.Modified**](clusproperty-modified.md).

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
</dt> <dt>

[**ClusProperties.Refresh**](clusproperties-refresh.md)
</dt> <dt>

[**ClusProperties.SaveChanges**](clusproperties-savechanges.md)
</dt> </dl>

 

 





