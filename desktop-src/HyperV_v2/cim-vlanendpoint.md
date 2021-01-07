---
description: An endpoint on a switch or end station that is assigned to a VLAN, or accepts traffic from one or more VLANs.
ms.assetid: 20943be3-35c3-4bf5-8f1a-d4095fa6897e
title: CIM_VLANEndpoint class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VLANEndpoint
- CIM_VLANEndpoint.DesiredEndpointMode
- CIM_VLANEndpoint.OtherEndpointMode
- CIM_VLANEndpoint.OperationalEndpointMode
- CIM_VLANEndpoint.DesiredVLANTrunkEncapsulation
- CIM_VLANEndpoint.OtherTrunkEncapsulation
- CIM_VLANEndpoint.OperationalVLANTrunkEncapsulation
- CIM_VLANEndpoint.GVRPStatus
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_VLANEndpoint class

An endpoint on a switch or end station that is assigned to a VLAN, or accepts traffic from one or more VLANs.

## Syntax

``` syntax
[Abstract, Version("2.26.0"), UMLPackagePath("CIM::Network::VLAN"), AMENDMENT]
class CIM_VLANEndpoint : CIM_ProtocolEndpoint
{
  uint16 DesiredEndpointMode;
  string OtherEndpointMode;
  uint16 OperationalEndpointMode;
  uint16 DesiredVLANTrunkEncapsulation;
  string OtherTrunkEncapsulation;
  uint16 OperationalVLANTrunkEncapsulation;
  uint16 GVRPStatus;
};
```

## Members

The **CIM\_VLANEndpoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VLANEndpoint** class has these properties.

<dl> <dt>

**DesiredEndpointMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VLANEndpoint**.**OperationalEndpointMode**", "**CIM\_VLANEndpoint**.**OtherEndpointMode**")
</dt> </dl>

The requested VLAN mode for the endpoint.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Access"></span><span id="access"></span><span id="ACCESS"></span>

**Access** (2)


</dt> <dd></dd> <dt>

<span id="Dynamic_Auto"></span><span id="dynamic_auto"></span><span id="DYNAMIC_AUTO"></span>

**Dynamic Auto** (3)


</dt> <dd></dd> <dt>

<span id="Dynamic_Desirable"></span><span id="dynamic_desirable"></span><span id="DYNAMIC_DESIRABLE"></span>

**Dynamic Desirable** (4)


</dt> <dd></dd> <dt>

<span id="Trunk"></span><span id="trunk"></span><span id="TRUNK"></span>

**Trunk** (5)


</dt> <dd></dd> <dt>

<span id="Dot1Q_Tunnel"></span><span id="dot1q_tunnel"></span><span id="DOT1Q_TUNNEL"></span>

**Dot1Q Tunnel** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (7..32767)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (..)


</dt> <dd></dd> </dl>

</dd> <dt>

**DesiredVLANTrunkEncapsulation**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\_VLANEndpointCapabilities.SupportsTrunkEncapsulationNegotiation", "**CIM\_VLANEndpoint**.**OperationalVLANTrunkEncapsulation**", "**CIM\_VLANEndpoint**.**OtherTrunkEncapsulation**")
</dt> </dl>

The requested VLAN encapsulation type.

> [!Note]  
> This property is only used when the VLAN endpoint is in trunking mode.

 

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

**DMTF Reserved** (6..32767)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..)


</dt> <dd></dd> </dl>

</dd> <dt>

**GVRPStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VLANEndpoint**.**OperationalEndpointMode**, CIM\_VLANEndpointCapabilities.Dot1QTagging")
</dt> </dl>

Indicates whether GARP VLAN Registration Protocol (GVRP) is enabled or disabled on the trunk endpoint.

> [!Note]  
> This property is only used when GVRP is supported by the endpoint, and trunking mode is enabled.

 

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

**OperationalEndpointMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VLANEndpoint**.**DesiredEndpointMode**", "**CIM\_VLANEndpoint**.**OtherEndpointMode**")
</dt> </dl>

The current VLAN mode for the endpoint.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Access"></span><span id="access"></span><span id="ACCESS"></span>

**Access** (2)


</dt> <dd></dd> <dt>

<span id="Dynamic_Auto"></span><span id="dynamic_auto"></span><span id="DYNAMIC_AUTO"></span>

**Dynamic Auto** (3)


</dt> <dd></dd> <dt>

<span id="Dynamic_Desirable"></span><span id="dynamic_desirable"></span><span id="DYNAMIC_DESIRABLE"></span>

**Dynamic Desirable** (4)


</dt> <dd></dd> <dt>

<span id="Trunk"></span><span id="trunk"></span><span id="TRUNK"></span>

**Trunk** (5)


</dt> <dd></dd> <dt>

<span id="Dot1Q_Tunnel"></span><span id="dot1q_tunnel"></span><span id="DOT1Q_TUNNEL"></span>

**Dot1Q Tunnel** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (7..32767)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (..)


</dt> <dd></dd> </dl>

</dd> <dt>

**OperationalVLANTrunkEncapsulation**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VLANEndpoint**.**OtherTrunkEncapsulation**", "**CIM\_VLANEndpoint**.**DesiredVLANTrunkEncapsulation**")
</dt> </dl>

The current VLAN encapsulation type.

> [!Note]  
> This property is only used when the VLAN endpoint is in trunking mode.

 

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

**DMTF Reserved** (6..32767)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..)


</dt> <dd></dd> </dl>

</dd> <dt>

**OtherEndpointMode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VLANEndpoint**.**DesiredEndpointMode**", "**CIM\_VLANEndpoint**.**OperationalEndpointMode**")
</dt> </dl>

The type of VLAN endpoint model that is supported by the VLANEndpoint when the value of **DesiredEndpointMode** is set to "1" (other); otherwise, **NULL**.

</dd> <dt>

**OtherTrunkEncapsulation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_VLANEndpoint**.**DesiredVLANTrunkEncapsulation**", "**CIM\_VLANEndpoint**.**OperationalVLANTrunkEncapsulation**")
</dt> </dl>

The type of VLAN encapsulation that is supported by the VLAN endpoint when the value of the **DesiredVLANTrunkEncapsulation** property is set to 1 (other); otherwise, **NULL**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md)
</dt> </dl>

 

