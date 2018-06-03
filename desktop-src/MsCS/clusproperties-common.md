---
title: ClusProperties.Common property
description: Indicates whether the properties in a ClusProperties collection are common properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7003b7e6-56f9-4499-9967-966ba23c40ed
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Common property Failover Cluster
- Common property Failover Cluster , ClusProperties collection
- ClusProperties collection Failover Cluster , Common property
topic_type:
- apiref
api_name:
- ClusProperties.Common
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusProperties.Common property

\[The **Common** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates whether the properties in a [**ClusProperties**](clusproperties-collection.md) collection are [common properties](common-properties.md).

This property is read-only.

## Syntax


```VB
ClusProperties.Common
```



## Property value

A **Variant** set to **VARIANT\_TRUE** if the properties are common properties, and **VARIANT\_FALSE** otherwise.

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

[**ClusProperties.Private**](clusproperties-private.md)
</dt> <dt>

[**ClusProperties.ReadOnly**](clusproperties-readonly.md)
</dt> </dl>

 

 





