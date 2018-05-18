---
title: ClusNetworkNetInterfaces collection
description: Provides access to the network interfaces available to a network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8b99f752-8aee-4c43-b49a-8ebaf20220f2'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusNetworkNetInterfaces collection Failover Cluster", "ClusNetworkNetInterfaces collection Failover Cluster , described"]
topic_type:
- apiref
api_name:
- ClusNetworkNetInterfaces
- ISClusNetworkNetInterfaces
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNetworkNetInterfaces collection

\[The **ClusNetworkNetInterfaces** collection is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides access to the [network interfaces](network-interfaces.md) available to a [network](networks.md).

## Members

The **ClusNetworkNetInterfaces** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusNetworkNetInterfaces** collection has these methods.



| Method                                              | Description                                      |
|:----------------------------------------------------|:-------------------------------------------------|
| [**Refresh**](clusnetworknetinterfaces-refresh.md) | Refreshes the data in the collection.<br/> |



 

### Properties

The **ClusNetworkNetInterfaces** collection has these properties.



| Property                                                   | Access type          | Description                                                        |
|:-----------------------------------------------------------|:---------------------|:-------------------------------------------------------------------|
| [**Count**](clusnetworknetinterfaces-count.md)<br/> | Read-only<br/> | Returns the number of objects in the collection.<br/>        |
| [**Item**](clusnetworknetinterfaces-item.md)<br/>   | Read-only<br/> | Returns a single network interface from the collection.<br/> |



 

## Remarks

A **ClusNetworkNetInterfaces** collection:

-   Contains [**ClusNetInterface**](clusnetinterface-object.md) objects.
-   Is obtained from [**ClusNetwork.NetInterfaces**](clusnetwork-netinterfaces.md).

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                     |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>           |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>         |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>         |
| IID<br/>                      | IID\_ISClusNetworkNetInterfaces is defined as F2E606F6-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[Network Management Objects](network-management-objects.md)
</dt> </dl>

 

 





