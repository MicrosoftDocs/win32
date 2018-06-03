---
title: Msvm\_VLANEndpoint class
description: Represents the VLAN endpoint of a switch port.
ms.assetid: 85cba5c6-7887-42c8-a551-91197d6f8a65
keywords:
- Msvm_VLANEndpoint class Hyper-V
- Msvm_VLANEndpoint class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_VLANEndpoint
- Msvm_VLANEndpoint.RequestStateChange
- Msvm_VLANEndpoint.BroadcastReset
- Msvm_VLANEndpoint.Caption
- Msvm_VLANEndpoint.ElementName
- Msvm_VLANEndpoint.InstallDate
- Msvm_VLANEndpoint.StatusDescriptions
- Msvm_VLANEndpoint.HealthState
- Msvm_VLANEndpoint.OtherEnabledState
- Msvm_VLANEndpoint.RequestedState
- Msvm_VLANEndpoint.SystemCreationClassName
- Msvm_VLANEndpoint.SystemName
- Msvm_VLANEndpoint.CreationClassName
- Msvm_VLANEndpoint.Description
- Msvm_VLANEndpoint.OperationalStatus
- Msvm_VLANEndpoint.EnabledState
- Msvm_VLANEndpoint.TimeOfLastStateChange
- Msvm_VLANEndpoint.NameFormat
- Msvm_VLANEndpoint.ProtocolType
- Msvm_VLANEndpoint.ProtocolIFType
- Msvm_VLANEndpoint.OtherTypeDescription
- Msvm_VLANEndpoint.DesiredEndpointMode
- Msvm_VLANEndpoint.OperationalEndpointMode
- Msvm_VLANEndpoint.OtherTrunkEncapsulation
- Msvm_VLANEndpoint.GVRPStatus
- Msvm_VLANEndpoint.Status
- Msvm_VLANEndpoint.EnabledDefault
- Msvm_VLANEndpoint.Name
- Msvm_VLANEndpoint.BroadcastResetSupported
- Msvm_VLANEndpoint.OtherEndpointMode
- Msvm_VLANEndpoint.DesiredVLANTrunkEncapsulation
- Msvm_VLANEndpoint.OperationalVLANTrunkEncapsulation
- Msvm_VLANEndpoint.SupportedEndpointModes
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_VLANEndpoint class

