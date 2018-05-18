---
title: CIM\_UnitaryComputerSystem class
description: A class derived from ComputerSystem that represents a Desktop, Mobile, NetPC, Server or other type of a single node Computer System.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd0fae5ba-4bf5-4ed6-9199-dbc9002bb386'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_UnitaryComputerSystem class", "CIM_UnitaryComputerSystem class, described"]
topic_type:
- apiref
api_name:
- CIM_UnitaryComputerSystem
- CIM_UnitaryComputerSystem.Caption
- CIM_UnitaryComputerSystem.Description
- CIM_UnitaryComputerSystem.InstallDate
- CIM_UnitaryComputerSystem.Status
- CIM_UnitaryComputerSystem.CreationClassName
- CIM_UnitaryComputerSystem.Name
- CIM_UnitaryComputerSystem.PrimaryOwnerContact
- CIM_UnitaryComputerSystem.PrimaryOwnerName
- CIM_UnitaryComputerSystem.Roles
- CIM_UnitaryComputerSystem.NameFormat
- CIM_UnitaryComputerSystem.OtherIdentifyingInfo
- CIM_UnitaryComputerSystem.IdentifyingDescriptions
- CIM_UnitaryComputerSystem.Dedicated
- CIM_UnitaryComputerSystem.InitialLoadInfo
- CIM_UnitaryComputerSystem.LastLoadInfo
- CIM_UnitaryComputerSystem.ResetCapability
- CIM_UnitaryComputerSystem.PowerManagementSupported
- CIM_UnitaryComputerSystem.PowerManagementCapabilities
- CIM_UnitaryComputerSystem.PowerState
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# CIM\_UnitaryComputerSystem class

