---
title: MicrosoftNLB\_Node class
description: The MicrosoftNLB\_Node \ 32;WMI class represents an instance of a node within a Network Load Balancing cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1a263761-b34c-43f8-89db-a289e882098a
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_Node class
- MicrosoftNLB_Node class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_Node
- MicrosoftNLB_Node.Caption
- MicrosoftNLB_Node.ComputerName
- MicrosoftNLB_Node.CreationClassName
- MicrosoftNLB_Node.DedicatedIPAddress
- MicrosoftNLB_Node.Description
- MicrosoftNLB_Node.HostPriority
- MicrosoftNLB_Node.InstallDate
- MicrosoftNLB_Node.LastLoadInfo
- MicrosoftNLB_Node.Name
- MicrosoftNLB_Node.NameFormat
- MicrosoftNLB_Node.PowerManagementCapabilities
- MicrosoftNLB_Node.PowerManagementSupported
- MicrosoftNLB_Node.PowerState
- MicrosoftNLB_Node.PrimaryOwnerContact
- MicrosoftNLB_Node.PrimaryOwnerName
- MicrosoftNLB_Node.ResetCapability
- MicrosoftNLB_Node.Roles
- MicrosoftNLB_Node.Status
- MicrosoftNLB_Node.StatusCode
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MicrosoftNLB\_Node class

