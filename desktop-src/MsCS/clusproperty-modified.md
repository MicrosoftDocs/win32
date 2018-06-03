---
title: ClusProperty.Modified property
description: Indicates whether the value of the property has changed since the last ClusProperties.Refresh or ClusProperties.SaveChanges operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 231e9e80-aa4c-4a83-83f6-4276fac4211b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Modified property Failover Cluster
- Modified property Failover Cluster , ClusProperty object
- ClusProperty object Failover Cluster , Modified property
topic_type:
- apiref
api_name:
- ClusProperty.Modified
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusProperty.Modified property

\[The **Modified** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates whether the value of the property has changed since the last [**ClusProperties.Refresh**](clusproperties-refresh.md) or [**ClusProperties.SaveChanges**](clusproperties-savechanges.md) operation.

This property is read-only.

## Syntax


```VB
ClusProperty.Modified
```



## Property value

A **Variant** set to **VARIANT\_TRUE** if any properties have been modified, added, or removed, and **VARIANT\_FALSE** otherwise.

## Remarks

A [**ClusProperty**](clusproperty-object.md) object operates on a local copy of cluster property data. Changes made to the local copy of the data do not take effect in the [*cluster*](https://www.bing.com/search?q=*cluster*) until the parent [**ClusProperties**](clusproperties-collection.md) collection invokes the [**ClusProperties.SaveChanges**](clusproperties-savechanges.md) method. Any change to the local copy of the property value causes **Modified** to return **VARIANT\_TRUE**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperty is defined as F2E606FE-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusProperty**](clusproperty-object.md)
</dt> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> <dt>

**ClusProperties**
</dt> <dt>

[**ClusProperties.Refresh**](clusproperties-refresh.md)
</dt> <dt>

[**ClusProperties.SaveChanges**](clusproperties-savechanges.md)
</dt> </dl>

 

 





