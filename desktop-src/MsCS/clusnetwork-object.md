---
title: ClusNetwork object
description: Enables operations on a network, its properties, and related objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d51e9872-eb86-4b0e-b417-1a2e5ac6ee9c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusNetwork object Failover Cluster
- ClusNetwork object Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusNetwork
- ISClusNetwork
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusNetwork object

\[The **ClusNetwork** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables operations on a [network](networks.md), its properties, and related objects.

## Members

The **ClusNetwork** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusNetwork** object has these properties.



| Property                                                                  | Access type          | Description                                                                                                                                                                                  |
|:--------------------------------------------------------------------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cluster**](clusnetwork-cluster.md)<br/>                         | Read-only<br/> | Returns a [**Cluster**](cluster-object.md) object providing access to the [*cluster*](https://www.bing.com/search?q=*cluster*) operating over the network.<br/>                                   |
| [**CommonProperties**](clusnetwork-commonproperties.md)<br/>       | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the network's read/write [common properties](common-properties.md).<br/>                          |
| [**CommonROProperties**](clusnetwork-commonroproperties.md)<br/>   | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the network's read-only common properties.<br/>                                                    |
| [**Name**](clusnetwork-name.md)<br/>                               | Read-only<br/> | Returns the name of the network.<br/>                                                                                                                                                  |
| [**NetInterfaces**](clusnetwork-netinterfaces.md)<br/>             | Read-only<br/> | Returns a [**ClusNetworkNetInterfaces**](clusnetworknetinterfaces-collection.md) collection providing access to the [network interfaces](network-interfaces.md) in the network.<br/> |
| [**NetworkID**](clusnetwork-networkid.md)<br/>                     | Read-only<br/> | Returns the network identifier for the network.<br/>                                                                                                                                   |
| [**PrivateProperties**](clusnetwork-privateproperties.md)<br/>     | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the network's read/write [private properties](private-properties.md).<br/>                        |
| [**PrivateROProperties**](clusnetwork-privateroproperties.md)<br/> | Read-only<br/> | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the network's read-only private properties.<br/>                                                   |
| [**State**](clusnetwork-state.md)<br/>                             | Read-only<br/> | Returns the state of the network.<br/>                                                                                                                                                 |



 

## Remarks

A **ClusNetwork** object:

-   Is obtained from [**ClusNetworks**](clusnetworks-collection.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetwork is defined as F2E606F2-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[Network Management Objects](network-management-objects.md)
</dt> </dl>

 

 





