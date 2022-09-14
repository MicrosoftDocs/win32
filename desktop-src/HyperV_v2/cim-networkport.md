---
description: A logical representation of a network port on a network device.
ms.assetid: afcfc93d-174e-43b5-a16f-28937b4bf81a
title: CIM_NetworkPort class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_NetworkPort
- CIM_NetworkPort.Speed
- CIM_NetworkPort.OtherNetworkPortType
- CIM_NetworkPort.PortNumber
- CIM_NetworkPort.LinkTechnology
- CIM_NetworkPort.OtherLinkTechnology
- CIM_NetworkPort.PermanentAddress
- CIM_NetworkPort.NetworkAddresses
- CIM_NetworkPort.FullDuplex
- CIM_NetworkPort.AutoSense
- CIM_NetworkPort.SupportedMaximumTransmissionUnit
- CIM_NetworkPort.ActiveMaximumTransmissionUnit
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_NetworkPort class

A logical representation of a network port on a network device.

## Syntax

``` syntax
[Abstract, Version("2.10.0"), UMLPackagePath("CIM::Device::Ports"), AMENDMENT]
class CIM_NetworkPort : CIM_LogicalPort
{
  uint64  Speed;
  string  OtherNetworkPortType;
  uint16  PortNumber;
  uint16  LinkTechnology;
  string  OtherLinkTechnology;
  string  PermanentAddress;
  string  NetworkAddresses[];
  boolean FullDuplex;
  boolean AutoSense;
  uint64  SupportedMaximumTransmissionUnit;
  uint64  ActiveMaximumTransmissionUnit;
};
```

## Members

The **CIM\_NetworkPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_NetworkPort** class has these properties.

<dl> <dt>

**ActiveMaximumTransmissionUnit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), **PUnit** ("byte")
</dt> </dl>

The active or negotiated maximum transmission unit (MTU) that is supported by the port.

</dd> <dt>

**AutoSense**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the port can automatically determine the speed or other communications characteristic of the attached network media; otherwise, **false**.

</dd> <dt>

**FullDuplex**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the port is operating in full duplex mode; otherwise, **false**.

</dd> <dt>

**LinkTechnology**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_NetworkPort**.**OtherLinkTechnology**")
</dt> </dl>

The link technology used by the port. When set to "1" (other), the **OtherLinkTechnology** property contains a description of the link type.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>

**Ethernet** (2)


</dt> <dd></dd> <dt>

<span id="IB"></span><span id="ib"></span>

**IB** (3)


</dt> <dd></dd> <dt>

<span id="FC"></span><span id="fc"></span>

**FC** (4)


</dt> <dd></dd> <dt>

<span id="FDDI"></span><span id="fddi"></span>

**FDDI** (5)


</dt> <dd></dd> <dt>

<span id="ATM"></span><span id="atm"></span>

**ATM** (6)


</dt> <dd></dd> <dt>

<span id="Token_Ring"></span><span id="token_ring"></span><span id="TOKEN_RING"></span>

**Token Ring** (7)


</dt> <dd></dd> <dt>

<span id="Frame_Relay"></span><span id="frame_relay"></span><span id="FRAME_RELAY"></span>

**Frame Relay** (8)


</dt> <dd></dd> <dt>

<span id="Infrared"></span><span id="infrared"></span><span id="INFRARED"></span>

**Infrared** (9)


</dt> <dd></dd> <dt>

<span id="BlueTooth"></span><span id="bluetooth"></span><span id="BLUETOOTH"></span>

**BlueTooth** (10)


</dt> <dd></dd> <dt>

<span id="Wireless_LAN"></span><span id="wireless_lan"></span><span id="WIRELESS_LAN"></span>

**Wireless LAN** (11)


</dt> <dd></dd> </dl>

</dd> <dt>

**NetworkAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Network Adapter 802 Port\|001.3")
</dt> </dl>

An array that contains the network addresses for the port.

</dd> <dt>

**OtherLinkTechnology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_NetworkPort**.**LinkTechnology**")
</dt> </dl>

The link technology when **LinkTechnology** is set to "1", (other).

</dd> <dt>

**OtherNetworkPortType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("**CIM\_NetworkPort**.**OtherPortType**"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_LogicalPort**](cim-logicalport.md).**PortType**")
</dt> </dl>

> [!Note]  
> Deprecated description: The module type of the port, when the **PortType** property contains 1 (other).

 

This property is deprecated. Instead, we recommend the **PortType** property in the [**CIM\_LogicalPort**](cim-logicalport.md) class.

</dd> <dt>

**PermanentAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Network Adapter 802 Port\|001.2")
</dt> </dl>

The network address that is hardcoded into a port. The hardcoded address can be changed using a firmware upgrade or a software configuration. When this change is made, this property should be updated at the same time. **PermanentAddress** should be left blank if the address doesn't exist.

</dd> <dt>

**PortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port number of the network port. Network ports are often numbered relative to either a logical module or a network element.

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Speed"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bits per Second"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|MIB-II.ifSpeed", "MIF.DMTF\|Network Adapter 802 Port\|001.5"), **PUnit** ("bit / second")
</dt> </dl>

The current bandwidth of the port in bits per second. For ports that vary in bandwidth, or for those where no accurate estimation can be made, this property should contain the nominal bandwidth.

</dd> <dt>

**SupportedMaximumTransmissionUnit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), **PUnit** ("byte")
</dt> </dl>

The maximum transmission unit (MTU) that is supported by the port.

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

[**CIM\_LogicalPort**](cim-logicalport.md)
</dt> </dl>

 

