---
title: ClusResGroup.PrivateROProperties property
description: Read-only private properties of a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '61a518b2-7792-4336-98ce-63de7ffe0e32'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["PrivateROProperties property Failover Cluster", "PrivateROProperties property Failover Cluster , ClusResGroup class", "ClusResGroup class Failover Cluster , PrivateROProperties property"]
topic_type:
- apiref
api_name:
- ClusResGroup.PrivateROProperties
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResGroup.PrivateROProperties property

\[The **PrivateROProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read-only [private properties](private-properties.md) of a [group](groups.md).

This property is read-only.

## Syntax


```VB
ClusResGroup.PrivateROProperties
```



## Property value

[**ClusProperties**](clusproperties-collection.md) collection to receive the read-only private properties of the group.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> </dl>

 

 





