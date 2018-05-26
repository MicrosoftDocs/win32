---
title: ClusNode object
description: Enables operations on a node, its properties, and related objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b164f5a6-13f1-4eff-a2f9-805b60138dd1
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusNode object Failover Cluster
- ClusNode object Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusNode
- ISClusNode
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusNode object

\[The **ClusNode** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables operations on a [node](nodes.md), its properties, and related objects.



| Method or property                                                   | Description                                                                                                                                                                        |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cluster**](clusnode-cluster.md) Property                         | Returns a [**Cluster**](cluster-object.md) object providing access to the [*cluster*](c-gly.md#-wolf-cluster-gly) associated with the node.                                      |
| [**CommonProperties**](clusnode-commonproperties.md) Property       | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the node's read/write [common properties](common-properties.md).                              |
| [**CommonROProperties**](clusnode-commonroproperties.md) Property   | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the node's read-only [common properties](common-properties.md).                               |
| [**Evict**](clusnode-evict.md) Method                               | Removes a node from the cluster.                                                                                                                                                   |
| [**NetInterfaces**](clusnode-netinterfaces.md) Property             | Returns a [**ClusNodeNetInterfaces**](clusnodenetinterfaces-collection.md) collection providing access to the [network interfaces](network-interfaces.md) available to the node. |
| [**NodeID**](clusnode-nodeid.md) Property                           | Returns the identifier of the node.                                                                                                                                                |
| [**Pause**](clusnode-pause.md) Method                               | Temporarily suspends the cluster activity of the node.                                                                                                                             |
| [**PrivateProperties**](clusnode-privateproperties.md) Property     | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the node's read/write [private properties](private-properties.md).                            |
| [**PrivateROProperties**](clusnode-privateroproperties.md) Property | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the node's read-only private properties.                                                       |
| [**ResourceGroups**](clusnode-resourcegroups.md) Property           | Returns a [**ClusResGroups**](clusresgroups-collection.md) collection providing access to the [groups](groups.md) that are currently being hosted by the node.                   |
| [**Resume**](clusnode-resume.md) Method                             | Resumes the cluster activity of the node.                                                                                                                                          |
| [**State**](clusnode-state.md) Property                             | Returns the state of the node.                                                                                                                                                     |



 

## Members

The **ClusNode** object has these types of members:

-   [Methods](#methods)

### Methods

The **ClusNode** object has these methods.



| Method                            | Description                                          |
|:----------------------------------|:-----------------------------------------------------|
| [**Resume**](clusnode-resume.md) | Resumes the cluster activity of the node.<br/> |



 

## Remarks

A **ClusNode** object is obtained from the following collections.

-   [**ClusNodes**](clusnodes-collection.md)
-   [**ClusResGroupPreferredOwnerNodes**](clusresgrouppreferredownernodes-collection.md)
-   [**ClusResPossibleOwnerNodes**](clusrespossibleownernodes-collection.md)

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNode is defined as F2E606F8-2631-11D1-89F1-00A0C90D061E<br/>         |



## See also

<dl> <dt>

[Node Management Objects](node-management-objects.md)
</dt> </dl>

 

 





