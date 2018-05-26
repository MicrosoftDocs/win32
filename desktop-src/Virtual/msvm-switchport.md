---
title: Msvm\_SwitchPort class
description: Represents a port on the switch.
ms.assetid: 8ecd95b8-2bde-4ea5-8f38-04e8eadc41b9
keywords:
- RequestStateChange method Hyper-V
- RequestStateChange method Hyper-V , Msvm_Switchport class
- Msvm_Switchport class Hyper-V , RequestStateChange method
- BroadcastReset method Hyper-V
- BroadcastReset method Hyper-V , Msvm_Switchport class
- Msvm_Switchport class Hyper-V , BroadcastReset method
- Msvm_SwitchPort class Hyper-V
- Msvm_SwitchPort class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_SwitchPort
- Msvm_SwitchPort.RequestStateChange
- Msvm_SwitchPort.BroadcastReset
- Msvm_SwitchPort.Caption
- Msvm_SwitchPort.ElementName
- Msvm_SwitchPort.InstallDate
- Msvm_SwitchPort.HealthState
- Msvm_SwitchPort.OtherEnabledState
- Msvm_SwitchPort.RequestedState
- Msvm_SwitchPort.SystemCreationClassName
- Msvm_SwitchPort.SystemName
- Msvm_SwitchPort.CreationClassName
- Msvm_SwitchPort.Description
- Msvm_SwitchPort.OperationalStatus
- Msvm_SwitchPort.EnabledState
- Msvm_SwitchPort.TimeOfLastStateChange
- Msvm_SwitchPort.ProtocolType
- Msvm_SwitchPort.ProtocolIFType
- Msvm_SwitchPort.PortNumber
- Msvm_SwitchPort.StatusDescriptions
- Msvm_SwitchPort.EnabledDefault
- Msvm_SwitchPort.Name
- Msvm_SwitchPort.NameFormat
- Msvm_SwitchPort.OtherTypeDescription
- Msvm_SwitchPort.BroadcastResetSupported
- Msvm_SwitchPort.ScopeOfResidence
- Msvm_SwitchPort.Status
- Msvm_SwitchPort.VMQOffloadWeight
- Msvm_SwitchPort.AllowedIPv6Addresses
- Msvm_SwitchPort.AllowedIPv4Addresses
- Msvm_SwitchPort.PreventIPSpoofing
- Msvm_SwitchPort.ChimneyOffloadWeight
- Msvm_SwitchPort.VMQOffloadUsage
- Msvm_SwitchPort.ChimneyOffloadUsage
- Msvm_SwitchPort.VMQOffloadLimit
- Msvm_SwitchPort.ChimneyOffloadLimit
- Msvm_SwitchPort.AllowMacSpoofing
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_SwitchPort class

