---
title: ClusNetInterface.CommonROProperties property
description: Read-only common properties of a network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 14d76420-1ac6-4d58-82dd-343dc8ad8dfe
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CommonROProperties property Failover Cluster
- CommonROProperties property Failover Cluster , ClusNetInterface object
- ClusNetInterface object Failover Cluster , CommonROProperties property
topic_type:
- apiref
api_name:
- ClusNetInterface.CommonROProperties
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusNetInterface.CommonROProperties property

\[The **CommonROProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read-only [common properties](common-properties.md) of a [network interface](network-interfaces.md).

This property is read-only.

## Syntax


```VB
ClusNetInterface.CommonROProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection that receives the read-only common properties of the network interface.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetInterface is defined as F2E606EE-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusNetInterface**](clusnetinterface-object.md)
</dt> <dt>

[**ClusProperties**](clusproperties-collection.md)
</dt> </dl>

 

 





