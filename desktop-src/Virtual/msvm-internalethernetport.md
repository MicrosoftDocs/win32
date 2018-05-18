---
title: Msvm\_InternalEthernetPort class
description: Represents an internal Ethernet port (network adapter).
ms.assetid: '8af63a0c-46a4-42dc-ac2b-112bd87027cd'
keywords: ["Msvm_InternalEthernetPort class Hyper-V", "Msvm_InternalEthernetPort class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_InternalEthernetPort
- Msvm_InternalEthernetPort.RequestStateChange
- Msvm_InternalEthernetPort.SetPowerState
- Msvm_InternalEthernetPort.Reset
- Msvm_InternalEthernetPort.EnableDevice
- Msvm_InternalEthernetPort.OnlineDevice
- Msvm_InternalEthernetPort.QuiesceDevice
- Msvm_InternalEthernetPort.SaveProperties
- Msvm_InternalEthernetPort.RestoreProperties
- Msvm_InternalEthernetPort.Caption
- Msvm_InternalEthernetPort.Description
- Msvm_InternalEthernetPort.ElementName
- Msvm_InternalEthernetPort.InstallDate
- Msvm_InternalEthernetPort.Name
- Msvm_InternalEthernetPort.OperationalStatus
- Msvm_InternalEthernetPort.StatusDescriptions
- Msvm_InternalEthernetPort.Status
- Msvm_InternalEthernetPort.HealthState
- Msvm_InternalEthernetPort.EnabledState
- Msvm_InternalEthernetPort.RequestedState
- Msvm_InternalEthernetPort.TimeOfLastStateChange
- Msvm_InternalEthernetPort.SystemCreationClassName
- Msvm_InternalEthernetPort.SystemName
- Msvm_InternalEthernetPort.CreationClassName
- Msvm_InternalEthernetPort.PowerManagementSupported
- Msvm_InternalEthernetPort.PowerManagementCapabilities
- Msvm_InternalEthernetPort.Availability
- Msvm_InternalEthernetPort.StatusInfo
- Msvm_InternalEthernetPort.LastErrorCode
- Msvm_InternalEthernetPort.ErrorDescription
- Msvm_InternalEthernetPort.ErrorCleared
- Msvm_InternalEthernetPort.TotalPowerOnHours
- Msvm_InternalEthernetPort.IdentifyingDescriptions
- Msvm_InternalEthernetPort.AdditionalAvailability
- Msvm_InternalEthernetPort.MaxQuiesceTime
- Msvm_InternalEthernetPort.LocationIndicator
- Msvm_InternalEthernetPort.MaxSpeed
- Msvm_InternalEthernetPort.RequestedSpeed
- Msvm_InternalEthernetPort.PortNumber
- Msvm_InternalEthernetPort.OtherLinkTechnology
- Msvm_InternalEthernetPort.PermanentAddress
- Msvm_InternalEthernetPort.FullDuplex
- Msvm_InternalEthernetPort.AutoSense
- Msvm_InternalEthernetPort.SupportedMaximumTransmissionUnit
- Msvm_InternalEthernetPort.NetworkAddresses
- Msvm_InternalEthernetPort.Capabilities
- Msvm_InternalEthernetPort.CapabilityDescriptions
- Msvm_InternalEthernetPort.EnabledCapabilities
- Msvm_InternalEthernetPort.OtherEnabledCapabilities
- Msvm_InternalEthernetPort.OtherEnabledState
- Msvm_InternalEthernetPort.EnabledDefault
- Msvm_InternalEthernetPort.DeviceID
- Msvm_InternalEthernetPort.OtherIdentifyingInfo
- Msvm_InternalEthernetPort.PowerOnHours
- Msvm_InternalEthernetPort.UsageRestriction
- Msvm_InternalEthernetPort.OtherPortType
- Msvm_InternalEthernetPort.Speed
- Msvm_InternalEthernetPort.OtherNetworkPortType
- Msvm_InternalEthernetPort.LinkTechnology
- Msvm_InternalEthernetPort.ActiveMaximumTransmissionUnit
- Msvm_InternalEthernetPort.PortType
- Msvm_InternalEthernetPort.MaxDataSize
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_InternalEthernetPort class

Represents an internal Ethernet port (network adapter). This type of Ethernet port gives virtual machines (VMs) access to the virtualization server running the networking software. The internal network adapters allow the VMs network traffic to be routed or filtered before leaving the physical system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_InternalEthernetPort : CIM_EthernetPort
{
  string   Caption = "Ethernet Port";
  string   Description = "Microsoft Internal Ethernet Port";
  string   ElementName;
  datetime InstallDate;
  string   Name;
  uint16   OperationalStatus[] = 2;
  string   StatusDescriptions[] = { "OK" };
  string   Status;
  uint16   HealthState = 5;
  uint16   EnabledState = 5;
  uint16   RequestedState = 12;
  datetime TimeOfLastStateChange;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName = "Msvm_InternalEthernetPort";
  boolean  PowerManagementSupported;
  uint16   PowerManagementCapabilities[];
  uint16   Availability;
  uint16   StatusInfo;
  uint32   LastErrorCode;
  string   ErrorDescription;
  boolean  ErrorCleared;
  uint64   TotalPowerOnHours;
  string   IdentifyingDescriptions[];
  uint16   AdditionalAvailability[] = 6;
  uint64   MaxQuiesceTime;
  uint16   LocationIndicator;
  uint64   MaxSpeed = 1000000000;
  uint64   RequestedSpeed = 1000000000;
  uint16   PortNumber;
  string   OtherLinkTechnology;
  string   PermanentAddress;
  boolean  FullDuplex = TRUE;
  boolean  AutoSense = True;
  uint64   SupportedMaximumTransmissionUnit = 1500;
  string   NetworkAddresses[];
  uint16   Capabilities[];
  string   CapabilityDescriptions[];
  uint16   EnabledCapabilities[];
  string   OtherEnabledCapabilities[];
  string   OtherEnabledState;
  uint16   EnabledDefault = 2;
  string   DeviceID = "Microsoft:GUID\device-specific data";
  string   OtherIdentifyingInfo[];
  uint64   PowerOnHours;
  uint16   UsageRestriction = 4;
  string   OtherPortType;
  uint64   Speed;
  string   OtherNetworkPortType;
  uint16   LinkTechnology = 2;
  uint64   ActiveMaximumTransmissionUnit = 1500;
  uint16   PortType;
  uint32   MaxDataSize = ;
};
```

## Members

The **Msvm\_InternalEthernetPort** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_InternalEthernetPort** class has these methods.



| Method                 | Description                              |
|:-----------------------|:-----------------------------------------|
| **EnableDevice**       | This method is not supported.<br/> |
| **OnlineDevice**       | This method is not supported.<br/> |
| **QuiesceDevice**      | This method is not supported.<br/> |
| **RequestStateChange** | This method is not supported.<br/> |
| **Reset**              | This method is not supported.<br/> |
| **RestoreProperties**  | This method is not supported.<br/> |
| **SaveProperties**     | This method is not supported.<br/> |
| **SetPowerState**      | This method is not supported.<br/> |



 

### Properties

The **Msvm\_InternalEthernetPort** class has these properties.

<dl> <dt>

**ActiveMaximumTransmissionUnit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The active or negotiated maximum transmission unit (MTU) that can be supported. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235) and is always set to 1500.

</dd> <dt>

**AdditionalAvailability**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**Availability**")
</dt> </dl>

Any additional availability and status of the device, beyond that specified in the **Availability** property. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is always set to 6 (Not Applicable).

</dd> <dt>

**AutoSense**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the network port is capable of automatically determining the speed or other communications characteristics of the attached network media. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235) and is always set to **True**.

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_AssociatedPowerManagementService.PowerState", "[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**", "[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus", "MIF.DMTF\|Host Device\|001.5"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**AdditionalAvailability**")
</dt> </dl>

The primary availability and status of the device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EthernetPort**](cim-ethernetport.md).**CapabilityDescriptions**")
</dt> </dl>

Capabilities of the Ethernet port. For example, the device might support **AlertOnLan**, **WakeOnLan**, **Load Balancing**, or **FailOver**. If failover or load balancing capabilities are listed, a [**CIM\_SpareGroup**](https://msdn.microsoft.com/library/aa388480) (failover) or [**CIM\_ExtraCapacityGroup**](https://msdn.microsoft.com/library/aa387268) (load balancing) should also be defined to completely describe the capability. This property is inherited from [**CIM\_EthernetPort**](https://msdn.microsoft.com/library/mt446068).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="AlertOnLan"></span><span id="alertonlan"></span><span id="ALERTONLAN"></span>

**AlertOnLan** (2)


</dt> <dd></dd> <dt>

<span id="WakeOnLan"></span><span id="wakeonlan"></span><span id="WAKEONLAN"></span>

**WakeOnLan** (3)


</dt> <dd></dd> <dt>

<span id="FailOver"></span><span id="failover"></span><span id="FAILOVER"></span>

**FailOver** (4)


</dt> <dd></dd> <dt>

<span id="LoadBalancing"></span><span id="loadbalancing"></span><span id="LOADBALANCING"></span>

**LoadBalancing** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**CapabilityDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EthernetPort**](cim-ethernetport.md).**Capabilities**")
</dt> </dl>

An array of free-form strings that provides more detailed explanations for any of the Ethernet port features that are indicated in the **Capabilities** array. Note, each entry of this array is related to the entry in the **Capabilities** array that is located at the same index. This property is inherited from [**CIM\_EthernetPort**](https://msdn.microsoft.com/library/mt446068).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one- line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and is always set to "Ethernet Port".

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is always set to "Msvm\_InternalEthernetPort".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and is always set to "Microsoft Internal Ethernet Port".

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

An address or other identifying information used to uniquely name the logical device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is always set to "Microsoft:*GUID*\\*device-specific data*".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and is generated based on the NIC present in the host.

</dd> <dt>

**EnabledCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EthernetPort**](cim-ethernetport.md).**Capabilities**", "**CIM\_EthernetPort**.**OtherEnabledCapabilities**")
</dt> </dl>

Specifies which capabilities are enabled from the list of all supported ones, which are defined in the **Capabilities** array. This property is inherited from [**CIM\_EthernetPort**](https://msdn.microsoft.com/library/mt446068).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="AlertOnLan"></span><span id="alertonlan"></span><span id="ALERTONLAN"></span>

**AlertOnLan** (2)


</dt> <dd></dd> <dt>

<span id="WakeOnLan"></span><span id="wakeonlan"></span><span id="WAKEONLAN"></span>

**WakeOnLan** (3)


</dt> <dd></dd> <dt>

<span id="FailOver"></span><span id="failover"></span><span id="FAILOVER"></span>

**FailOver** (4)


</dt> <dd></dd> <dt>

<span id="LoadBalancing"></span><span id="loadbalancing"></span><span id="LOADBALANCING"></span>

**LoadBalancing** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An administrator's default or startup configuration for the enabled state of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is always set to 2 (Enabled).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**OtherEnabledState**")
</dt> </dl>

The enabled and disabled states of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is always set to 5 (Not Applicable).

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (5)


</dt> <dd>

Indicates the element does not support to be enabled or disabled.

</dd> </dl>

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Indicates whether the error reported in the **LastErrorCode** property is now cleared. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_DeviceErrorData.ErrorDescription")
</dt> </dl>

A free-form string that provides more information about the error recorded in the **LastErrorCode** property, and information on any corrective actions that may be taken. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) property and is not used.

</dd> <dt>

**FullDuplex**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the port is operating in full duplex mode. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235) and is always set to **TRUE**.

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to 5 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and operates within normal operational parameters and without error.

</dd> </dl>

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**OtherIdentifyingInfo**")
</dt> </dl>

An array of free-form strings that provide explanations and details behind the entries in the **OtherIdentifyingInfo** property array. Note that each entry of this array is related to the entry in the **OtherIdentifyingInfo** property array that is located at the same index. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

A **datetime** value that indicates when the object was installed. Lack of a value does not indicate that the object is not installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_DeviceErrorData.LastErrorCode")
</dt> </dl>

The last error code reported by the logical device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**LinkTechnology**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_NetworkPort**](cim-networkport.md).**OtherLinkTechnology**")
</dt> </dl>

The types of links. When set to 1 ("Other"), the related property **OtherLinkTechnology** contains a string description of the type of link. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235) and is always set to 2 (Ethernet).

</dd> <dt>

**LocationIndicator**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_AlarmDevice**](https://msdn.microsoft.com/library/aa386576).**AlarmState**", "**CIM\_AlarmDevice**.**AudioIndicatorIsDisabled**", "**CIM\_AlarmDevice**.**VisualIndicatorIsDisabled**", "**CIM\_AlarmDevice**.**MotionIndicatorIsDisabled**")
</dt> </dl>

The state of an indicator that is part of a device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not used.

</dd> <dt>

**MaxDataSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|BRIDGE-MIB.dot1dTpPortMaxInfo")
</dt> </dl>

The maximum size of the INFO (non-MAC) field that will be received or transmitted. This property is inherited from [**CIM\_EthernetPort**](https://msdn.microsoft.com/library/mt446068) and is always set to 1500.

</dd> <dt>

**MaxQuiesceTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("MilliSeconds")
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**MaxSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bits per Second")
</dt> </dl>

The maximum bandwidth of the port, in bits per second. This property is inherited from [**CIM\_LogicalPort**](https://msdn.microsoft.com/library/cc136869) and is always set to 1000000000.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**NetworkAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Ethernet/802.3 MAC addresses formatted as twelve hexadecimal digits (for example, "010203040506"), with each pair representing one of the six octets of the MAC address in "canonical" bit order (the Group address bit is found in the low order bit of the first character of the string.) This property is inherited from [**CIM\_EthernetPort**](https://msdn.microsoft.com/library/mt446068).

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

The current statuses of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to 2 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Indicates full functionality without errors.

</dd> </dl>

</dd> <dt>

**OtherEnabledCapabilities**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EthernetPort**](cim-ethernetport.md).**EnabledCapabilities**")
</dt> </dl>

An array of free-form strings that provides more detailed explanations for any of the enabled capabilities that are specified as 1 (Other). This property is inherited from [**CIM\_EthernetPort**](https://msdn.microsoft.com/library/mt446068).

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other.) This property must be set to null when the **EnabledState** property is any value other than 1. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is not used.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalDevice**](cim-logicaldevice.md).**IdentifyingDescriptions**")
</dt> </dl>

Any data, in addition to device ID information, that could be used to identify a logical device. For example, you could use this property to hold the operating system's user-friendly name for the device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**OtherLinkTechnology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_NetworkPort**](cim-networkport.md).**LinkTechnology**")
</dt> </dl>

A string value that describes the **LinkTechnology** property when it is set to 1 (Other). This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235) but is not used.

</dd> <dt>

**OtherNetworkPortType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_NetworkPort**](cim-networkport.md).**OtherPortType**"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalPort**](cim-logicalport.md).**PortType**")
</dt> </dl>

This property is deprecated. Use the **PortType** property. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235).

Deprecated description: The type of module, when the **PortType** property is set to 1 (Other.)

</dd> <dt>

**OtherPortType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalPort**](cim-logicalport.md).**PortType**")
</dt> </dl>

The type of module, when the **PortType** property is set to 1 (Other). This property is inherited from [**CIM\_LogicalPort**](https://msdn.microsoft.com/library/cc136869) and is always set to **NULL**.

</dd> <dt>

**PermanentAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Network Adapter 802 Port\|001.2")
</dt> </dl>

The network address that is hardcoded into a port. This address can be changed using a firmware upgrade or a software configuration. When this change is made, the field should be updated at the same time. This should be left blank if no hardcoded address exists for the network adapter. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235).

</dd> <dt>

**PortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network ports are often numbered relative to either a logical module or a network element. This value is 1 for emulated NICs, 0 for all others. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235).

</dd> <dt>

**PortType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The specific mode that is currently enabled for the port. When set to 1 (Other), the related property **OtherPortType** contains a string description of the type of port. This property is inherited from [**CIM\_EthernetPort**](https://msdn.microsoft.com/library/mt446068).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="50_Copper_10BaseT"></span><span id="50_copper_10baset"></span><span id="50_COPPER_10BASET"></span>

**50 Copper 10BaseT** (50)


</dt> <dd></dd> <dt>

<span id="10-100BaseT"></span><span id="10-100baset"></span><span id="10-100BASET"></span>

**10-100BaseT** (51)


</dt> <dd></dd> <dt>

<span id="100BaseT"></span><span id="100baset"></span><span id="100BASET"></span>

**100BaseT** (52)


</dt> <dd></dd> <dt>

<span id="1000BaseT"></span><span id="1000baset"></span><span id="1000BASET"></span>

**1000BaseT** (53)


</dt> <dd></dd> <dt>

<span id="2500BaseT"></span><span id="2500baset"></span><span id="2500BASET"></span>

**2500BaseT** (54)


</dt> <dd></dd> <dt>

<span id="10GBaseT"></span><span id="10gbaset"></span><span id="10GBASET"></span>

**10GBaseT** (55)


</dt> <dd></dd> <dt>

<span id="10GBase-CX4"></span><span id="10gbase-cx4"></span><span id="10GBASE-CX4"></span>

**10GBase-CX4** (56)


</dt> <dd></dd> <dt>

<span id="100_Fiber_100Base-FX"></span><span id="100_fiber_100base-fx"></span><span id="100_FIBER_100BASE-FX"></span>

**100 Fiber 100Base-FX** (100)


</dt> <dd></dd> <dt>

<span id="100Base-SX"></span><span id="100base-sx"></span><span id="100BASE-SX"></span>

**100Base-SX** (101)


</dt> <dd></dd> <dt>

<span id="1000Base-SX"></span><span id="1000base-sx"></span><span id="1000BASE-SX"></span>

**1000Base-SX** (102)


</dt> <dd></dd> <dt>

<span id="1000Base-LX"></span><span id="1000base-lx"></span><span id="1000BASE-LX"></span>

**1000Base-LX** (103)


</dt> <dd></dd> <dt>

<span id="1000Base-CX"></span><span id="1000base-cx"></span><span id="1000BASE-CX"></span>

**1000Base-CX** (104)


</dt> <dd></dd> <dt>

<span id="10GBase-SR"></span><span id="10gbase-sr"></span><span id="10GBASE-SR"></span>

**10GBase-SR** (105)


</dt> <dd></dd> <dt>

<span id="10GBase-SW"></span><span id="10gbase-sw"></span><span id="10GBASE-SW"></span>

**10GBase-SW** (106)


</dt> <dd></dd> <dt>

<span id="10GBase-LX4"></span><span id="10gbase-lx4"></span><span id="10GBASE-LX4"></span>

**10GBase-LX4** (107)


</dt> <dd></dd> <dt>

<span id="10GBase-LR"></span><span id="10gbase-lr"></span><span id="10GBASE-LR"></span>

**10GBase-LR** (108)


</dt> <dd></dd> <dt>

<span id="10GBase-LW"></span><span id="10gbase-lw"></span><span id="10GBASE-LW"></span>

**10GBase-LW** (109)


</dt> <dd></dd> <dt>

<span id="10GBase-ER"></span><span id="10gbase-er"></span><span id="10GBASE-ER"></span>

**10GBase-ER** (110)


</dt> <dd></dd> <dt>

<span id="10GBase-EW"></span><span id="10gbase-ew"></span><span id="10GBASE-EW"></span>

**10GBase-EW** (111)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>16000–65535</dd> </dl>

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PowerManagementCapabilities.PowerCapabilities")
</dt> </dl>

The power management capabilities of the device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PowerManagementCapabilities")
</dt> </dl>

Indicates whether the device can be power managed. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**PowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PoweredStatisticalData.PowerOnHours"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours"), **Counter**
</dt> </dl>

The number of consecutive hours that this device has been powered, since its last power cycle. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**RequestedSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bits per Second"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_LogicalPort**](cim-logicalport.md).**Speed**")
</dt> </dl>

The requested bandwidth of the port, in bits per second. The actual bandwidth is reported in the **Speed** property. This property is inherited from [**CIM\_LogicalPort**](https://msdn.microsoft.com/library/cc136869) and is always set to 1000000000.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the management service. When the **EnabledState** property is set to 5 (Not Applicable), then this property has no meaning. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is always set to 12 (Not Applicable).

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (12)


</dt> <dd>

Indicates that this instance does not support the **RequestedState** property.

</dd> </dl>

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bits per Second"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|MIB-II.ifSpeed", "MIF.DMTF\|Network Adapter 802 Port\|001.5")
</dt> </dl>

The current bandwidth of the port in bits per second. For ports that vary in bandwidth or for those where no accurate estimation can be made, this property should contain the nominal bandwidth. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) but it is not used.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Strings that describe the various **OperationalStatus** array values. Note that entries in this array are correlated with those at the same array index in **OperationalStatus**. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to "OK".

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Operational State\|006.4")
</dt> </dl>

The state of the logical device. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**SupportedMaximumTransmissionUnit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The maximum transmission unit (MTU) that can be supported. This property is inherited from [**CIM\_NetworkPort**](https://msdn.microsoft.com/library/mt432235) and is always set to 1500.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) but it is not supported

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The virtual machine ID in **GUID** form. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the **EnabledState** property of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is not used.

</dd> <dt>

**TotalPowerOnHours**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_PoweredStatisticalData.TotalPowerOnHours"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Hours"), **Counter**
</dt> </dl>

The total number of hours that this device has been powered. This property is inherited from [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and is not used.

</dd> <dt>

**UsageRestriction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

In some circumstances, a logical port might be identifiable as a front end or back end port. If there is no restriction on the use of the port, then the value should be set to 4 ("Not Restricted"). This property is inherited from [**CIM\_LogicalPort**](https://msdn.microsoft.com/library/cc136869) and is always set to 4 (Not Restricted).

</dd> </dl>

## Remarks

Access to the **Msvm\_InternalEthernetPort** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_EthernetPort**](cim-ethernetport.md)
</dt> <dt>

[**CIM\_EthernetPort**](https://msdn.microsoft.com/library/mt446068)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