Represents a port on the switch.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SwitchPort : CIM_SwitchPort
{
  string   Caption = "Switch Port";
  string   ElementName;
  datetime InstallDate;
  uint16   HealthState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  string   SystemCreationClassName = "Msvm_VirtualSwitch";
  string   SystemName;
  string   CreationClassName = "Msvm_SwitchPort";
  string   Description = "Microsoft Virtual Switch Port";
  uint16   OperationalStatus[] = 2;
  uint16   EnabledState = 5;
  datetime TimeOfLastStateChange;
  uint16   ProtocolType;
  uint16   ProtocolIFType = 1;
  uint16   PortNumber;
  String   StatusDescriptions[] = "OK";
  uint16   EnabledDefault = 2;
  String   Name;
  String   NameFormat;
  String   OtherTypeDescription = "Virtual Ethernet";
  boolean  BroadcastResetSupported = FALSE;
  string   ScopeOfResidence;
  string   Status;
  uint32   VMQOffloadWeight = 100;
  string   AllowedIPv6Addresses[];
  string   AllowedIPv4Addresses[];
  boolean  PreventIPSpoofing;
  uint32   ChimneyOffloadWeight = 0;
  uint32   VMQOffloadUsage;
  uint32   ChimneyOffloadUsage;
  uint32   VMQOffloadLimit;
  uint32   ChimneyOffloadLimit;
  boolean  AllowMacSpoofing;
};
```

## Members

The **Msvm\_SwitchPort** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_SwitchPort** class has these methods.



| Method                 | Description                              |
|:-----------------------|:-----------------------------------------|
| **BroadcastReset**     | This method is not supported.<br/> |
| **RequestStateChange** | This method is not supported.<br/> |



 

### Properties

The **Msvm\_SwitchPort** class has these properties.

<dl> <dt>

**AllowedIPv4Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The list of IPv4 addresses which are valid in ARP and neighbor Discovery packets.

Each address in the list must point a text string of an IPv4 address in dotted-decimal notation as in "192.168.16.0", an example of an IPv4 address in dotted-decimalnotation.

</dd> <dt>

**AllowedIPv6Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The list of IPv6 addresses which are valid in ARP and neighbor Discovery packets.The basic string representation consists of 8 hexadecimal numbers separated by colons.A string of consecutive zero numbers may be replaced with a double-colon.There can only be one double-colon in the string representation of the IPv6 address.The last 32 bits may be represented in IPv4-style dotted-octet notationif the address is a IPv4-compatible address.

</dd> <dt>

**AllowMacSpoofing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the port will allow MAC spoofing.



| Value                                                                                | Meaning                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | The port will allow MAC addresses to be spoofed. All valid unicast MAC address values are allowed except those of ports with the **AllowMacSpoofing** property set to **FALSE**.<br/> |
| <dl> <dt>**FALSE**</dt> </dl> | The port will allow only MAC addresses configured within Hyper-V management to be used.<br/>                                                                                          |



 

**Windows Server 2008:** The **AllowMacSpoofing** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**BroadcastResetSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("FC-SWAPI.INCITS-T11\|SWAPI\_PORT\_CONFIG\_CAPS\_T.PortForceLipSupported"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**BroadcastReset**")
</dt> </dl>

Indicates whether the instrumentation supports the **BroadcastReset** method. This property is inherited from [**CIM\_SwitchPort**](https://msdn.microsoft.com/library/cc136919) and is always set to **FALSE**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one- line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and is always set to "Switch Port".

</dd> <dt>

**ChimneyOffloadLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The current TCP Chimney Offloading resources limit on this port. The limit is the maximum usage of TCP Chimney Offloading resources on the port.

**Windows Server 2008:** The **ChimneyOffloadLimit** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**ChimneyOffloadUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The current TCP Chimney Offloading usage on this port. The usage is the amount of TCP Chimney Offloading resources in use on the port.

**Windows Server 2008:** The **ChimneyOffloadUsage** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**ChimneyOffloadWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The weight assigned to this port for TCP Chimney Offloading. The weight is the relative importance when assigning TCP Chimney Offloading resources. Setting the **ChimneyOffloadWeight** property to 0 disables TCP Chimney Offloading on the port. The default is 0.

**Windows Server 2008:** The **ChimneyOffloadWeight** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or the subclass used in the creation of an instance. This property is inherited from [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) and is always set to "Msvm\_SwitchPort".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifDescr")
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is always set to "Microsoft Virtual Switch Port".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An administrator's default or startup configuration for the Enabled State of an element. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is always set to 2 (Enabled).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifAdminStatus")
</dt> </dl>

The enabled and disabled states of this element. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is always set to 5 (Not Applicable).

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (5)


</dt> <dd>

The element does not support being enabled or disabled.

</dd> </dl>

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current health of the element. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to 5 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and operates within normal operational parameters and without error.

</dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

A datetime value that indicates when the object was installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is not used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

A string that identifies this protocol endpoint with either a port or an interface on a device. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264).

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The naming heuristic that is selected to ensure that the value of the Name property is unique. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is not used.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifOperStatus")
</dt> </dl>

The current statuses of the element. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is always set to 2 (OK).

<dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Full functionality without errors.

</dd> </dl>

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The enabled or disabled state of the element when the **EnabledState** property is set to 1 ("Other"). This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is not used.

</dd> <dt>

**OtherTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**ProtocolType**", "**CIM\_ProtocolEndpoint**.**ProtocolIFType**")
</dt> </dl>

A string that describes the type of protocol endpoint when the **Type** property of this class (or any of its subclasses) is set to 1 ("Other"). This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is always set to "Virtual Ethernet".

</dd> <dt>

**PortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|BRIDGE-MIB.dot1dPort")
</dt> </dl>

The numeric identifier for a switch port. This property is inherited from [**CIM\_SwitchPort**](https://msdn.microsoft.com/library/cc136919) but it is not used.

</dd> <dt>

**PreventIPSpoofing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the IP spoofing prevention is enabled on the port.

TRUE: IP Spoofing checks will be enabled on ARP and Neighbor Discoverypackets. Router Advertisements and Router redirects will be blocked from the port

FALSE: No IP spoofing checks will be performed.

</dd> <dt>

**ProtocolIFType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifType"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**OtherTypeDescription**")
</dt> </dl>

The IANA ifType MIB. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is always set to 1 (Other).

</dd> <dt>

**ProtocolType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**ProtocolIFType**"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**OtherTypeDescription**")
</dt> </dl>

Information to categorize and classify different instances of this class. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is not used.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The last requested or desired state for the management service. This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is always set to 12 (Not Applicable).

<dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (12)


</dt> <dd>

Indicates that this instance does not support the **RequestedState** property.

</dd> </dl>

</dd> <dt>

**ScopeOfResidence**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The AzMan scope for the switch service. This scope will be used when performing access checks for the switch service.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Status)
</dt> </dl>

The current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates whether an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898)

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to "OK".

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The creation class name of the scoping system. This property is inherited from [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) and is always set to "Msvm\_VirtualSwitch".

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**Name**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The system name of the scoping system. This property is inherited from [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifLastChange")
</dt> </dl>

The date or time when the enabled state of the element last changed. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is not used.

</dd> <dt>

**VMQOffloadLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The current VMQ offloading limit on this port. The limit is the maximum usage of VMQ offloading resources on the port.

**Windows Server 2008:** The **VMQOffloadLimit** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**VMQOffloadUsage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The current VMQ offloading usage on this port. The usage is the amount of VMQ resources in use on the port.

**Windows Server 2008:** The **VMQOffloadUsage** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**VMQOffloadWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The weight assigned to this port for virtual machine queue (VMQ) offloading. The weight is the relative importance when assigning VMQ resources. Setting the **VMQOffloadWeight** property to 0 disables VMQ on the port. The default is 100.



| Value                                                                          | Meaning                              |
|--------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>0</dt> </dl>   | Disables VMQ on the port.<br/> |
| <dl> <dt>100</dt> </dl> | Default value.<br/>            |



 

**Windows Server 2008:** The **VMQOffloadWeight** property is not supported until Windows Server 2008 R2.

</dd> </dl>

## Remarks

Access to the **Msvm\_SwitchPort** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SwitchPort**](cim-switchport.md)
</dt> <dt>

[**CIM\_SwitchPort**](https://msdn.microsoft.com/library/cc136919)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





