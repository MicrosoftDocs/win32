---
title: MSCluster\_Resource class
description: A dynamic WMI class that represents a cluster resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d0d07dd9-e3ea-4306-8736-3a2b3dbfaf1d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_Resource class
- MSCluster_Resource class, described
topic_type:
- apiref
api_name:
- MSCluster_Resource
- MSCluster_Resource.Caption
- MSCluster_Resource.InstallDate
- MSCluster_Resource.Status
- MSCluster_Resource.Flags
- MSCluster_Resource.Characteristics
- MSCluster_Resource.Name
- MSCluster_Resource.Id
- MSCluster_Resource.Description
- MSCluster_Resource.IsAlivePollInterval
- MSCluster_Resource.LooksAlivePollInterval
- MSCluster_Resource.PendingTimeout
- MSCluster_Resource.MonitorProcessId
- MSCluster_Resource.PersistentState
- MSCluster_Resource.RestartAction
- MSCluster_Resource.RestartPeriod
- MSCluster_Resource.RestartThreshold
- MSCluster_Resource.EmbeddedFailureAction
- MSCluster_Resource.RetryPeriodOnFailure
- MSCluster_Resource.SeparateMonitor
- MSCluster_Resource.Type
- MSCluster_Resource.State
- MSCluster_Resource.InternalState
- MSCluster_Resource.ResourceClass
- MSCluster_Resource.Subclass
- MSCluster_Resource.PrivateProperties
- MSCluster_Resource.CryptoCheckpoints
- MSCluster_Resource.RegistryCheckpoints
- MSCluster_Resource.QuorumCapable
- MSCluster_Resource.LocalQuorumCapable
- MSCluster_Resource.DeleteRequiresAllNodes
- MSCluster_Resource.CoreResource
- MSCluster_Resource.DeadlockTimeout
- MSCluster_Resource.StatusInformation
- MSCluster_Resource.LastOperationStatusCode
- MSCluster_Resource.ResourceSpecificData1
- MSCluster_Resource.ResourceSpecificData2
- MSCluster_Resource.ResourceSpecificStatus
- MSCluster_Resource.RestartDelay
- MSCluster_Resource.IsClusterSharedVolume
- MSCluster_Resource.RequiredDependencyTypes
- MSCluster_Resource.RequiredDependencyClasses
- MSCluster_Resource.OwnerGroup
- MSCluster_Resource.OwnerNode
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_Resource class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) [resource](https://msdn.microsoft.com/library/aa372152).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{C2862F9C-34DE-4b16-9EE3-099D078E9F59}"), AMENDMENT]
class MSCluster_Resource : MSCluster_LogicalElement
{
  string             Caption;
  datetime           InstallDate;
  string             Status;
  uint32             Flags;
  uint32             Characteristics;
  string             Name;
  string             Id;
  string             Description;
  uint32             IsAlivePollInterval;
  uint32             LooksAlivePollInterval;
  uint32             PendingTimeout;
  uint32             MonitorProcessId;
  boolean            PersistentState;
  uint32             RestartAction;
  uint32             RestartPeriod;
  uint32             RestartThreshold;
  uint32             EmbeddedFailureAction;
  uint32             RetryPeriodOnFailure;
  boolean            SeparateMonitor;
  string             Type;
  uint32             State;
  string             InternalState;
  uint32             ResourceClass;
  uint32             Subclass;
  MSCluster_Property PrivateProperties;
  string             CryptoCheckpoints[];
  string             RegistryCheckpoints[];
  boolean            QuorumCapable;
  boolean            LocalQuorumCapable;
  boolean            DeleteRequiresAllNodes;
  boolean            CoreResource;
  uint32             DeadlockTimeout;
  uint64             StatusInformation;
  uint64             LastOperationStatusCode;
  uint64             ResourceSpecificData1;
  uint64             ResourceSpecificData2;
  string             ResourceSpecificStatus;
  uint32             RestartDelay;
  boolean            IsClusterSharedVolume;
  string             RequiredDependencyTypes[];
  uint32             RequiredDependencyClasses[];
  string             OwnerGroup;
  string             OwnerNode;
};
```

## Members

The **MSCluster\_Resource** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_Resource** class has these methods.



| Method                                                                          | Description                                                                                                                                                                                                             |
|:--------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddCryptoCheckpoint**](mscluster-resource-addcryptocheckpoint.md)           | Adds an encrypted crypto checkpoint to the [resource](https://msdn.microsoft.com/library/aa372152).<br/>                                                                                                                                       |
| [**AddDependency**](mscluster-resource-adddependency.md)                       | Creates a dependency relationship between two resources.<br/>                                                                                                                                                     |
| [**AddPossibleOwner**](mscluster-resource-addpossibleowner.md)                 | Adds a possible owner (host) node to the list of possible owners for this resource.<br/>                                                                                                                          |
| [**AddRegistryCheckpoint**](mscluster-resource-addregistrycheckpoint.md)       | Adds a registry checkpoint to the resource.<br/>                                                                                                                                                                  |
| [**AttachStorageDevice**](mscluster-resource-attachstoragedevice.md)           | Attaches the underlying storage of a resource to another device.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/>         |
| [**BringOnline**](mscluster-resource-bringonline.md)                           | Brings a resource online.<br/>                                                                                                                                                                                    |
| [**CreateResource**](mscluster-resource-createresource.md)                     | Creates a resource.<br/>                                                                                                                                                                                          |
| [**DeleteResource**](mscluster-resource-deleteresource.md)                     | Deletes a resource.<br/>                                                                                                                                                                                          |
| [**ExecuteResourceControl**](mscluster-resource-executeresourcecontrol.md)     | Executes a control code on the resource.<br/>                                                                                                                                                                     |
| [**FailResource**](mscluster-resource-failresource.md)                         | Forces this resource to become unavailable to simulate failure. This method is used by applications to test their failover configurations.<br/>                                                                   |
| [**GetDependencies**](mscluster-resource-getdependencies.md)                   | Gets the resource dependency expression.<br/>                                                                                                                                                                     |
| [**GetPossibleOwners**](mscluster-resource-getpossibleowners.md)               | Gets the list of nodes which can be an owner, host, of this resource.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/>    |
| [**MigrateVirtualMachine**](mscluster-resource-migratevirtualmachine.md)       | Migrates the virtual machine settings.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/>                                   |
| [**MoveToNewGroup**](mscluster-resource-movetonewgroup.md)                     | Moves the resource to a different group.<br/>                                                                                                                                                                     |
| [**ReleaseAddress**](mscluster-resource-releaseaddress.md)                     | Releases the IPv4 address DHCP lease. Valid only for IP address resources.<br/>                                                                                                                                   |
| [**RemoveCryptoCheckpoint**](mscluster-resource-removecryptocheckpoint.md)     | Removes a crypto key from the list of keys being checkpointed for the [resource](https://msdn.microsoft.com/library/aa372152).<br/>                                                                                                            |
| [**RemoveDependency**](mscluster-resource-removedependency.md)                 | Removes a dependency relationship between two resources.<br/>                                                                                                                                                     |
| [**RemovePossibleOwner**](mscluster-resource-removepossibleowner.md)           | Removes a possible owner node (host) from the list of possible owners for this resource.<br/>                                                                                                                     |
| [**RemoveRegistryCheckpoint**](mscluster-resource-removeregistrycheckpoint.md) | Removes a registry key from the list of keys being checkpointed for the [resource](https://msdn.microsoft.com/library/aa372152).<br/>                                                                                                          |
| [**Rename**](mscluster-resource-rename.md)                                     | Renames the resource.<br/>                                                                                                                                                                                        |
| [**RenewAddress**](mscluster-resource-renewaddress.md)                         | Renews the IPv4 address DHCP lease. Valid only for IP address resources.<br/>                                                                                                                                     |
| [**SetDependencies**](mscluster-resource-setdependencies.md)                   | Sets the resource dependency expression.<br/>                                                                                                                                                                     |
| [**TakeOffline**](mscluster-resource-takeoffline.md)                           | Takes the resource offline.<br/>                                                                                                                                                                                  |
| [**TakeOfflineParams**](mscluster-resource-takeofflineparams.md)               | Take the resource offline with the parameters specified as a raw buffer.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/> |
| [**UpdateVirtualMachine**](mscluster-resource-updatevirtualmachine.md)         | Updates the configuration of a clustered virtual machine.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/>                |



 

### Properties

The **MSCluster\_Resource** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the characteristics of the object. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**CoreResource**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, indicates that the resource is essential to the cluster and cannot be deleted.

</dd> <dt>

**CryptoCheckpoints**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a list of crypto checkpoints for the resource.

</dd> <dt>

**DeadlockTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the length of time to wait, in milliseconds, before declaring a deadlock in any call into a resource.

</dd> <dt>

**DeleteRequiresAllNodes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the resource cannot be deleted unless all nodes are active. Setting this property to **True** adds the **CLUS\_CHAR\_DELETE\_REQUIRES\_ALL\_NODES** characteristic to the resource.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Description)
</dt> </dl>

Provides access to the resource's [**Description**](https://msdn.microsoft.com/library/aa372161) property.

</dd> <dt>

**EmbeddedFailureAction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time, in milliseconds, that a resource should remain in a failed state before the Cluster service attempts to restart it.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the flags set for the object. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Id of the resource.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

A **datetime** value indicating when the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InternalState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2008:  **

The current internal state of the resource.

</dd> <dt>

**IsAlivePollInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Milliseconds")
</dt> </dl>

Provides access to the resource's [**IsAlivePollInterval**](https://msdn.microsoft.com/library/aa372166) property, which is the recommended interval in milliseconds at which the Cluster Service should poll the resource to determine whether it is operational. If the property is set to 0xFFFFFFFF, the Cluster Service uses the [**IsAlivePollInterval**](https://msdn.microsoft.com/library/aa372297) property for the resource type associated with the resource.

</dd> <dt>

**IsClusterSharedVolume**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies if the resource is a cluster shared volume resource.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**LastOperationStatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last application-specific error code returned by the Resource DLL during a cluster operation.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**LocalQuorumCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource can be selected as the quorum resource in clusters configured using the **-localquorum** switch.

</dd> <dt>

**LooksAlivePollInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Milliseconds")
</dt> </dl>

Provides access to the resource's [**LooksAlivePollInterval**](https://msdn.microsoft.com/library/aa372189) property, which is the recommended interval in milliseconds at which the Cluster Service should poll the resource to determine whether it appears operational. If the property is set to 0xFFFFFFFF, the Cluster Service uses the [**LooksAlivePollInterval**](https://msdn.microsoft.com/library/aa372301) property for the resource type associated with the resource.

</dd> <dt>

**MonitorProcessId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the process ID of the resource host service that is currently hosting the resource.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property was read-write prior to Windows Server 2016.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Name), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Provides the name of the resource.

</dd> <dt>

**OwnerGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource group which the resource belongs to.

**Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2012.

</dd> <dt>

**OwnerNode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The node hosting the resource.

**Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2012.

</dd> <dt>

**PendingTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource's [**PendingTimeout**](https://msdn.microsoft.com/library/aa372194) property. If a resource cannot be brought online or taken offline in the number of milliseconds specified by the **PendingTimeout** property, the resource is forcibly terminated.

</dd> <dt>

**PersistentState**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource's [**PersistentState**](https://msdn.microsoft.com/library/aa372197) property, which specifies whether the resource should be brought online or left offline when the Cluster Service is started.

</dd> <dt>

**PrivateProperties**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Property**](mscluster-property.md)**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the private properties of the resource.

</dd> <dt>

**QuorumCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource can be selected as the quorum resource for the cluster.

</dd> <dt>

**RegistryCheckpoints**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a list of registry checkpoints for the resource.

</dd> <dt>

**RequiredDependencyClasses**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource classes which the resource must depend on.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

**Storage** (1)


</dt> <dd></dd> <dt>

<span id="Network"></span><span id="network"></span><span id="NETWORK"></span>

**Network** (2)


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** (32768)


</dt> <dd></dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**RequiredDependencyTypes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The resource types which the resource must depend on.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**ResourceClass**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets or sets the resource class of a resource.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

**Storage** (1)


</dt> <dd></dd> <dt>

<span id="Network"></span><span id="network"></span><span id="NETWORK"></span>

**Network** (2)


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** (32768)


</dt> <dd></dd> </dl>

</dd> <dt>

**ResourceSpecificData1**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Resource-specific information.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**ResourceSpecificData2**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Resource-specific information.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**ResourceSpecificStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a resource-specific status message that complements the current resource state.

</dd> <dt>

**RestartAction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource's [**RestartAction**](https://msdn.microsoft.com/library/aa372202) property, which is the action to be taken by the Cluster Service if the resource fails. The following are the possible values.

<dt>

0
</dt> <dd>

Do not restart the resource after a failure.

</dd> <dt>

1
</dt> <dd>

Restart the resource after a failure. If the resource exceeds its restart threshold within its restart period, do not attempt to [failover](https://msdn.microsoft.com/library/aa369573) the [group](https://msdn.microsoft.com/library/aa369645) to another [node](https://msdn.microsoft.com/library/aa371745) in the [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

</dd> <dt>

2
</dt> <dd>

Restart the resource after a failure. If the resource exceeds its restart threshold within its restart period, attempt to fail over the group to another node in the cluster. This is the default setting.

</dd> </dl>

</dd> <dt>

**RestartDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the time delay before a failed resource is restarted.

</dd> <dt>

**RestartPeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource's [**RestartPeriod**](https://msdn.microsoft.com/library/aa372205) property, which is interval of time, in milliseconds, during which a specified number of restart attempts can be made on a nonresponsive resource.

</dd> <dt>

**RestartThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource's [**RestartThreshold**](https://msdn.microsoft.com/library/aa372207) property which is the maximum number of restart attempts that can be made on a resource within an interval defined by the [**RestartPeriod**](https://msdn.microsoft.com/library/aa372205) property before the Cluster Service initiates the action specified by the [**RestartAction**](https://msdn.microsoft.com/library/aa372202) property.

</dd> <dt>

**RetryPeriodOnFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource's [**RetryPeriodOnFailure**](https://msdn.microsoft.com/library/aa372208) property, which is the interval of time (in milliseconds) that a resource should remain in a failed state before the Cluster service attempts to restart it.

</dd> <dt>

**SeparateMonitor**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource's [**SeparateMonitor**](https://msdn.microsoft.com/library/aa372211) property, which indicates whether the resource requires its own Resource Monitor.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of the resource. The following are the possible values. For a list of possible state values, see [**GetClusterResourceState**](https://msdn.microsoft.com/library/aa369627).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (-1)


</dt> <dd>

The operation was not successful.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **StateUnknown** before Windows Server 2012 R2 .

</dd> <dt>

<span id="Inherited"></span><span id="inherited"></span><span id="INHERITED"></span>

<span id="Inherited"></span><span id="inherited"></span><span id="INHERITED"></span>**Inherited** (0)


</dt> <dd></dd> <dt>

<span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span>

<span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span>**Initializing** (1)


</dt> <dd>

The resource is performing initialization.

</dd> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>**Online** (2)


</dt> <dd>

The resource is operational and functioning normally.

</dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (3)


</dt> <dd>

The resource is not operational. This value will be returned if the resource reported a state of **ClusterResourceOffline** (3) or **ClusterResourceCannotComeOnlineOnThisNode** (127).

</dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>**Failed** (4)


</dt> <dd>

The resource has failed. This value will be returned if the resource reported a state of **ClusterResourceFailed** (4) or **ClusterResourceCannotComeOnlineOnAnyNode** (126).

</dd> <dt>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>**Pending** (128)


</dt> <dd>

The resource is coming online or going offline.

</dd> <dt>

<span id="Online_Pending"></span><span id="online_pending"></span><span id="ONLINE_PENDING"></span>

<span id="Online_Pending"></span><span id="online_pending"></span><span id="ONLINE_PENDING"></span>**Online Pending** (129)


</dt> <dd>

The resource is coming online.

</dd> <dt>

<span id="Offline_Pending"></span><span id="offline_pending"></span><span id="OFFLINE_PENDING"></span>

<span id="Offline_Pending"></span><span id="offline_pending"></span><span id="OFFLINE_PENDING"></span>**Offline Pending** (130)


</dt> <dd>

The resource is going offline.

</dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the object. Various operational and non-operational statuses are defined. Operational statuses are "OK", "Degraded", "Stressed" and "Pred Fail". "Stressed" indicates that the Element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, etc. The condition "Pred Fail" (failure predicted) indicates that an Element is functioning properly but predicting a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses can also be specified. These are "Error", "NonRecover", "Starting", "Stopping" and "Service". "NonRecover" indicates that a non-recoverable error has occurred. "Service" describes an Element being configured, maintained or cleaned, or otherwise administered. This status could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative task. Not all such work is on-line, yet the Element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> </dl>

</dd> <dt>

**StatusInformation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status flags for the resource that are set by cluster service.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**Subclass**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides the list of references to nodes that can be the owner of this resource.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the resource's [**Type**](https://msdn.microsoft.com/library/aa372213) property, which is the name for the resource's type.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