The **MicrosoftNLB\_Node** [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) represents an instance of a [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) within a Network Load Balancing [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_Node : CIM_UnitaryComputerSystem
{
  string   Caption;
  string   ComputerName;
  string   CreationClassName;
  string   DedicatedIPAddress;
  string   Description;
  uint32   HostPriority;
  datetime InstallDate;
  string   LastLoadInfo;
  string   Name;
  string   NameFormat;
  uint16   PowerManagementCapabilities[];
  boolean  PowerManagementSupported;
  uint16   PowerState;
  string   PrimaryOwnerContact;
  string   PrimaryOwnerName;
  uint16   ResetCapability;
  string   Roles[];
  string   Status;
  uint32   StatusCode;
};
```

## Members

The **MicrosoftNLB\_Node** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftNLB\_Node** class has these methods.



| Method                                                   | Description                                                                                                            |
|:---------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**Disable**](microsoftnlb-node-disable.md)             | Disables a [*range of ports*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-6-gly) on the node.<br/>                    |
| [**DisableEx**](microsoftnlb-node-disableex.md)         | Disables ports specified by virtual [*IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) and range.<br/> |
| [**Drain**](microsoftnlb-node-drain.md)                 | [*Drains*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-11-gly) a range of ports on the node.<br/>                    |
| [**DrainEx**](microsoftnlb-node-drainex.md)             | Drains ports specified by virtual IP address and range.<br/>                                                     |
| [**DrainStop**](microsoftnlb-node-drainstop.md)         | Drains all ports, then stops cluster operations on the node.<br/>                                                |
| [**Enable**](microsoftnlb-node-enable.md)               | Enables ports that have been disabled on the node.<br/>                                                          |
| [**EnableEx**](microsoftnlb-node-enableex.md)           | Enables ports specified by virtual IP address and range.<br/>                                                    |
| [**Resume**](microsoftnlb-node-resume.md)               | Resumes all suspended ports on the node.<br/>                                                                    |
| [**SetPowerState**](microsoftnlb-node-setpowerstate.md) | Not used. Inherited from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).<br/>              |
| [**Start**](microsoftnlb-node-start.md)                 | Starts cluster operations on the node.<br/>                                                                      |
| [**Stop**](microsoftnlb-node-stop.md)                   | Stops cluster operations on the node.<br/>                                                                       |
| [**Suspend**](microsoftnlb-node-suspend.md)             | Suspends cluster operations on the node.<br/>                                                                    |



 

### Properties

The **MicrosoftNLB\_Node** class has these properties.

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

**ComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns the computer name in the form of a Fully Qualified Domain Name (FQDN), unless the FQDN exceeds 100 characters, in which case only the host name is returned. An empty string will be returned in the case of a failure.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The **CreationClassName** property indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**DedicatedIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies this node's unique IP address used for network traffic not associated with the cluster (for example, Telnet access to a specific node within the cluster).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**HostPriority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the [*host priority*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-3-gly) of the node. Each node within the cluster must specify a unique host priority, ranging from 1 (indicates the highest priority) to *n* (lowest priority), where *n* is the number of nodes in the cluster. The node with the highest priority receives all network traffic not handled by port rules.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The **InstallDate** property is a **datetime** value indicating when the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**LastLoadInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|HOST-RESOURCES-MIB.hrSystemInitialLoadDevice", "MIB.IETF\|HOST-RESOURCES-MIB.hrSystemInitialLoadParameters")
</dt> </dl>

The array entry of the **InitialLoadInfo** property, that holds the data corresponding to booting the currently loaded operating system.

This property is inherited from [**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name")
</dt> </dl>

Identifies the node by a combination of the [*cluster IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) and the node's host priority. The name is formatted as (cluster IP address)(colon)(host priority). For example: "172.150.35.12:1".

> [!Note]  
> When configuring new clusters, all of the cluster IP addresses may initially be set to zero (0.0.0.0). In this case the name format changes to "0.0.0.*x*:*id*" where *x* is a unique index and *id* is the host priority of the node.

 

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("NameFormat")
</dt> </dl>

Specifies the process by which the **Name** property is generated.

<dt>



 ("Other")


</dt> <dd></dd> <dt>



 ("IP")


</dt> <dd></dd> <dt>



 ("Dial")


</dt> <dd></dd> <dt>



 ("HID")


</dt> <dd></dd> <dt>



 ("NWA")


</dt> <dd></dd> <dt>



 ("HWA")


</dt> <dd></dd> <dt>



 ("X25")


</dt> <dd></dd> <dt>



 ("ISDN")


</dt> <dd></dd> <dt>



 ("IPX")


</dt> <dd></dd> <dt>



 ("DCC")


</dt> <dd></dd> <dt>



 ("ICD")


</dt> <dd></dd> <dt>



 ("E.164")


</dt> <dd></dd> <dt>



 ("SNA")


</dt> <dd></dd> <dt>



 ("OID/OSI")


</dt> <dd></dd> </dl>

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the specific power management capabilities of the node as an array of any of the following values that apply.

For more information, see [**SetPowerState**](microsoftnlb-node-setpowerstate.md).

This property inherits from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The power management capabilities of the node cannot be determined.

</dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>**Not Supported** (1)


</dt> <dd>

If the **PowerManagementSupported** property is **FALSE**, this should be the only value in the array.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (2)


</dt> <dd>

The power management capabilities of the node are turned off.

</dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (3)


</dt> <dd>

The power management features are currently enabled, but the exact feature set is unknown, or the information is unavailable.

</dd> <dt>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>**Power Saving Modes Entered Automatically** (4)


</dt> <dd>

The node can change its power state based on usage or other criteria.

</dd> <dt>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>**Power State Settable** (5)


</dt> <dd>

The [**SetPowerState**](microsoftnlb-node-setpowerstate.md) method is supported.

</dd> <dt>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>**Power Cycling Supported** (6)


</dt> <dd>

The [**SetPowerState**](microsoftnlb-node-setpowerstate.md) method can be invoked with the *PowerState* input variable set to 5 (Power Cycle).

</dd> <dt>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>**Timed Power On Supported** (7)


</dt> <dd>

As 6 (Power Cycling Supported), but also allows the *Time* parameter to specify a power-on time.

</dd> </dl>

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Boolean indicating that the computer system, with its running operating system, support power management. This boolean does not indicate that power management features are currently enabled, only that the system is capable of power management.

This property is inherited from [**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md).

</dd> <dt>

**PowerState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current power state of the node as one of the following values.

This property inherits from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The node's power state cannot be determined.

</dd> <dt>

<span id="Full_Power"></span><span id="full_power"></span><span id="FULL_POWER"></span>

<span id="Full_Power"></span><span id="full_power"></span><span id="FULL_POWER"></span>**Full Power** (1)


</dt> <dd>

The node is operating at full power.

</dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>**Power Save - Low Power Mode** (2)


</dt> <dd>

The node is in a power save state and is available, but its performance may be degraded.

</dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>**Power Save - Standby** (3)


</dt> <dd>

The node is in a power save state and is unavailable but can be powered up quickly.

</dd> <dt>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>**Power Save - Unknown** (4)


</dt> <dd>

The node is in an unrecognized power save state.

</dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>**Power Cycle** (5)


</dt> <dd>

The node is changing power states.

</dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>**Power Off** (6)


</dt> <dd>

The node is powered off and unavailable.

</dd> <dt>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>**Power Save - Warning** (7)


</dt> <dd>

The node is in a low power state and is generating a warning (for example, a low battery warning from a laptop).

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

A string that provides information on how the primary system owner can be reached (e.g. phone number, email address, ...).

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

The name of the primary system owner.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**ResetCapability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System Hardware Security\|001.4")
</dt> </dl>

Describes the ability of the node to be reset.

This property inherits from [**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

The node has some other reset capability.

</dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (2)


</dt> <dd>

Reset capacity is unknown.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)


</dt> <dd>

Hardware reset is not allowed.

</dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (4)


</dt> <dd>

The unitary computer system can be reset via hardware (e.g. the power and reset buttons).

</dd> <dt>

<span id="Not_Implemented"></span><span id="not_implemented"></span><span id="NOT_IMPLEMENTED"></span>

<span id="Not_Implemented"></span><span id="not_implemented"></span><span id="NOT_IMPLEMENTED"></span>**Not Implemented** (5)


</dt> <dd>

Reset capability has not been implemented.

</dd> </dl>

</dd> <dt>

**Roles**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A collection of strings that specify the roles this system plays in the IT-environment.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Indicates the current status of the node as one of the following values.

This property inherits from [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK**


</dt> <dd>

The node is operational.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error**


</dt> <dd>

No status information is available due to an unknown error.

</dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown**


</dt> <dd>

The node returned unrecognized state information.

</dd> </dl>

</dd> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current status of the node as one of the following values.

For an example that demonstrates the **StatusCode** property, see [Enumerating Remote Nodes](https://msdn.microsoft.com/library/bb736301).

<dt>

0
</dt> <dd>

Node is remote. The **StatusCode** value cannot be retrieved.

</dd> <dt>

<span id="WLBS_STOPPED"></span><span id="wlbs_stopped"></span>

<span id="WLBS_STOPPED"></span><span id="wlbs_stopped"></span>**WLBS\_STOPPED** (1005)


</dt> <dd>

Cluster operations have stopped on at least one node.

</dd> <dt>

<span id="WLBS_CONVERGING"></span><span id="wlbs_converging"></span>

<span id="WLBS_CONVERGING"></span><span id="wlbs_converging"></span>**WLBS\_CONVERGING** (1006)


</dt> <dd>

The [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) is [*converging*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly).

</dd> <dt>

<span id="WLBS_CONVERGED"></span><span id="wlbs_converged"></span>

<span id="WLBS_CONVERGED"></span><span id="wlbs_converged"></span>**WLBS\_CONVERGED** (1007)


</dt> <dd>

The [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) has [*converged*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly) successfully.

</dd> <dt>

<span id="WLBS_DEFAULT"></span><span id="wlbs_default"></span>

<span id="WLBS_DEFAULT"></span><span id="wlbs_default"></span>**WLBS\_DEFAULT** (1008)


</dt> <dd>

The specified node has converged as the [*default host*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-9-gly).

</dd> <dt>

<span id="WLBS_DRAINING"></span><span id="wlbs_draining"></span>

<span id="WLBS_DRAINING"></span><span id="wlbs_draining"></span>**WLBS\_DRAINING** (1009)


</dt> <dd>

One or more nodes are [*draining*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-11-gly).

</dd> <dt>

<span id="WLBS_SUSPENDED"></span><span id="wlbs_suspended"></span>

<span id="WLBS_SUSPENDED"></span><span id="wlbs_suspended"></span>**WLBS\_SUSPENDED** (1013)


</dt> <dd>

Cluster operations have been suspended on one or more nodes.

</dd> </dl>

</dd> </dl>

## Remarks

The **MicrosoftNLB\_Node** class is derived from the [**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626) class.

All methods except [**SetPowerState**](https://msdn.microsoft.com/library/aa371200) (which is not used) will fail if called on an instance of a **MicrosoftNLB\_Node** object that represents a remote node.

## Examples

For an example that demonstrates the **MicrosoftNLB\_Node** class, see [Enumerating Remote Nodes](https://msdn.microsoft.com/library/bb736301).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md)
</dt> <dt>

[Network Load Balancing WMI Classes](network-load-balancing-wmi-classes.md)
</dt> <dt>

[**CIM\_UnitaryComputerSystem**](https://msdn.microsoft.com/library/aa388626)
</dt> </dl>

 

 