Represents the VLAN endpoint of a switch port. The configuration of this endpoint will change the way the switch port sends VLAN packets through the switch.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VLANEndpoint : CIM_VLANEndpoint
{
  string   Caption;
  string   ElementName;
  datetime InstallDate;
  string   StatusDescriptions[] = { "The service is running normally" };
  uint16   HealthState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  string   SystemCreationClassName = "Msvm_VirtualSwitch";
  string   SystemName;
  string   CreationClassName = "Msvm_VLANEndpoint";
  string   Description;
  uint16   OperationalStatus[] = 2;
  uint16   EnabledState = 5;
  datetime TimeOfLastStateChange;
  string   NameFormat;
  uint16   ProtocolType;
  uint16   ProtocolIFType = 1;
  string   OtherTypeDescription = "Virtual Ethernet";
  uint16   DesiredEndpointMode;
  uint16   OperationalEndpointMode;
  string   OtherTrunkEncapsulation;
  uint16   GVRPStatus;
  string   Status;
  uint16   EnabledDefault = 2;
  String   Name;
  boolean  BroadcastResetSupported = False;
  string   OtherEndpointMode;
  uint16   DesiredVLANTrunkEncapsulation;
  uint16   OperationalVLANTrunkEncapsulation;
  uint16   SupportedEndpointModes[];
};
```

## Members

The **Msvm\_VLANEndpoint** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msvm\_VLANEndpoint** class has these methods.



| Method                 | Description                              |
|:-----------------------|:-----------------------------------------|
| **BroadcastReset**     | This method is not supported.<br/> |
| **RequestStateChange** | This method is not supported.<br/> |



 

### Properties

The **Msvm\_VLANEndpoint** class has these properties.

<dl> <dt>

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

A short textual description (one line string) of the object. This property is inherited from [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class or the subclass used in the creation of an instance. This property is inherited from [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) and is always set to "Msvm\_VLANEndpoint".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIB.IETF\|IF-MIB.ifDescr")
</dt> </dl>

A textual description of the object. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264).

</dd> <dt>

**DesiredEndpointMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**", "**CIM\_VLANEndpoint**.**OtherEndpointMode**")
</dt> </dl>

The desired VLAN mode that is requested for use. (Note that the current mode is given by the **OperationalEndpointMode** property.) This property is inherited from [**CIM\_VLANEndpoint**](https://msdn.microsoft.com/library/cc150675).

The possible values are:

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Access"></span><span id="access"></span><span id="ACCESS"></span>

<span id="Access"></span><span id="access"></span><span id="ACCESS"></span>**Access** (2)


</dt> <dd>

The endpoint is in permanent non-trunking mode and negotiates to convert the link into a non-trunk link. The endpoint becomes a non-trunk interface.

</dd> <dt>

<span id="Dynamic_Auto"></span><span id="dynamic_auto"></span><span id="DYNAMIC_AUTO"></span>

<span id="Dynamic_Auto"></span><span id="dynamic_auto"></span><span id="DYNAMIC_AUTO"></span>**Dynamic Auto** (3)


</dt> <dd>

The endpoint can convert the link to a trunk link. The endpoint becomes a trunk interface if the neighboring interface is set to trunk or desirable mode.

</dd> <dt>

<span id="Dynamic_Desirable"></span><span id="dynamic_desirable"></span><span id="DYNAMIC_DESIRABLE"></span>

<span id="Dynamic_Desirable"></span><span id="dynamic_desirable"></span><span id="DYNAMIC_DESIRABLE"></span>**Dynamic Desirable** (4)


</dt> <dd>

The endpoint actively attempts to convert the link to a trunk link. In addition, the endpoint becomes a trunk interface if the neighboring interface is set to trunk, desirable, or auto mode. The default switch-port mode for all ethernet interfaces is dynamic desirable.

</dd> <dt>

<span id="Trunk"></span><span id="trunk"></span><span id="TRUNK"></span>

<span id="Trunk"></span><span id="trunk"></span><span id="TRUNK"></span>**Trunk** (5)


</dt> <dd>

The endpoint is in permanent trunking mode and negotiates to convert the link into a trunk link. The endpoint becomes a trunk interface even if the neighboring interface is not a trunk interface.

</dd> <dt>

<span id="Dot1Q_Tunnel"></span><span id="dot1q_tunnel"></span><span id="DOT1Q_TUNNEL"></span>

<span id="Dot1Q_Tunnel"></span><span id="dot1q_tunnel"></span><span id="DOT1Q_TUNNEL"></span>**Dot1Q Tunnel** (6)


</dt> <dd>

Configures the interface as a tunnel (non-trunking) endpoint to be connected in an asymmetric link with an 802.1Q trunk port. 802.1Q tunneling is used to maintain customer VLAN integrity across a service provider network.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

</dd> <dt>

**DesiredVLANTrunkEncapsulation**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_VLANEndpointCapabilities.SupportsTrunkEncapsulationNegotiation", "[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalVLANTrunkEncapsulation**", "**CIM\_VLANEndpoint**.**OtherTrunkEncapsulation**")
</dt> </dl>

The type of VLAN encapsulation that is requested for use. (Note that the encapsulation currently in use is given by the **OperationalVLANTrunkEncapsulation** property.) Note that this property is only applicable when the endpoint is operating in a trunking mode (see the **OperationalEndpointMode** property for additional details). This property is either 2 (Not Applicable) (that is, the endpoint will never be placed in a trunking mode), a particular type (802.1Q or Cisco ISL), or 5 (Negotiate) (that is, the result of the negotiation between this interface and its neighbor). The value, 5 (Negotiate) is not allowed if the endpoint does not support negotiation. This capability is hardware and vendor dependent. Refer to the associated **CIM\_VLANEndpointCapabilities**.doesTrunkEncapsulationNegotiation property to validate whether a particular endpoint (port) supports encapsulation negotiation. This property is inherited from [**CIM\_VLANEndpoint**](https://msdn.microsoft.com/library/cc150675).

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (2)


</dt> <dd></dd> <dt>

<span id="802.1q"></span><span id="802.1Q"></span>

**802.1q** (3)


</dt> <dd></dd> <dt>

<span id="Cisco_ISL"></span><span id="cisco_isl"></span><span id="CISCO_ISL"></span>

**Cisco ISL** (4)


</dt> <dd></dd> <dt>

<span id="Negotiate"></span><span id="negotiate"></span><span id="NEGOTIATE"></span>

**Negotiate** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

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

**GVRPStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OperationalEndpointMode**, CIM\_VLANEndpointCapabilities.Dot1QTagging")
</dt> </dl>

Indicates whether GARP VLAN Registration Protocol (GVRP) is enabled or disabled on the trunk endpoint/port. This property is 2 (Not Applicable) unless GVRP is supported by the endpoint. This is indicated in the **Capabilities** property, **CIM\_VLANEndpointCapabilities** class **Dot1QTagging** property. This property is applicable only when the endpoint is operating in trunking mode (determined by examining the **SwitchEndpointMode** property). This property is inherited from [**CIM\_VLANEndpoint**](https://msdn.microsoft.com/library/cc150675).

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (2)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (3)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (4)


</dt> <dd></dd> </dl>

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

The date and time when the object was installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) and is not used.

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

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The naming heuristic that is selected to ensure that the value of the **Name** property is unique. This property is inherited from [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/mt432264) and is not used.

</dd> <dt>

**OperationalEndpointMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**DesiredEndpointMode**", "**CIM\_VLANEndpoint**.**OtherEndpointMode**")
</dt> </dl>

The configuration mode for the VLAN endpoint. This property is inherited from [**CIM\_VLANEndpoint**](https://msdn.microsoft.com/library/cc150675).

The possible values are:

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

The endpoint is not VLAN aware.

</dd> <dt>

<span id="Access"></span><span id="access"></span><span id="ACCESS"></span>

<span id="Access"></span><span id="access"></span><span id="ACCESS"></span>**Access** (2)


</dt> <dd>

The endpoint is in permanent non-trunking mode and negotiates to convert the link into a non-trunk link. The endpoint becomes a non-trunk interface.

</dd> <dt>

<span id="Dynamic_Auto"></span><span id="dynamic_auto"></span><span id="DYNAMIC_AUTO"></span>

<span id="Dynamic_Auto"></span><span id="dynamic_auto"></span><span id="DYNAMIC_AUTO"></span>**Dynamic Auto** (3)


</dt> <dd>

The endpoint can convert the link to a trunk link. The endpoint becomes a trunk interface if the neighboring interface is set to trunk or desirable mode.

</dd> <dt>

<span id="Dynamic_Desirable"></span><span id="dynamic_desirable"></span><span id="DYNAMIC_DESIRABLE"></span>

<span id="Dynamic_Desirable"></span><span id="dynamic_desirable"></span><span id="DYNAMIC_DESIRABLE"></span>**Dynamic Desirable** (4)


</dt> <dd>

The endpoint actively attempts to convert the link to a trunk link. In addition, the endpoint becomes a trunk interface if the neighboring interface is set to trunk, desirable, or auto mode. The default switch-port mode for all ethernet interfaces is dynamic desirable.

</dd> <dt>

<span id="Trunk"></span><span id="trunk"></span><span id="TRUNK"></span>

<span id="Trunk"></span><span id="trunk"></span><span id="TRUNK"></span>**Trunk** (5)


</dt> <dd>

The endpoint is in permanent trunking mode and negotiates to convert the link into a trunk link. The endpoint becomes a trunk interface even if the neighboring interface is not a trunk interface.

</dd> <dt>

<span id="Dot1Q_Tunnel"></span><span id="dot1q_tunnel"></span><span id="DOT1Q_TUNNEL"></span>

<span id="Dot1Q_Tunnel"></span><span id="dot1q_tunnel"></span><span id="DOT1Q_TUNNEL"></span>**Dot1Q Tunnel** (6)


</dt> <dd>

Configures the interface as a tunnel (non-trunking) endpoint to be connected in an asymmetric link with an 802.1Q trunk port. 802.1Q tunneling is used to maintain customer VLAN integrity across a service provider network.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Vendor reserved.

</dd> </dl>

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

**OperationalVLANTrunkEncapsulation**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**OtherTrunkEncapsulation**", "**CIM\_VLANEndpoint**.**DesiredVLANTrunkEncapsulation**")
</dt> </dl>

The type of VLAN encapsulation in use on a trunk endpoint/port. This property is either 2 (Not Applicable) (that is, the endpoint is not operating in trunking mode), a particular type (3 - 802.1Q or 4 - Cisco ISL), 5 (Negotiate) (that is, the endpoints are negotiating the encapsulation type). Note that this property is only applicable when the endpoint is operating in a trunking mode (see the **OperationalEndpointMode** property for additional details). This property is inherited from [**CIM\_VLANEndpoint**](https://msdn.microsoft.com/library/cc150675).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (2)


</dt> <dd></dd> <dt>

<span id="802.1q"></span><span id="802.1Q"></span>

**802.1q** (3)


</dt> <dd></dd> <dt>

<span id="Cisco_ISL"></span><span id="cisco_isl"></span><span id="CISCO_ISL"></span>

**Cisco ISL** (4)


</dt> <dd></dd> <dt>

<span id="Negotiating"></span><span id="negotiating"></span><span id="NEGOTIATING"></span>

**Negotiating** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**EnabledState**")
</dt> </dl>

The enabled or disabled state of the element when the **EnabledState** property is set to 1 (Other). This property is inherited from [**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063) and is not used.

</dd> <dt>

**OtherEndpointMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**DesiredEndpointMode**", "**CIM\_VLANEndpoint**.**OperationalEndpointMode**")
</dt> </dl>

The type of VLAN endpoint model that is supported by this VLAN endpoint, when the value of the mode property is set to 1 (Other). This property should be set to **NULL** when the **OperationalEndpointMode** property is any value other than 1. This property is inherited from [**CIM\_VLANEndpoint**](https://msdn.microsoft.com/library/cc150675).

</dd> <dt>

**OtherTrunkEncapsulation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VLANEndpoint**](cim-vlanendpoint.md).**DesiredVLANTrunkEncapsulation**", "**CIM\_VLANEndpoint**.**OperationalVLANTrunkEncapsulation**")
</dt> </dl>

The type of VLAN encapsulation that is supported by this VLANEndpoint, when the value of the **OperationalVLANTrunkEncapsulation** property is set to 1 (Other). This property should be set to **NULL** when the desired encapsulation property is any value other than 1. This property is inherited from [**CIM\_VLANEndpoint**](https://msdn.microsoft.com/library/cc150675).

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

The current status of the object. Operational and non-operational status can be defined. Operational status can include "OK", "Degraded", and "Pred Fail". "Pred Fail" indicates whether an element is functioning properly, but is predicting a failure (for example, a SMART-enabled hard disk drive).

Non-operational status can include "Error", "Starting", "Stopping", and "Service". "Service" can apply during disk mirror-resilvering, reloading a user permissions list, or other administrative work. Not all such work is online, but the managed element is neither "OK" nor in one of the other states.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) but it is not supported.

</dd> <dt>

**SupportedEndpointModes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

The endpoint mode supported by this port. This is generated dynamically.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Propagated**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The creation class name of the scoping system. This property is inherited from [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) and is always set to "Msvm\_VirtualSwitch"

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

The [**Msvm\_NetworkElementSettingData**](msvm-networkelementsettingdata.md) class is used to hold the association between the **Msvm\_VLANEndpoint** and [**Msvm\_VLANEndpointSettingData**](msvm-vlanendpointsettingdata.md) classes.

Access to the **Msvm\_VLANEndpoint** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_VLANEndpoint**](cim-vlanendpoint.md)
</dt> <dt>

[**CIM\_VLANEndpoint**](https://msdn.microsoft.com/library/cc150675)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





