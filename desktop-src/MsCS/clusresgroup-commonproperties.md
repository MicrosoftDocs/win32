---
title: ClusResGroup.CommonProperties property
description: Read/write common properties of a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 08c280a6-96c5-4e40-be42-4c798684482f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CommonProperties property Failover Cluster
- CommonProperties property Failover Cluster , ClusResGroup class
- ClusResGroup class Failover Cluster , CommonProperties property
topic_type:
- apiref
api_name:
- ClusResGroup.CommonProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResGroup.CommonProperties property

\[The **CommonProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read/write [common properties](common-properties.md) of a [group](groups.md).

This property is read-only.

## Syntax


```VB
ClusResGroup.CommonProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the read/write common properties of the group.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusResGroup is defined as F2E60706-2631-11D1-89F1-00A0C90D061E<br/>     |



## See also

<dl> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> </dl>

 

 





