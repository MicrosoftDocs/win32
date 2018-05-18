---
title: ClusNetInterface.PrivateROProperties property
description: Read-only private properties of a network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4a495832-d463-4390-b360-ce90fb5e6356'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["PrivateROProperties property Failover Cluster", "PrivateROProperties property Failover Cluster , ClusNetInterface object", "ClusNetInterface object Failover Cluster , PrivateROProperties property"]
topic_type:
- apiref
api_name:
- ClusNetInterface.PrivateROProperties
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNetInterface.PrivateROProperties property

\[The **PrivateROProperties** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the read-only [private properties](private-properties.md) of a [network interface](network-interfaces.md).

This property is read-only.

## Syntax


```VB
ClusNetInterface.PrivateROProperties
```



## Property value

A [**ClusProperties**](clusproperties-collection.md) collection to receive the read-only private properties of the network interface.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
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

 

 





