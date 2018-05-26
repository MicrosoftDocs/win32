---
title: MSCluster\_ResourceGroup class
description: A dynamic WMI class that represents a cluster \ 32;group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b5cb8bee-24ce-4dbc-82c3-104a5f90a5ab
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, described
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup
- MSCluster_ResourceGroup.Caption
- MSCluster_ResourceGroup.InstallDate
- MSCluster_ResourceGroup.Status
- MSCluster_ResourceGroup.Flags
- MSCluster_ResourceGroup.Characteristics
- MSCluster_ResourceGroup.Name
- MSCluster_ResourceGroup.Description
- MSCluster_ResourceGroup.State
- MSCluster_ResourceGroup.AutoFailbackType
- MSCluster_ResourceGroup.FailbackWindowEnd
- MSCluster_ResourceGroup.FailbackWindowStart
- MSCluster_ResourceGroup.FailoverPeriod
- MSCluster_ResourceGroup.FailoverThreshold
- MSCluster_ResourceGroup.Id
- MSCluster_ResourceGroup.PersistentState
- MSCluster_ResourceGroup.AntiAffinityClassNames
- MSCluster_ResourceGroup.PrivateProperties
- MSCluster_ResourceGroup.InternalState
- MSCluster_ResourceGroup.Priority
- MSCluster_ResourceGroup.DefaultOwner
- MSCluster_ResourceGroup.CCFEpoch
- MSCluster_ResourceGroup.ResiliencyPeriod
- MSCluster_ResourceGroup.GroupType
- MSCluster_ResourceGroup.OwnerNode
- MSCluster_ResourceGroup.IsCore
- MSCluster_ResourceGroup.StatusInformation
- MSCluster_ResourceGroup.ColdStartSetting
- MSCluster_ResourceGroup.PreferredSite
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_ResourceGroup class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) [group](https://msdn.microsoft.com/library/aa369645).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{DDE3A30E-55F7-4c31-B6CF-E360D12C5253}"), AMENDMENT]
class MSCluster_ResourceGroup : MSCluster_LogicalElement
{
  string             Caption;
  datetime           InstallDate;
  string             Status;
  uint32             Flags;
  uint32             Characteristics;
  string             Name;
  string             Description;
  uint32             State;
  uint32             AutoFailbackType;
  sint32             FailbackWindowEnd;
  sint32             FailbackWindowStart;
  uint32             FailoverPeriod;
  uint32             FailoverThreshold;
  string             Id;
  boolean            PersistentState;
  string             AntiAffinityClassNames[];
  MSCluster_Property PrivateProperties;
  string             InternalState;
  uint32             Priority;
  uint32             DefaultOwner;
  uint64             CCFEpoch;
  uint32             ResiliencyPeriod;
  uint32             GroupType;
  string             OwnerNode;
  boolean            IsCore;
  uint64             StatusInformation;
  uint32             ColdStartSetting;
  string             PreferredSite[];
};
```

## Members

The **MSCluster\_ResourceGroup** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_ResourceGroup** class has these methods.



| Method                                                                     | Description                                                                                                                                                                                                                                                      |
|:---------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BringOnline**](mscluster-resourcegroup-bringonline.md)                 | Brings a group online.<br/>                                                                                                                                                                                                                                |
| [**CancelOperation**](mscluster-resourcegroup-canceloperation.md)         | Cancels any pending operations on the resource group.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/> <br/>                                                             |
| [**CreateGroup**](mscluster-resourcegroup-creategroup.md)                 | Creates a group.<br/>                                                                                                                                                                                                                                      |
| [**DeleteGroup**](mscluster-resourcegroup-deletegroup.md)                 | Deletes a group.<br/>                                                                                                                                                                                                                                      |
| [**DestroyGroup**](mscluster-resourcegroup-destroygroup.md)               | Destroys the cluster group and any resources in this group.<br/>                                                                                                                                                                                           |
| [**ExecuteGroupControl**](mscluster-resourcegroup-executegroupcontrol.md) | Executes a control code on the group.<br/>                                                                                                                                                                                                                 |
| [**GetGroupType**](mscluster-resourcegroup-getgrouptype.md)               | Gets the group type for this resource group.<br/>                                                                                                                                                                                                          |
| [**GetPreferredOwners**](mscluster-resourcegroup-getpreferredowners.md)   | Get the list of preferred owners for this resource group.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/> <br/>                                                         |
| [**MoveToNewNode**](mscluster-resourcegroup-movetonewnode.md)             | Moves the group to a different node.<br/>                                                                                                                                                                                                                  |
| [**MoveToNewNodeEx**](mscluster-resourcegroup-movetonewnodeex.md)         | Move the resource group to a different node.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/> <br/>                                                                      |
| [**MoveToNewNodeParams**](mscluster-resourcegroup-movetonewnodeparams.md) | Move the resource group to different node with the parameters specified as a raw buffer.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/> <br/>                          |
| [**Rename**](mscluster-resourcegroup-rename.md)                           | Renames a group.<br/>                                                                                                                                                                                                                                      |
| [**SetGroupType**](mscluster-resourcegroup-setgrouptype.md)               | Sets the group type for this resource group.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2008.<br/> This method is obsolete beginning in Windows Server 2012.<br/> <br/> |
| [**SetPreferredOwners**](mscluster-resourcegroup-setpreferredowners.md)   | Sets the preferred owner list for this resource group.<br/>                                                                                                                                                                                                |
| [**TakeOffline**](mscluster-resourcegroup-takeoffline.md)                 | Takes a group offline.<br/>                                                                                                                                                                                                                                |
| [**TakeOfflineParams**](mscluster-resourcegroup-takeofflineparams.md)     | Take the resource group offline with the parameters specified as a raw buffer.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not available before Windows Server 2012.<br/> <br/>                                    |



 

### Properties

The **MSCluster\_ResourceGroup** class has these properties.

<dl> <dt>

**AntiAffinityClassNames**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the group's [**AntiAffinityClassNames**](https://msdn.microsoft.com/library/aa369651) property.

The [**AntiAffinityClassNames**](https://msdn.microsoft.com/library/aa369651) property identifies groups that should not be hosted on the same cluster node.

</dd> <dt>

**AutoFailbackType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the group's [**AutoFailbackType**](https://msdn.microsoft.com/library/aa369653) property.

The [**AutoFailbackType**](https://msdn.microsoft.com/library/aa369653) property specifies whether the group should automatically be failed back to the node identified as its preferred owner when that node comes back online following a failover.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the group

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CCFEpoch**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The current CCF of the resource group.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides the characteristics of the group. The cluster defines characteristics only for [resources](https://msdn.microsoft.com/library/aa372152). For a description of these characteristics, see [CLUSCTL\_RESOURCE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367466).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**ColdStartSetting**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether a group can start after a cluster cold start.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not available before Windows Server 2016.

The following are the possible values.

<dt>

<span id="Always_Start"></span><span id="always_start"></span><span id="ALWAYS_START"></span>

**Always Start** (0)


</dt> <dd></dd> <dt>

<span id="Start_Disabled"></span><span id="start_disabled"></span><span id="START_DISABLED"></span>

**Start Disabled** (1)


</dt> <dd></dd> <dt>

<span id="Start_Allowed_Until_Next_Cold_Start"></span><span id="start_allowed_until_next_cold_start"></span><span id="START_ALLOWED_UNTIL_NEXT_COLD_START"></span>

**Start Allowed Until Next Cold Start** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**DefaultOwner**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (-1), [**Max**](https://msdn.microsoft.com/library/aa393650) (512)
</dt> </dl>

Number of the last node the resource group was activated on or explicitly moved to.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Description)
</dt> </dl>

The Description property provides comments about the group.

</dd> <dt>

**FailbackWindowEnd**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (-1), [**Max**](https://msdn.microsoft.com/library/aa393650) (23), [**Units**](https://msdn.microsoft.com/library/aa393650) ("hours")
</dt> </dl>

Provides access to the group's [**FailbackWindowEnd**](https://msdn.microsoft.com/library/aa369659) property.

The [**FailbackWindowEnd**](https://msdn.microsoft.com/library/aa369659) property provides the latest time that the group can be moved back to the node identified as its preferred node.

</dd> <dt>

**FailbackWindowStart**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (-1), [**Max**](https://msdn.microsoft.com/library/aa393650) (23), [**Units**](https://msdn.microsoft.com/library/aa393650) ("hours")
</dt> </dl>

Provides access to the group's [**FailbackWindowStart**](https://msdn.microsoft.com/library/aa369662) property.

The [**FailbackWindowStart**](https://msdn.microsoft.com/library/aa369662) property provides the earliest time (that is, local time as kept by the cluster) that the group can be moved back to the node identified as its preferred node.

</dd> <dt>

**FailoverPeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1193), [**Units**](https://msdn.microsoft.com/library/aa393650) ("hours")
</dt> </dl>

Provides access to the group's [**FailoverPeriod**](https://msdn.microsoft.com/library/aa369665) property.

The [**FailoverPeriod**](https://msdn.microsoft.com/library/aa369665) property specifies a number of hours during which a maximum number of failover attempts, specified by the **FailoverThreshold** property, can occur.

</dd> <dt>

**FailoverThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the group's [**FailoverThreshold**](https://msdn.microsoft.com/library/aa369668) property.

The [**FailoverThreshold**](https://msdn.microsoft.com/library/aa369668) property specifies the maximum number of failover attempts.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the flags set for the group. The cluster defines flags only for resources. For a description of these flags, see [CLUSCTL\_RESOURCE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367471).

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

This property is inherited from [**MSCluster\_LogicalElement**](mscluster-logicalelement.md).

</dd> <dt>

**GroupType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Type of the resource group.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read/write before Windows Server 2012.

The values **iSCSI Target Server**, **Scale-Out File Server**, and **Hyper-V Replica Broker** are not available before Windows Server 2012.

<dt>

<span id="File_Server"></span><span id="file_server"></span><span id="FILE_SERVER"></span>

<span id="File_Server"></span><span id="file_server"></span><span id="FILE_SERVER"></span>**File Server** (100)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **FileServer** before Windows Server 2012 R2.

</dd> <dt>

<span id="Print_Server"></span><span id="print_server"></span><span id="PRINT_SERVER"></span>

<span id="Print_Server"></span><span id="print_server"></span><span id="PRINT_SERVER"></span>**Print Server** (101)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **PrintServer** before Windows Server 2012 R2.

</dd> <dt>

<span id="DHCP_Server"></span><span id="dhcp_server"></span><span id="DHCP_SERVER"></span>

<span id="DHCP_Server"></span><span id="dhcp_server"></span><span id="DHCP_SERVER"></span>**DHCP Server** (102)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **DhcpServer** before Windows Server 2012 R2.

</dd> <dt>

<span id="DTC"></span><span id="dtc"></span>

<span id="DTC"></span><span id="dtc"></span>**DTC** (103)


</dt> <dd></dd> <dt>

<span id="Message_Queuing"></span><span id="message_queuing"></span><span id="MESSAGE_QUEUING"></span>

<span id="Message_Queuing"></span><span id="message_queuing"></span><span id="MESSAGE_QUEUING"></span>**Message Queuing** (104)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **Msmq** before Windows Server 2012 R2.

</dd> <dt>

<span id="WINS_Server"></span><span id="wins_server"></span><span id="WINS_SERVER"></span>

<span id="WINS_Server"></span><span id="wins_server"></span><span id="WINS_SERVER"></span>**WINS Server** (105)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **Wins** before Windows Server 2012 R2.

</dd> <dt>

<span id="DFS_Namespace_Server"></span><span id="dfs_namespace_server"></span><span id="DFS_NAMESPACE_SERVER"></span>

<span id="DFS_Namespace_Server"></span><span id="dfs_namespace_server"></span><span id="DFS_NAMESPACE_SERVER"></span>**DFS Namespace Server** (106)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **StandAloneDfs** before Windows Server 2012 R2.

</dd> <dt>

<span id="Generic_Application"></span><span id="generic_application"></span><span id="GENERIC_APPLICATION"></span>

<span id="Generic_Application"></span><span id="generic_application"></span><span id="GENERIC_APPLICATION"></span>**Generic Application** (107)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **GenericApplication** before Windows Server 2012 R2.

</dd> <dt>

<span id="Generic_Service"></span><span id="generic_service"></span><span id="GENERIC_SERVICE"></span>

<span id="Generic_Service"></span><span id="generic_service"></span><span id="GENERIC_SERVICE"></span>**Generic Service** (108)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **GenericService** before Windows Server 2012 R2.

</dd> <dt>

<span id="Generic_Script"></span><span id="generic_script"></span><span id="GENERIC_SCRIPT"></span>

<span id="Generic_Script"></span><span id="generic_script"></span><span id="GENERIC_SCRIPT"></span>**Generic Script** (109)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **GenericScript** before Windows Server 2012 R2.

</dd> <dt>

<span id="iSNS_Cluster_Resource"></span><span id="isns_cluster_resource"></span><span id="ISNS_CLUSTER_RESOURCE"></span>

<span id="iSNS_Cluster_Resource"></span><span id="isns_cluster_resource"></span><span id="ISNS_CLUSTER_RESOURCE"></span>**iSNS Cluster Resource** (110)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **IScsiNameService** before Windows Server 2012 R2.

</dd> <dt>

<span id="Virtual_Machine"></span><span id="virtual_machine"></span><span id="VIRTUAL_MACHINE"></span>

<span id="Virtual_Machine"></span><span id="virtual_machine"></span><span id="VIRTUAL_MACHINE"></span>**Virtual Machine** (111)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **Virtual Machine** before Windows Server 2012 R2.

</dd> <dt>

<span id="TS_Session_Broker"></span><span id="ts_session_broker"></span><span id="TS_SESSION_BROKER"></span>

<span id="TS_Session_Broker"></span><span id="ts_session_broker"></span><span id="TS_SESSION_BROKER"></span>**TS Session Broker** (112)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **TsSessionBroker** before Windows Server 2012 R2.

</dd> <dt>

<span id="iSCSI_Target_Server"></span><span id="iscsi_target_server"></span><span id="ISCSI_TARGET_SERVER"></span>

<span id="iSCSI_Target_Server"></span><span id="iscsi_target_server"></span><span id="ISCSI_TARGET_SERVER"></span>**iSCSI Target Server** (113)


</dt> <dd></dd> <dt>

<span id="Scale-Out_File_Server"></span><span id="scale-out_file_server"></span><span id="SCALE-OUT_FILE_SERVER"></span>

<span id="Scale-Out_File_Server"></span><span id="scale-out_file_server"></span><span id="SCALE-OUT_FILE_SERVER"></span>**Scale-Out File Server** (114)


</dt> <dd></dd> <dt>

<span id="Hyper-V_Replica_Broker"></span><span id="hyper-v_replica_broker"></span><span id="HYPER-V_REPLICA_BROKER"></span>

<span id="Hyper-V_Replica_Broker"></span><span id="hyper-v_replica_broker"></span><span id="HYPER-V_REPLICA_BROKER"></span>**Hyper-V Replica Broker** (115)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (9999)


</dt> <dd></dd> </dl>

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Id of the network.

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

Indicates when the group was installed. A lack of a value does not indicate that the group is not installed.

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

Provides the current internal state of the resource group.

</dd> <dt>

**IsCore**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the resource group is essential to the cluster and cannot be deleted.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not available before Windows Server 2012.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Name), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The Name property specifies the name of the group.

</dd> <dt>

**OwnerNode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The node hosting the resource group.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not available before Windows Server 2012.

</dd> <dt>

**PersistentState**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the group's [**PersistentState**](https://msdn.microsoft.com/library/aa369678) property.

The [**PersistentState**](https://msdn.microsoft.com/library/aa369678) property specifies whether a group should be left offline or brought online when the Cluster service starts.

</dd> <dt>

**PreferredSite**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The preferred site to host the group.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (0), [**Max**](https://msdn.microsoft.com/library/aa393650) (4999)
</dt> </dl>

Priority value of the resource group

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

**Windows Server 2008 R2:  **

This property has a maximum value of "512" before Windows Server 2012.

</dd> <dt>

**PrivateProperties**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Property**](mscluster-property.md)**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the group's [**MSCluster\_Property**](mscluster-property.md) class.

</dd> <dt>

**ResiliencyPeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The resiliency period for this group, in seconds.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of the resource group.

The following are the possible values.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (-1)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **StateUnknown** before Windows Server 2012 R2.

</dd> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>**Online** (0)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (1)


</dt> <dd></dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>**Failed** (2)


</dt> <dd></dd> <dt>

<span id="Partial_Online"></span><span id="partial_online"></span><span id="PARTIAL_ONLINE"></span>

<span id="Partial_Online"></span><span id="partial_online"></span><span id="PARTIAL_ONLINE"></span>**Partial Online** (3)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **PartialOnline** before Windows Server 2012 R2.

</dd> <dt>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>**Pending** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the group.

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

Status flags for the resource group that are set by the cluster service.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not available before Windows Server 2012.

</dd> </dl>

## Remarks

The **MSCluster\_ResourceGroup** class is derived from the [**MSCluster\_LogicalElement**](mscluster-logicalelement.md) class.

## Examples

The [Is this server part of a MS Cluster](https://Gallery.TechNet.Microsoft.Com/da51bcca-8407-45c3-896a-0df98014a4d5) PowerShell code sample on TechNet Gallery uses **MSCluster\_ResourceGroup** to determine if a remote server is part of a cluster.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_LogicalElement**](mscluster-logicalelement.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