A class derived from ComputerSystem that represents a Desktop, Mobile, NetPC, Server or other type of a single node Computer System.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, UUID("{903487A9-1E55-4489-9389-4CEE0AE6B236}"), AMENDMENT]
class CIM_UnitaryComputerSystem : CIM_ComputerSystem
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Status;
  string   CreationClassName;
  string   Name;
  string   PrimaryOwnerContact;
  string   PrimaryOwnerName;
  string   Roles[];
  string   NameFormat;
  string   OtherIdentifyingInfo[];
  string   IdentifyingDescriptions[];
  uint16   Dedicated[];
  string   InitialLoadInfo[];
  string   LastLoadInfo;
  uint16   ResetCapability;
  boolean  PowerManagementSupported;
  uint16   PowerManagementCapabilities[];
  uint16   PowerState;
};
```

## Members

The **CIM\_UnitaryComputerSystem** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_UnitaryComputerSystem** class has these methods.



| Method                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:-----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetPowerState**](cim-unitarycomputersystem-setpowerstate.md) | SetPowerState defines the desired power state of a ComputerSystem and its running OperatingSystem, and when the system should be put into that state. The PowerState parameter is specified as one of the valid integer values defined for the property, PowerState. The Time parameter (for all state changes but 5, "Power Cycle") indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). When the PowerState parameter is equal to 5, "Power Cycle", the Time parameter indicates when the system should power on again. Power off is immediate. SetPowerState should return 0 if successful, 1 if the specified State and Time request is not supported, and some other value if any other error occurred.<br/> |



 

### Properties

The **CIM\_UnitaryComputerSystem** class has these properties.

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

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_KEY**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**Dedicated**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Enumeration indicating whether the ComputerSystem is a special-purpose System (ie, dedicated to a particular use), versus being 'general purpose'. For example, one could specify that the System is dedicated to "Print" (value=11) or acts as a "Hub" (value=8).

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

<dt>

<span id="Not_Dedicated"></span><span id="not_dedicated"></span><span id="NOT_DEDICATED"></span>

**Not Dedicated** (0)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (1)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (2)


</dt> <dd></dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

**Storage** (3)


</dt> <dd></dd> <dt>

<span id="Router"></span><span id="router"></span><span id="ROUTER"></span>

**Router** (4)


</dt> <dd></dd> <dt>

<span id="Switch"></span><span id="switch"></span><span id="SWITCH"></span>

**Switch** (5)


</dt> <dd></dd> <dt>

<span id="Layer_3_Switch"></span><span id="layer_3_switch"></span><span id="LAYER_3_SWITCH"></span>

**Layer 3 Switch** (6)


</dt> <dd></dd> <dt>

<span id="Central_Office_Switch"></span><span id="central_office_switch"></span><span id="CENTRAL_OFFICE_SWITCH"></span>

**Central Office Switch** (7)


</dt> <dd></dd> <dt>

<span id="Hub"></span><span id="hub"></span><span id="HUB"></span>

**Hub** (8)


</dt> <dd></dd> <dt>

<span id="Access_Server"></span><span id="access_server"></span><span id="ACCESS_SERVER"></span>

**Access Server** (9)


</dt> <dd></dd> <dt>

<span id="Firewall"></span><span id="firewall"></span><span id="FIREWALL"></span>

**Firewall** (10)


</dt> <dd></dd> <dt>

<span id="Print"></span><span id="print"></span><span id="PRINT"></span>

**Print** (11)


</dt> <dd></dd> <dt>

<span id="I_O"></span><span id="i_o"></span>

**I/O** (12)


</dt> <dd></dd> <dt>

<span id="Web_Caching"></span><span id="web_caching"></span><span id="WEB_CACHING"></span>

**Web Caching** (13)


</dt> <dd></dd> </dl>

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

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).OtherIdentifyingInfo")
</dt> </dl>

An array of free-form strings providing explanations and details behind the entries in the OtherIdentifyingInfo array. Note, each entry of this array is related to the entry in OtherIdentifyingInfo that is located at the same index.

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

</dd> <dt>

**InitialLoadInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This object contains the data needed to find either the initial load device (its key) or the boot service to request the operating system to start up. In addition, the load parameters (ie, a pathname and parameters) may also be specified.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

A datetime value indicating when the object was installed. A lack of a value does not indicate that the object is not installed.

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

This object contains the data identifying either the initial load device (its key) or the boot service that requested the last operating system load. In addition, the load parameters (ie, a pathname and parameters) may also be specified.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The inherited Name serves as key of a System instance in an enterprise environment.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ComputerSystem object and its derivatives are Top Level Objects of CIM. They provide the scope for numerous components. Having unique System keys is required. A heuristic is defined to create the ComputerSystem Name to attempt to always generate the same Name, independent of discovery protocol. This prevents inventory and management problems where the same asset or entity is discovered multiple times, but can not be resolved to a single object. Use of the heuristic is optional, but recommended.

The NameFormat property identifies how the ComputerSystem Name is generated, using a heuristic. The heuristic is outlined, in detail, in the CIM V2 System Model spec. It assumes that the documented rules are traversed in order, to determine and assign a Name. The NameFormat Values list defines the precedence order for assigning the ComputerSystem Name. Several rules do map to the same Value.

Note that the ComputerSystem Name calculated using the heuristic is the System's key value. Other names can be assigned and used for the ComputerSystem, that better suit a business, using Aliases.

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

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

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).IdentifyingDescriptions")
</dt> </dl>

OtherIdentifyingInfo captures additional data, beyond System Name information, that could be used to identify a ComputerSystem. One example would be to hold the Fibre Channel World-Wide Name (WWN) of a node. Note that if only the Fibre Channel name is available and is unique (able to be used as the System key), then this property would be NULL and the WWN would become the System key, its data placed in the Name property.

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|System Power Controls\|001.2")
</dt> </dl>

Indicates the specific power-related capabilities of a ComputerSystem and its associated running OperatingSystem. The values, 0="Unknown", 1="Not Supported", and 2="Disabled" are self-explanatory. The value, 3="Enabled" indicates that the power management features are currently enabled but the exact feature set is unknown or the information is unavailable. "Power Saving Modes Entered Automatically" (4) describes that a system can change its power state based on usage or other criteria. "Power State Settable" (5) indicates that the SetPowerState method is supported. "Power Cycling Supported" (6) indicates that the SetPowerState method can be invoked with the PowerState input variable set to 5 ("Power Cycle"). "Timed Power On Supported" (7) indicates that the SetPowerState method can be invoked with the PowerState input variable set to 5 ("Power Cycle") and the Time parameter set to a specific date and time, or interval, for power-on.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

**Not Supported** (1)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (2)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (3)


</dt> <dd></dd> <dt>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>

**Power Saving Modes Entered Automatically** (4)


</dt> <dd></dd> <dt>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>

**Power State Settable** (5)


</dt> <dd></dd> <dt>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>

**Power Cycling Supported** (6)


</dt> <dd></dd> <dt>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>

**Timed Power On Supported** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Boolean indicating that the ComputerSystem, with its running OperatingSystem, supports power management. This boolean does not indicate that power management features are currently enabled, or if enabled, what features are supported. Refer to the PowerManagementCapabilities array for this information. If this boolean is false, the integer value 1 for the string, "Not Supported", should be the only entry in the PowerManagementCapabilities array.

</dd> <dt>

**PowerState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current power state of the ComputerSystem and its associated OperatingSystem. Regarding the Power Save states, these are defined as follows: Value 4 ("Power Save - Unknown") indicates that the System is known to be in a power save mode, but its exact status in this mode is unknown; 2 ("Power Save - Low Power Mode") indicates that the System is in a power save state but still functioning, and may exhibit degraded performance; 3 ("Power Save - Standby") describes that the System is not functioning but could be brought to full power 'quickly'; and value 7 ("Power Save - Warning") indicates that the ComputerSystem is in a warning state, though also in a power save mode.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Full_Power"></span><span id="full_power"></span><span id="FULL_POWER"></span>

**Full Power** (1)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

**Power Save - Low Power Mode** (2)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

**Power Save - Standby** (3)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>

**Power Save - Unknown** (4)


</dt> <dd></dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

**Power Cycle** (5)


</dt> <dd></dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

**Power Off** (6)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>

**Power Save - Warning** (7)


</dt> <dd></dd> </dl>

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

If enabled (value = 4), the UnitaryComputerSystem can be reset via hardware (e.g. the power and reset buttons). If disabled (value = 3), hardware reset is not allowed. In addition to Enabled and Disabled, other Values for the property are also defined - "Not Implemented" (5), "Other" (1) and "Unknown" (2).

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

An array (bag) of strings that specify the roles this System plays in the IT-environment. Subclasses of System may override this property to define explicit Roles values. Alternately, a Working Group may describe the heuristics, conventions and guidelines for specifying Roles. For example, for an instance of a networking system, the Roles property might contain the string, 'Switch' or 'Bridge'.

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

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ComputerSystem**](cim-computersystem.md)
</dt> </dl>

 

 





