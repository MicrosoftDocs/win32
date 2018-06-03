---
title: ClusResGroup.PrivateProperties property
description: Read/write private properties of a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 79988509-16fb-4d75-96fa-7659d1831c34
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PrivateProperties property Failover Cluster
- PrivateProperties property Failover Cluster , ClusResGroup class
- ClusResGroup class Failover Cluster , PrivateProperties property
topic_type:
- apiref
api_name:
- ClusResGroup.PrivateProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusResGroup.PrivateProperties property

\[The **PrivateProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read/write [private properties](private-properties.md) of a [group](groups.md).

This property is read-only.

## Syntax


```VB
ClusResGroup.PrivateProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the read/write private properties of the group.

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

 

 





