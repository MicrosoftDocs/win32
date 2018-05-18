---
title: ClusNetInterface object
description: Enables operations on a network interface, its properties, and related objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '21aaf37d-5b60-4005-9e7f-f0435de590b2'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusNetInterface object Failover Cluster", "ClusNetInterface object Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusNetInterface
- ISClusNetInterface
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNetInterface object

\[The **ClusNetInterface** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables operations on a [network interface](network-interfaces.md), its properties, and related objects.

## Members

The **ClusNetInterface** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusNetInterface** object has these properties.



| Property                                                                       | Access type          | Description                                                                                                                                                                     |
|:-------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cluster**](clusnetinterface-cluster.md)<br/>                         | Read-only<br/> | Returns a [**Cluster**](cluster-object.md) object providing access to the [*cluster*](c-gly.md#-wolf-cluster-gly) that owns the network interface.<br/>                 |
| [**CommonProperties**](clusnetinterface-commonproperties.md)<br/>       | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the network interface's read/write [common properties](common-properties.md).<br/>   |
| [**CommonROProperties**](clusnetinterface-commonroproperties.md)<br/>   | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the network interface's read-only common properties.<br/>                             |
| [**Name**](clusnetinterface-name.md)<br/>                               | Read-only<br/> | Returns the name of the network interface.<br/>                                                                                                                           |
| [**PrivateProperties**](clusnetinterface-privateproperties.md)<br/>     | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the network interface's read/write [private properties](private-properties.md).<br/> |
| [**PrivateROProperties**](clusnetinterface-privateroproperties.md)<br/> | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the network interface's read-only private properties.<br/>                            |
| [**State**](clusnetinterface-state.md)<br/>                             | Read-only<br/> | Returns the state of the network interface.<br/>                                                                                                                          |



 

## Remarks

A **ClusNetInterface** object is obtained from the following collections.

-   [**ClusNetInterfaces**](clusnetinterfaces-collection.md)
-   [**ClusNetworkNetInterfaces**](clusnetworknetinterfaces-collection.md)
-   [**ClusNodeNetInterfaces**](clusnodenetinterfaces-collection.md)

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

[Network Interface Management Objects](network-interface-management-objects.md)
</dt> </dl>

 

 





