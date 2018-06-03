---
title: ClusNetInterface.Name property
description: Name of a network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: efad2b26-6e36-44bd-b4c3-c63dbb54b256
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name property Failover Cluster
- Name property Failover Cluster , ClusNetInterface object
- ClusNetInterface object Failover Cluster , Name property
topic_type:
- apiref
api_name:
- ClusNetInterface.Name
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNetInterface.Name property

\[The **Name** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves or sets the name of a [network interface](network-interfaces.md).

This property is read-only.

## Syntax


```VB
ClusNetInterface.Name
```



## Property value

**String** that specifies the new network interface name.

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

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





