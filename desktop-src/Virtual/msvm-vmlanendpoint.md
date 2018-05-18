---
title: Msvm\_VmLANEndpoint class
description: Represents the logical connection point for a network adapter.
ms.assetid: 'e7250373-e176-47df-97c6-90a2eb240094'
keywords: ["Msvm_VmLANEndpoint class Hyper-V", "Msvm_VmLANEndpoint class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_VmLANEndpoint
- Msvm_VmLANEndpoint.RequestStateChange
- Msvm_VmLANEndpoint.BroadcastReset
- Msvm_VmLANEndpoint.Caption
- Msvm_VmLANEndpoint.ElementName
- Msvm_VmLANEndpoint.InstallDate
- Msvm_VmLANEndpoint.Status
- Msvm_VmLANEndpoint.HealthState
- Msvm_VmLANEndpoint.OtherEnabledState
- Msvm_VmLANEndpoint.RequestedState
- Msvm_VmLANEndpoint.SystemCreationClassName
- Msvm_VmLANEndpoint.SystemName
- Msvm_VmLANEndpoint.CreationClassName
- Msvm_VmLANEndpoint.Description
- Msvm_VmLANEndpoint.OperationalStatus
- Msvm_VmLANEndpoint.EnabledState
- Msvm_VmLANEndpoint.TimeOfLastStateChange
- Msvm_VmLANEndpoint.NameFormat
- Msvm_VmLANEndpoint.ProtocolType
- Msvm_VmLANEndpoint.OtherTypeDescription
- Msvm_VmLANEndpoint.LANID
- Msvm_VmLANEndpoint.LANType
- Msvm_VmLANEndpoint.OtherLANType
- Msvm_VmLANEndpoint.MACAddress
- Msvm_VmLANEndpoint.AliasAddresses
- Msvm_VmLANEndpoint.GroupAddresses
- Msvm_VmLANEndpoint.ProtocolIFType
- Msvm_VmLANEndpoint.StatusDescriptions
- Msvm_VmLANEndpoint.EnabledDefault
- Msvm_VmLANEndpoint.Name
- Msvm_VmLANEndpoint.BroadcastResetSupported
- Msvm_VmLANEndpoint.MaxDataSize
- Msvm_VmLANEndpoint.Connected
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_VmLANEndpoint class

Represents the logical connection point for a network adapter. When the LAN endpoint is connected to a switch port, the network adapter connected to the LAN endpoint has network connectivity.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VmLANEndpoint : CIM_LANEndpoint
{
  string   Caption = "LAN Endpoint";
  string   ElementName;
  datetime InstallDate;
  string   Status;
  uint16   HealthState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  string   SystemCreationClassName = "Msvm_ComputerSystem";
  string   SystemName;
  string   CreationClassName = "Msvm_VmLANEndpoint";
  string   Description = "Microsoft Virtual LAN Endpoint";
  uint16   OperationalStatus[] = 2;
  uint16   EnabledState = 5;
  datetime TimeOfLastStateChange;
  string   NameFormat;
  uint16   ProtocolType;
  string   OtherTypeDescription = "Virtual Ethernet";
  string   LANID;
  uint16   LANType;
  string   OtherLANType;
  string   MACAddress;
  string   AliasAddresses[];
  string   GroupAddresses[];
  uint16   ProtocolIFType;
  string   StatusDescriptions[];
  uint16   EnabledDefault = 2;
  string   Name;
  boolean  BroadcastResetSupported = False;
  uint32   MaxDataSize = 1500;
  boolean  Connected;
};
```

## Members

The **Msvm\_VmLANEndpoint** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_VmLANEndpoint** class has these methods.



| Method                 | Description                              |
|:-----------------------|:-----------------------------------------|
| **BroadcastReset**     | This method is not supported.<br/> |
| **RequestStateChange** | This method is not supported.<br/> |



 

### Properties

The **Msvm\_VmLANEndpoint** class has these properties.

<dl> <dt>

**AliasAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Other unicast addresses that may be used. This property is inherited from [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865) and is not used.

</dd> <dt>

**BroadcastResetSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("FC-SWAPI.INCITS-T11\|SWAPI\_PORT\_CONFIG\_CAPS\_T.PortForceLipSupported"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**BroadcastReset**")
</dt> </dl>

Indicates whether the instrumentation supports the **BroadcastReset** method. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is always set to **False**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one- line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) and is always set to "LAN Endpoint".

</dd> <dt>

**Connected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is set to **TRUE** if the LAN endpoint is connected to a switch port.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or the subclass used in the creation of an instance. This property is inherited from [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) and is always set to "Msvm\_VmLANEndpoint".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifDescr")
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is always set to "Microsoft Virtual LAN Endpoint".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

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

**GroupAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The multicast addresses to which this LAN endpoint listens. This property is inherited from [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865) and is not used.

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

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date and time when the object was installed. Lack of a value does not indicate that the object is not installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is not used.

</dd> <dt>

**LANID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LANConnectivitySegment.LANID, CIM\_LANSegment.LANID")
</dt> </dl>

A label or identifier for the LAN Segment to which the Endpoint is connected. This property is inherited from [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865) and is not used.

</dd> <dt>

**LANType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_LANEndpoint**](cim-lanendpoint.md).**ProtocolIFType**"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LANConnectivitySegment.ConnectivityType, CIM\_LANSegment.LANType")
</dt> </dl>

The type of technology used on the LAN. This property is inherited from [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865) and is not used.

</dd> <dt>

**MACAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (12)
</dt> </dl>

The principal unicast address used. This property is inherited from [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865).

</dd> <dt>

**MaxDataSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bits")
</dt> </dl>

The largest information field that may be sent or received by the LANEndpoint. This property is inherited from [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865) and is always set to 1500.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

A string that identifies this protocol endpoint with either a port or an interface on a device. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264).

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The naming heuristic that is selected to ensure that the value of the **Name** property is unique. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264).

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

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is not used.

</dd> <dt>

**OtherLANType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**OtherTypeDescription**"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_LANConnectivitySegment.OtherTypeDescription", "[**CIM\_LANEndpoint**](cim-lanendpoint.md).**LANType**")
</dt> </dl>

A free-form string that describes the type of technology used on the LAN when the value of the **LANType** property is equal to 1 (Other). This property is inherited from [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865) and is not used.

</dd> <dt>

**OtherTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**ProtocolType**", "**CIM\_ProtocolEndpoint**.**ProtocolIFType**")
</dt> </dl>

The type of protocol endpoint when the **Type** property of this class (or any of its subclasses) is set to 1 (Other). This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is always set to "Virtual Ethernet".

</dd> <dt>

**ProtocolIFType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Enumeration is limited to Layer 2-related and reserved values for this subclass of protocol endpoint. 1 (Other). This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**ProtocolType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**ProtocolIFType**"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).**OtherTypeDescription**")
</dt> </dl>

This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is not used.

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

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string that specifies the current status of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) but is not used.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Strings that describe the various **OperationalStatus** array values. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is always set to **NULL**.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The creation class name of the scoping system. This property is inherited from [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) and is always set to "Msvm\_ComputerSystem".

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

</dd> </dl>

## Remarks

Access to the **Msvm\_VmLANEndpoint** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_LANEndpoint**](cim-lanendpoint.md)
</dt> <dt>

[**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





