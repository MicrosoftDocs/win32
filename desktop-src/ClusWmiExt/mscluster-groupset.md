---
title: MSCluster\_GroupSet class
description: Describes a set of groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 585cc1b8-07a1-47e5-bce4-d2e57e20fa18
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_GroupSet class
- MSCluster_GroupSet class, described
topic_type:
- apiref
api_name:
- MSCluster_GroupSet
- MSCluster_GroupSet.Name
- MSCluster_GroupSet.ClusterNodeObjectReturnedFrom
- MSCluster_GroupSet.GroupNames
- MSCluster_GroupSet.ProviderNames
- MSCluster_GroupSet.StartupCount
- MSCluster_GroupSet.StatusInformation
- MSCluster_GroupSet.IsGlobal
- MSCluster_GroupSet.StartupDelayTrigger
- MSCluster_GroupSet.StartupDelay
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_GroupSet class

Describes a set of groups.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("MSCLUSTEREXT"), AMENDMENT]
class MSCluster_GroupSet
{
  string  Name;
  string  ClusterNodeObjectReturnedFrom;
  string  GroupNames[];
  string  ProviderNames[];
  uint32  StartupCount;
  uint64  StatusInformation;
  boolean IsGlobal;
  uint32  StartupDelayTrigger;
  uint32  StartupDelay;
};
```

## Members

The **MSCluster\_GroupSet** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_GroupSet** class has these methods.



| Method                                                                      | Description                                                                       |
|:----------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**AddGroupToSet**](mscluster-groupset-addgrouptoset.md)                   | Adds a group to the set.<br/>                                               |
| [**AddProviderForGroup**](mscluster-groupset-addproviderforgroup.md)       | Adds a provider for the group.<br/>                                         |
| [**AddSetProvider**](mscluster-groupset-addsetprovider.md)                 | Adds a set as a provider.<br/>                                              |
| [**CreateSet**](mscluster-groupset-createset.md)                           | Creates a set.<br/>                                                         |
| [**GetGroups**](mscluster-groupset-getgroups.md)                           | Gets the groups that are providers for the group.<br/>                      |
| [**GetSetFrom**](mscluster-groupset-getsetfrom.md)                         | Gets the sets that contain the group.<br/>                                  |
| [**Remove**](mscluster-groupset-remove.md)                                 | Removes the set from the cluster.<br/>                                      |
| [**RemoveGroupFromSet**](mscluster-groupset-removegroupfromset.md)         | Removes a group from the set.<br/>                                          |
| [**RemoveProviderForGroup**](mscluster-groupset-removeproviderforgroup.md) | Removes a group provider for the group.<br/>                                |
| [**RemoveSetProvider**](mscluster-groupset-removesetprovider.md)           | Removes a set from being a provider.<br/>                                   |
| [**SetSet**](mscluster-groupset-setset.md)                                 | Changes settings on the set, pass in null to not change that variable.<br/> |



 

### Properties

The **MSCluster\_GroupSet** class has these properties.

<dl> <dt>

**ClusterNodeObjectReturnedFrom**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The adapter to help create cluster groups.

</dd> <dt>

**GroupNames**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the names of the groups contained in the collection.

</dd> <dt>

**IsGlobal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the property is global; otherwise, **false**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The friendly name of the set.

</dd> <dt>

**ProviderNames**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The names of the collections that are providers to this collection.

</dd> <dt>

**StartupCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ready count.

</dd> <dt>

**StartupDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The delay after reaching ready state.

</dd> <dt>

**StartupDelayTrigger**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ready setting.

</dd> <dt>

**StatusInformation**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status information.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



 

 





