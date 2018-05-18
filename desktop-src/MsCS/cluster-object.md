---
title: Cluster object
description: Enables operations on the cluster and provides access to all of the objects in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4a765dce-c823-4a79-8608-ff41feec8a39'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Cluster object Failover Cluster", "Cluster object Failover Cluster , described"]
topic_type:
- apiref
api_name:
- Cluster
- ISCluster
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster object

\[The **Cluster** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables operations on the [*cluster*](c-gly.md#-wolf-cluster-gly) and provides access to all of the objects in the cluster.

## Members

The **Cluster** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Cluster** object has these methods.



| Method                       | Description                                 |
|:-----------------------------|:--------------------------------------------|
| [**Open**](cluster-open.md) | Opens a connection to a cluster.<br/> |



 

### Properties

The **Cluster** object has these properties.



| Property                                                              | Description                                                                                                                                                                  |
|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommonProperties**](cluster-commonproperties.md)<br/>       | Returns the read/write [common properties](common-properties.md) of the cluster.<br/>                                                                                 |
| [**CommonROProperties**](cluster-commonroproperties.md)<br/>   | Returns the read-only common properties of the cluster.<br/>                                                                                                           |
| [**Name**](cluster-name.md)<br/>                               | Returns the current name of a cluster or allows a new name to be assigned.<br/>                                                                                        |
| [**NetInterfaces**](cluster-netinterfaces.md)<br/>             | Returns a [**ClusNetInterfaces**](clusnetinterfaces-collection.md) collection providing access to the [network interfaces](network-interfaces.md) in a cluster.<br/> |
| [**Networks**](cluster-networks.md)<br/>                       | Returns a [**ClusNetworks**](clusnetworks-collection.md) collection providing access to the [networks](networks.md) in a cluster.<br/>                               |
| [**Nodes**](cluster-nodes.md)<br/>                             | Returns a [**ClusNodes**](clusnodes-collection.md) collection providing access to the [nodes](nodes.md) in a cluster.<br/>                                           |
| [**PrivateProperties**](cluster-privateproperties.md)<br/>     | Returns the read-only private properties of the cluster.<br/>                                                                                                          |
| [**PrivateROProperties**](cluster-privateroproperties.md)<br/> | Returns the read/write [private properties](private-properties.md) of the cluster.<br/>                                                                               |
| [**QuorumLogSize**](cluster-quorumlogsize.md)<br/>             | Sets or returns the maximum size of the log file maintained by the quorum resource.<br/>                                                                               |
| [**QuorumPath**](cluster-quorumpath.md)<br/>                   | Sets or returns the path to the log file maintained by the [quorum resource](quorum-resource.md).<br/>                                                                |
| [**QuorumResource**](cluster-quorumresource.md)<br/>           | Specifies or returns a [**ClusResource**](clusresource-object.md) object representing the current quorum resource for a cluster.<br/>                                 |
| [**ResourceGroups**](cluster-resourcegroups.md)<br/>           | Returns a [**ClusResGroups**](clusresgroups-collection.md) collection providing access to the [groups](groups.md) in a cluster.<br/>                                 |
| [**Resources**](cluster-resources.md)<br/>                     | Returns a [**ClusResources**](clusresources-collection.md) collection providing access to the [resources](resources.md) in a cluster.<br/>                           |
| [**ResourceTypes**](cluster-resourcetypes.md)<br/>             | Returns a [**ClusResTypes**](clusrestypes-collection.md) collection providing access to the [resource types](resource-types.md) in a cluster.<br/>                   |
| [**Version**](cluster-version.md)<br/>                         | Returns a [**ClusVersion**](clusversion-object.md) object describing the [*cluster version*](c-gly.md#-wolf-cluster-version-gly).<br/>                               |



 

## Remarks

**Cluster** is a top-level object, allowing new object instances to be created. For example:


```VB
Dim objCluster as Cluster
Set objCluster = New Cluster
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[Cluster Management Objects](cluster-management-objects.md)
</dt> </dl>

 

 





