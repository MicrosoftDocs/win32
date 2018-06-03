---
title: ClusResGroup.CommonROProperties property
description: Read-only common properties of a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 90de1234-d55c-40c2-9616-cfb3f9230c41
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CommonROProperties property Failover Cluster
- CommonROProperties property Failover Cluster , ClusResGroup class
- ClusResGroup class Failover Cluster , CommonROProperties property
topic_type:
- apiref
api_name:
- ClusResGroup.CommonROProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroup.CommonROProperties property

\[The **CommonROProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read-only [common properties](common-properties.md) of a [group](groups.md).

This property is read-only.

## Syntax


```VB
ClusResGroup.CommonROProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the read-only common properties of the group.

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

[**ClusProperties**](clusproperties-collection.md)
</dt> <dt>

[**ClusResGroup**](clusresgroup-object.md)
</dt> </dl>

 

 





