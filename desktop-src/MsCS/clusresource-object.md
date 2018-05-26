---
title: ClusResource object
description: Enables operations on a resource, its properties, and related objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c1b66495-c428-4ee4-94e2-263fd31f61ad
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusResource object Failover Cluster
- ClusResource object Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusResource
- ISClusResource
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusResource object

\[The **ClusResource** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Enables operations on a [resource](resources.md), its properties, and related objects.

## Members

The **ClusResource** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ClusResource** object has these methods.



| Method                                                                | Description                                                                                                    |
|:----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**AddResourceNode**](clusresource-addresourcenode.md)               | Adds a new [node](nodes.md) to the list of possible nodes that can host the resource.<br/>              |
| [**BecomeQuorumResource**](clusresource-becomequorumresource.md)     | Sets the [quorum resource](quorum-resource.md).<br/>                                                    |
| [**CanResourceBeDependent**](clusresource-canresourcebedependent.md) | Determines if the resource can be [*dependent*](d-gly.md#-wolf-dependent-gly) on another resource.<br/> |
| [**ChangeResourceGroup**](clusresource-changeresourcegroup.md)       | Moves the resource from its current [group](groups.md) to a different group.<br/>                       |
| [**Delete**](clusresource-delete.md)                                 | Deletes the resource from the cluster.<br/>                                                              |
| [**Fail**](clusresource-fail.md)                                     | Initiates [failure](resource-failure.md) of the resource.<br/>                                          |
| [**Offline**](clusresource-offline.md)                               | Takes the resource offline.<br/>                                                                         |
| [**Online**](clusresource-online.md)                                 | Brings the resource online.<br/>                                                                         |
| [**RemoveResourceNode**](clusresource-removeresourcenode.md)         | Removes a node from the list of possible nodes that can host the resource.<br/>                          |



 

### Properties

The **ClusResource** object has these properties.



| Property                                                                   | Access type           | Description                                                                                                                                                                    |
|:---------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClassInfo**](clusresource-classinfo.md)<br/>                     | Read-only<br/>  | Returns the resource class of a resource.<br/>                                                                                                                           |
| [**Cluster**](clusresource-cluster.md)<br/>                         | Read-only<br/>  | Returns the [*cluster*](c-gly.md#-wolf-cluster-gly) that includes the resource.<br/>                                                                                    |
| [**CommonProperties**](clusresource-commonproperties.md)<br/>       | Read-only<br/>  | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the resource's read/write [common properties](common-properties.md).<br/>           |
| [**CommonROProperties**](clusresource-commonroproperties.md)<br/>   | Read-only<br/>  | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the resource's read-only common properties.<br/>                                     |
| [**CoreFlag**](clusresource-coreflag.md)<br/>                       | Read-only<br/>  | Returns any flags that identify the resource as a [core resource](core-resources.md).<br/>                                                                              |
| [**CryptoKeys**](clusresource-cryptokeys.md)<br/>                   | Read-only<br/>  | Returns a [**ClusCryptoKeys**](cluscryptokeys-collection.md) collection containing the resource's [checkpointed](checkpointing.md) crypto keys.<br/>                   |
| [**Dependencies**](clusresource-dependencies.md)<br/>               | Read-only<br/>  | Returns a [**ClusResDependencies**](clusresdependencies-collection.md) collection providing access to the resource's [dependency](resource-dependencies.md) list.<br/> |
| [**Dependents**](clusresource-dependents.md)<br/>                   | Read-only<br/>  | Returns a [**ClusResDependents**](clusresdependents-collection.md) collection providing access to the list of the resource's dependent resources.<br/>                  |
| [**Disk**](clusresource-disk.md)<br/>                               | Read-only<br/>  | For [Physical Disk](physical-disk.md) resources, returns a [**ClusDisk**](clusdisk-object.md) object providing access to information about the disk.<br/>              |
| [**Group**](clusresource-group.md)<br/>                             | Read-only<br/>  | Returns the group to which the resource belongs.<br/>                                                                                                                    |
| [**MaintenanceMode**](clusresource-maintenancemode.md)<br/>         | Read/write<br/> | Returns or sets maintenance mode for a disk resource.<br/>                                                                                                               |
| [**Name**](clusresource-name.md)<br/>                               | Read/write<br/> | [Read/write property](read-write-properties.md) that either retrieves or modifies the name of the resource.<br/>                                                        |
| [**OwnerNode**](clusresource-ownernode.md)<br/>                     | Read-only<br/>  | Returns the node that is hosting the resource.<br/>                                                                                                                      |
| [**PossibleOwnerNodes**](clusresource-possibleownernodes.md)<br/>   | Read-only<br/>  | Returns the nodes that are members of the resource's [*possible owners*](p-gly.md#-wolf-possible-owner-gly) list.<br/>                                                  |
| [**PrivateProperties**](clusresource-privateproperties.md)<br/>     | Read-only<br/>  | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the resource's read/write [private properties](private-properties.md).<br/>         |
| [**PrivateROProperties**](clusresource-privateroproperties.md)<br/> | Read-only<br/>  | Returns a [**ClusProperties**](clusproperties-collection.md) collection containing the resource's read-only private properties.<br/>                                    |
| [**RegistryKeys**](clusresource-registrykeys.md)<br/>               | Read-only<br/>  | Returns a [**ClusRegistryKeys**](clusregistrykeys-collection.md) collection containing the resource's checkpointed registry keys.<br/>                                  |
| [**State**](clusresource-state.md)<br/>                             | Read-only<br/>  | Returns information about the current state of the resource.<br/>                                                                                                        |
| [**Type**](clusresource-type.md)<br/>                               | Read-only<br/>  | Returns the resource type of the resource as a [**ClusResType**](clusrestype-object.md) object.<br/>                                                                    |
| [**TypeName**](clusresource-typename.md)<br/>                       | Read-only<br/>  | Returns the resource type name of the resource.<br/>                                                                                                                     |



 

## Remarks

A **ClusResource** object is obtained from the following collections:

-   [**ClusResGroupResources**](clusresgroupresources-collection.md)
-   [**ClusResDependencies**](clusresdependencies-collection.md)
-   [**ClusResources**](clusresources-collection.md)
-   [**ClusResTypeResources**](clusrestyperesources-collection.md)

## Requirements



|                                     |                                                                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                                                                           |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>                                                                                 |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>                                                                               |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>                                                                               |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>                                                                               |
| IID<br/>                      | CLSID\_ClusResource is defined as f2e60709-2631-11d1-89f1-00a0c90d061e<br/> IID\_ISClusResource is defined as f2e6070a-2631-11d1-89f1-00a0c90d061e<br/> |



## See also

<dl> <dt>

[Resource Management Objects](resource-management-objects.md)
</dt> </dl>

 

 





