---
title: MSCluster\_ClusterSharedVolume class
description: A dynamic WMI class that represents a cluster shared volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bb2e5ece-e8c8-4da5-8ddf-0b52fdcad715'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ClusterSharedVolume class", "MSCluster_ClusterSharedVolume class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterSharedVolume
- MSCluster_ClusterSharedVolume.Caption
- MSCluster_ClusterSharedVolume.Description
- MSCluster_ClusterSharedVolume.InstallDate
- MSCluster_ClusterSharedVolume.Status
- MSCluster_ClusterSharedVolume.Name
- MSCluster_ClusterSharedVolume.Flags
- MSCluster_ClusterSharedVolume.Characteristics
- MSCluster_ClusterSharedVolume.VolumeName
- MSCluster_ClusterSharedVolume.FaultState
- MSCluster_ClusterSharedVolume.VolumeOffset
- MSCluster_ClusterSharedVolume.BackupState
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ClusterSharedVolume class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a cluster shared volume (CSV).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{15b2185f-3e18-4685-9136-5a3695ef62a6}"), AMENDMENT]
class MSCluster_ClusterSharedVolume : MSCluster_LogicalElement
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Status;
  string   Name;
  uint32   Flags;
  uint32   Characteristics;
  string   VolumeName;
  uint32   FaultState;
  uint64   VolumeOffset;
  uint32   BackupState;
};
```

## Members

The **MSCluster\_ClusterSharedVolume** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_ClusterSharedVolume** class has these methods.



| Method                                                                                   | Description                                                                                                    |
|:-----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**MoveToNewHost**](mscluster-clustersharedvolume-movetonewhost.md)                     | Moves the cluster shared volume to a another node. All volumes of this resource will also be moved.<br/> |
| [**TurnOffMaintenance**](mscluster-clustersharedvolume-turnoffmaintenance.md)           | Takes the cluster shared volume out of maintenance mode.<br/>                                            |
| [**TurnOffRedirectedAccess**](mscluster-clustersharedvolume-turnoffredirectedaccess.md) | Disables direct IO on the cluster shared volume.<br/>                                                    |
| [**TurnOnMaintenance**](mscluster-clustersharedvolume-turnonmaintenance.md)             | Places the cluster shared volume into maintenance mode.<br/>                                             |
| [**TurnOnRedirectedAccess**](mscluster-clustersharedvolume-turnonredirectedaccess.md)   | Enables direct IO on the cluster shared volume.<br/>                                                     |



 

### Properties

The **MSCluster\_ClusterSharedVolume** class has these properties.

<dl> <dt>

**BackupState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns the backup state of the cluster shared volume.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd></dd> <dt>

<span id="In_Progress"></span><span id="in_progress"></span><span id="IN_PROGRESS"></span>

<span id="In_Progress"></span><span id="in_progress"></span><span id="IN_PROGRESS"></span>**In Progress** (1)


</dt> <dd>

**Windows Server 2012 and Windows Server 2008 R2:** This value was **InProgress** before Windows Server 2012 R2.

</dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the characteristics of the object. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md)

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**FaultState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns the fault state of the cluster shared volume.

<dt>

<span id="No_Faults"></span><span id="no_faults"></span><span id="NO_FAULTS"></span>

<span id="No_Faults"></span><span id="no_faults"></span><span id="NO_FAULTS"></span>**No Faults** (0)


</dt> <dd>

**Windows Server 2012 and Windows Server 2008 R2:** This value was **NoFaults** before Windows Server 2012 R2.

</dd> <dt>

<span id="Redirected_Access"></span><span id="redirected_access"></span><span id="REDIRECTED_ACCESS"></span>

<span id="Redirected_Access"></span><span id="redirected_access"></span><span id="REDIRECTED_ACCESS"></span>**Redirected Access** (1)


</dt> <dd>

**Windows Server 2012 and Windows Server 2008 R2:** This value was **NoDirectIO** before Windows Server 2012 R2.

</dd> <dt>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>**No Access** (2)


</dt> <dd>

**Windows Server 2012 and Windows Server 2008 R2:** This value was **NoAccess** before Windows Server 2012 R2.

</dd> <dt>

<span id="In_Maintenance"></span><span id="in_maintenance"></span><span id="IN_MAINTENANCE"></span>

<span id="In_Maintenance"></span><span id="in_maintenance"></span><span id="IN_MAINTENANCE"></span>**In Maintenance** (4)


</dt> <dd>

**Windows Server 2012 and Windows Server 2008 R2:** This value was **Maintenence** before Windows Server 2012 R2.

</dd> </dl>

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the flags set for the object. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md)

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the element was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Name), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Returns the friendly name of the cluster shared volume.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the element.

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

**VolumeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns the device Id of the cluster shared volume.

</dd> <dt>

**VolumeOffset**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns the volume offset of the cluster shared volume.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_LogicalElement**](mscluster-logicalelement.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





