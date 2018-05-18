---
title: MSCluster\_Node class
description: A dynamic WMI class that represents a cluster node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bf531708-7a43-4567-bdeb-72b8908725f0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_Node class", "MSCluster_Node class, described"]
topic_type:
- apiref
api_name:
- MSCluster_Node
- MSCluster_Node.Caption
- MSCluster_Node.CreationClassName
- MSCluster_Node.InitialLoadInfo
- MSCluster_Node.InstallDate
- MSCluster_Node.LastLoadInfo
- MSCluster_Node.Name
- MSCluster_Node.NameFormat
- MSCluster_Node.OtherIdentifyingInfo
- MSCluster_Node.IdentifyingDescriptions
- MSCluster_Node.Dedicated
- MSCluster_Node.PowerManagementCapabilities
- MSCluster_Node.PowerManagementSupported
- MSCluster_Node.PowerState
- MSCluster_Node.PrimaryOwnerContact
- MSCluster_Node.PrimaryOwnerName
- MSCluster_Node.ResetCapability
- MSCluster_Node.Roles
- MSCluster_Node.Status
- MSCluster_Node.Description
- MSCluster_Node.NodeWeight
- MSCluster_Node.DynamicWeight
- MSCluster_Node.NodeHighestVersion
- MSCluster_Node.NodeLowestVersion
- MSCluster_Node.MajorVersion
- MSCluster_Node.MinorVersion
- MSCluster_Node.BuildNumber
- MSCluster_Node.CSDVersion
- MSCluster_Node.Id
- MSCluster_Node.NodeInstanceID
- MSCluster_Node.NodeDrainStatus
- MSCluster_Node.NodeDrainTarget
- MSCluster_Node.State
- MSCluster_Node.Flags
- MSCluster_Node.Characteristics
- MSCluster_Node.NeedsPreventQuorum
- MSCluster_Node.FaultDomainId
- MSCluster_Node.StatusInformation
- MSCluster_Node.FaultDomain
- MSCluster_Node.PrivateProperties
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_Node class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) [node](https://msdn.microsoft.com/library/aa371745).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{C306EBED-0654-4360-AA70-DE912C5FC364}"), AMENDMENT]
class MSCluster_Node : CIM_UnitaryComputerSystem
{
  string             Caption;
  string             CreationClassName;
  string             InitialLoadInfo[];
  datetime           InstallDate;
  string             LastLoadInfo;
  string             Name;
  string             NameFormat;
  string             OtherIdentifyingInfo[];
  string             IdentifyingDescriptions[];
  uint16             Dedicated[];
  uint16             PowerManagementCapabilities[];
  boolean            PowerManagementSupported;
  uint16             PowerState;
  string             PrimaryOwnerContact;
  string             PrimaryOwnerName;
  uint16             ResetCapability;
  string             Roles[];
  string             Status;
  string             Description;
  uint32             NodeWeight;
  uint32             DynamicWeight;
  uint32             NodeHighestVersion;
  uint32             NodeLowestVersion;
  uint32             MajorVersion;
  uint32             MinorVersion;
  uint32             BuildNumber;
  uint32             CSDVersion;
  string             Id;
  string             NodeInstanceID;
  uint32             NodeDrainStatus;
  string             NodeDrainTarget;
  uint32             State;
  uint32             Flags;
  uint32             Characteristics;
  uint32             NeedsPreventQuorum;
  string             FaultDomainId;
  uint32             StatusInformation;
  string             FaultDomain[];
  MSCluster_Property PrivateProperties;
};
```

## Members

The **MSCluster\_Node** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_Node** class has these methods.



| Method                                                                | Description                                                                                                                                                                                                                              |
|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ExecuteNodeControl**](mscluster-node-executenodecontrol.md)       | Executes a control code on the node.<br/>                                                                                                                                                                                          |
| [**Pause**](mscluster-node-pause.md)                                 | Pauses the cluster activity on a node.<br/>                                                                                                                                                                                        |
| [**Resume**](mscluster-node-resume.md)                               | Resumes the cluster activity on a node.<br/>                                                                                                                                                                                       |
| [**SetPowerState**](mscluster-node-setpowerstate.md)                 | Defines the desired power state for a logical device and when a device should be put into that state. Not implemented by WMI.<br/> Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).<br/> |
| [**WillEvictLoseQuorum**](mscluster-node-willevictlosequorum.md)     | Checks if evicting the node will cause the cluster to lose quorum.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/>                        |
| [**WillOfflineLoseQuorum**](mscluster-node-willofflinelosequorum.md) | Checks if the taking the node offline will cause the cluster to lose quorum.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/>              |



 

### Properties

The **MSCluster\_Node** class has these properties.

<dl> <dt>

**BuildNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the node's [**BuildNumber**](https://msdn.microsoft.com/library/aa371747) property.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Provides a short textual description (one-line string) of the node.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**Characteristics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the characteristics set for the node. For a list of possible characteristics, see [CLUSCTL\_NODE\_GET\_CHARACTERISTICS](https://msdn.microsoft.com/library/aa367416).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_KEY**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Indicates the name of the class or the subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**CSDVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the node's [**CSDVersion**](https://msdn.microsoft.com/library/aa371748) property, which specifies the most recent service pack installed on the node, if any.

</dd> <dt>

**Dedicated**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the node is a special-purpose node.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

<dt>

<span id="Not_Dedicated"></span><span id="not_dedicated"></span><span id="NOT_DEDICATED"></span>

<span id="Not_Dedicated"></span><span id="not_dedicated"></span><span id="NOT_DEDICATED"></span>**"Not Dedicated"** (0)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**"Unknown"** (1)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**"Other"** (2)


</dt> <dd></dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>**"Storage"** (3)


</dt> <dd></dd> <dt>

<span id="Router"></span><span id="router"></span><span id="ROUTER"></span>

<span id="Router"></span><span id="router"></span><span id="ROUTER"></span>**"Router"** (4)


</dt> <dd></dd> <dt>

<span id="Switch"></span><span id="switch"></span><span id="SWITCH"></span>

<span id="Switch"></span><span id="switch"></span><span id="SWITCH"></span>**"Switch"** (5)


</dt> <dd></dd> <dt>

<span id="Layer_3_Switch"></span><span id="layer_3_switch"></span><span id="LAYER_3_SWITCH"></span>

<span id="Layer_3_Switch"></span><span id="layer_3_switch"></span><span id="LAYER_3_SWITCH"></span>**"Layer 3 Switch"** (6)


</dt> <dd></dd> <dt>

<span id="Central_Office_Switch"></span><span id="central_office_switch"></span><span id="CENTRAL_OFFICE_SWITCH"></span>

<span id="Central_Office_Switch"></span><span id="central_office_switch"></span><span id="CENTRAL_OFFICE_SWITCH"></span>**"Central Office Switch"** (7)


</dt> <dd></dd> <dt>

<span id="Hub"></span><span id="hub"></span><span id="HUB"></span>

<span id="Hub"></span><span id="hub"></span><span id="HUB"></span>**"Hub"** (8)


</dt> <dd></dd> <dt>

<span id="Access_Server"></span><span id="access_server"></span><span id="ACCESS_SERVER"></span>

<span id="Access_Server"></span><span id="access_server"></span><span id="ACCESS_SERVER"></span>**"Access Server"** (9)


</dt> <dd></dd> <dt>

<span id="Firewall"></span><span id="firewall"></span><span id="FIREWALL"></span>

<span id="Firewall"></span><span id="firewall"></span><span id="FIREWALL"></span>**"Firewall"** (10)


</dt> <dd></dd> <dt>

<span id="Print"></span><span id="print"></span><span id="PRINT"></span>

<span id="Print"></span><span id="print"></span><span id="PRINT"></span>**"Print"** (11)


</dt> <dd></dd> <dt>

<span id="I_O"></span><span id="i_o"></span>

<span id="I_O"></span><span id="i_o"></span>**"I/O"** (12)


</dt> <dd></dd> <dt>

<span id="Web_Caching"></span><span id="web_caching"></span><span id="WEB_CACHING"></span>

<span id="Web_Caching"></span><span id="web_caching"></span><span id="WEB_CACHING"></span>**"Web Caching"** (13)


</dt> <dd></dd> <dt>


</dt> <dd>

Web Caching

</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the node's [**Description**](https://msdn.microsoft.com/library/aa371749) property, which has comments about the node.

</dd> <dt>

**DynamicWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The dynamic vote weight of the node adjusted by dynamic quorum feature.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**FaultDomain**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Fault domain hierarchy of this node.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**FaultDomainId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fault domain id of the node.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the flags set for the node. For a list of possible characteristics, see [CLUSCTL\_NODE\_GET\_FLAGS](https://msdn.microsoft.com/library/aa367420).

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Id of the node.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.OtherIdentifyingInfo")
</dt> </dl>

Provides explanations and details of the entries in the **OtherIdentifyingInfo** array. Each entry of this array is related to the entry in **OtherIdentifyingInfo** is located at the same index.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**InitialLoadInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains the data needed to find either the initial load device (its key) or the boot service to request the operating system to start up. In addition, the load parameters (a path and parameters) may also be specified.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

Indicates when the node was installed. The lack of a value does not indicate that the node is not installed.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**LastLoadInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|HOST-RESOURCES-MIB.hrSystemInitialLoadDevice", "MIB.IETF\|HOST-RESOURCES-MIB.hrSystemInitialLoadParameters")
</dt> </dl>

Contains the data identifying either the initial load device (its key) or the boot service that requested the last operating system load. In addition, the load parameters (a path and parameters) may also be specified.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**MajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the node's [**MajorVersion**](https://msdn.microsoft.com/library/aa371751) property, which specifies the major portion of the Windows version installed.

</dd> <dt>

**MinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the node's [**MinorVersion**](https://msdn.microsoft.com/library/aa371754) property, which specifies the minor portion of the Windows version installed.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name")
</dt> </dl>

Defines the label by which the node is known.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("NameFormat")
</dt> </dl>

Identifies how the node **Name** property is generated, using a heuristic. This property identifies how the system name was generated by using the subclass heuristic. The heuristic is outlined in the CIM V2 Common Model specification and assumes that the documented rules are traversed to determine and assign a name. The **NameFormat** values list defines the precedence order for assigning the system name with several rules mapping to the same value.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

Values include the following:

"IP"

"Dial"

"HID"

"NWA"

"HWA"

"X25"

"ISDN"

"IPX"

"DCC"

"ICD"

"E.164"

"SNA"

"OID/OSI"

"Other"

</dd> <dt>

**NeedsPreventQuorum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the cluster service on that node should be started with prevent quorum flag.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**NodeDrainStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current node drain status of a node.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

The possible values are.

<dt>

<span id="Not_Initiated"></span><span id="not_initiated"></span><span id="NOT_INITIATED"></span>

<span id="Not_Initiated"></span><span id="not_initiated"></span><span id="NOT_INITIATED"></span>**Not Initiated** (0)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **NotInitiated** before Windows Server 2012 R2 .

</dd> <dt>

<span id="In_Progress"></span><span id="in_progress"></span><span id="IN_PROGRESS"></span>

<span id="In_Progress"></span><span id="in_progress"></span><span id="IN_PROGRESS"></span>**In Progress** (1)


</dt> <dd>

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **InProgress** before Windows Server 2012 R2 .

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (2)


</dt> <dd></dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>**Failed** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**NodeDrainTarget**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The target specified for the node drain.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**NodeHighestVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the node's [**NodeHighestVersion**](https://msdn.microsoft.com/library/aa371755) property, which specifies the highest possible version of the cluster service with which the node can join or communicate.

</dd> <dt>

**NodeInstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the instance of the node.

</dd> <dt>

**NodeLowestVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the node's [**NodeLowestVersion**](https://msdn.microsoft.com/library/aa371756) property, which specifies the lowest possible version of the cluster service with which the node can join or communicate.

</dd> <dt>

**NodeWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The vote weight of the node.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.IdentifyingDescriptions")
</dt> </dl>

Contains additional data, beyond the **Name** property, that can be used to identify a node.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System Power Controls\|001.2")
</dt> </dl>

Indicates the specific power-related capabilities of a node and its associated running operating system.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The power management features are currently unknown.

</dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>**Not Supported** (1)


</dt> <dd>

The power management features are currently not supported.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (2)


</dt> <dd>

The power management features are currently disabled.

</dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (3)


</dt> <dd>

The power management features are currently enabled but the exact feature set is unknown or the information is unavailable.

</dd> <dt>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>**Power Saving Modes Entered Automatically** (4)


</dt> <dd>

The device can change its power state based on usage or other criteria.

</dd> <dt>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>**Power State Settable** (5)


</dt> <dd>

The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method is supported. This method is found on the parent [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class and can be implemented. For more information, see [Designing Managed Object Format (MOF) Classes](https://msdn.microsoft.com/library/aa390351).

</dd> <dt>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>**Power Cycling Supported** (6)


</dt> <dd>

The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle).

</dd> <dt>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>**Timed Power On Supported** (7)


</dt> <dd>

The [**SetPowerState**](https://msdn.microsoft.com/library/aa393485) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle) and *Time* set to a specific date and time, or interval, for power-on.

</dd> <dt>


</dt> <dd>

Timed Power On Supported

</dd> </dl>

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the node, with its running operating system, supports power management. If **FALSE**, the integer value 1 ("Not Supported") should be the only entry in the **PowerManagementCapabilities** array. This boolean does not indicate that power management features are currently enabled, or if enabled, what features are supported. For more information, see the **PowerManagementCapabilities** array.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**PowerState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current power state of the node and its associated operating system.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

System power state is unknown.

</dd> <dt>

<span id="Full_power"></span><span id="full_power"></span><span id="FULL_POWER"></span>

<span id="Full_power"></span><span id="full_power"></span><span id="FULL_POWER"></span>**Full power** (1)


</dt> <dd>

System is in a full power state.

</dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>**Power Save - Low Power Mode** (2)


</dt> <dd>

System is in a power-save state and still functioning but may exhibit degraded performance.

</dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>**Power Save - Standby** (3)


</dt> <dd>

System is not functioning but could be brought to full power quickly.

</dd> <dt>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>**Power Save - Unknown** (4)


</dt> <dd>

System is known to be in a power-save mode but its exact status is unknown.

</dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>**Power Cycle** (5)


</dt> <dd>

System power is being cycled.

</dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>**Power Off** (6)


</dt> <dd>

System power is off.

</dd> <dt>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>**Power Save - Warning** (7)


</dt> <dd>

System is in a warning state and also in a power-save mode.

</dd> <dt>

<span id="Power_Save_-_Hibernate"></span><span id="power_save_-_hibernate"></span><span id="POWER_SAVE_-_HIBERNATE"></span>

<span id="Power_Save_-_Hibernate"></span><span id="power_save_-_hibernate"></span><span id="POWER_SAVE_-_HIBERNATE"></span>**Power Save - Hibernate** (8)


</dt> <dd>

System is in a hibernate state and also in a power-save mode.

</dd> <dt>

<span id="Power_Save_-_Soft_Off"></span><span id="power_save_-_soft_off"></span><span id="POWER_SAVE_-_SOFT_OFF"></span>

<span id="Power_Save_-_Soft_Off"></span><span id="power_save_-_soft_off"></span><span id="POWER_SAVE_-_SOFT_OFF"></span>**Power Save - Soft Off** (9)


</dt> <dd>

System is in a soft off power state and also in a power-save mode.

</dd> <dt>


</dt> <dd>

Power Save - Warning

</dd> </dl>

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

Provides information on how the primary system owner can be reached.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

Contains the name of the primary node owner.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**PrivateProperties**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Property**](mscluster-property.md)**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An instance of the [**MSCluster\_Property**](mscluster-property.md) class representing the private properties of the node.

</dd> <dt>

**ResetCapability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System Hardware Security\|001.4")
</dt> </dl>

Determines whether the node can be reset with the power and reset buttons.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (4)


</dt> <dd></dd> <dt>

<span id="Not_Implemented"></span><span id="not_implemented"></span><span id="NOT_IMPLEMENTED"></span>

**Not Implemented** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Roles**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of strings that specify the roles this node plays in the IT-environment.

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns the current state of a node. For a list of possible state values, see [**GetClusterNodeState**](https://msdn.microsoft.com/library/aa369622) or the [**CLUSTER\_NODE\_STATE**](https://msdn.microsoft.com/library/bb309157) enumeration.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (-1)


</dt> <dd>

**Windows Server 2012 and Windows Server 2008 R2:** This value was **StateUnknown** before Windows Server 2012 R2.

</dd> <dt>

<span id="Up"></span><span id="up"></span><span id="UP"></span>

<span id="Up"></span><span id="up"></span><span id="UP"></span>**Up** (0)


</dt> <dd></dd> <dt>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>**Down** (1)


</dt> <dd></dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>**Paused** (2)


</dt> <dd></dd> <dt>

<span id="Joining"></span><span id="joining"></span><span id="JOINING"></span>

<span id="Joining"></span><span id="joining"></span><span id="JOINING"></span>**Joining** (3)


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

Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

Values include the following:

"OK"

"Error"

"Degraded"

"Unknown"

"Pred Fail"

"Starting"

"Stopping"

"Service"

"Stressed"

"NonRecover"

"No Contact"

"Lost Comm"

</dd> <dt>

**StatusInformation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The isolation or quarantine status of the node.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

This property can have the following values.

<dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** (0)


</dt> <dd></dd> <dt>

<span id="Isolated"></span><span id="isolated"></span><span id="ISOLATED"></span>

**Isolated** (1)


</dt> <dd></dd> <dt>

<span id="Quarantined"></span><span id="quarantined"></span><span id="QUARANTINED"></span>

**Quarantined** (2)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **MSCluster\_Node** class is derived from the [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





