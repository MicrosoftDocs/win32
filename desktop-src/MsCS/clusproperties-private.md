---
title: ClusProperties.Private property
description: Indicates whether the properties in a ClusProperties collection are private properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '94ce9052-98af-4edd-b3da-6aeff40d8242'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Private property Failover Cluster", "Private property Failover Cluster , ClusProperties collection", "ClusProperties collection Failover Cluster , Private property"]
topic_type:
- apiref
api_name:
- ClusProperties.Private
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusProperties.Private property

\[The **Private** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates whether the properties in a [**ClusProperties**](clusproperties-collection.md) collection are [private properties](private-properties.md).

This property is read-only.

## Syntax


```VB
ClusProperties.Private
```



## Property value

A **Variant** set to **VARIANT\_TRUE** if the properties are private and **VARIANT\_FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusProperties is defined as F2E60700-2631-11D1-89F1-00A0C90D061E<br/>   |



## See also

<dl> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> </dl>

 

 





