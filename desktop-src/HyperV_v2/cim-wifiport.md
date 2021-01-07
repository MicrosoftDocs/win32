---
description: Represents a wireless local area network communications device that conforms to the IEEE 802.11 series of specifications.
ms.assetid: c4e3345f-5c7d-4d1d-9a94-64112d7334ff
title: CIM_WiFiPort class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_WiFiPort
- CIM_WiFiPort.Speed
- CIM_WiFiPort.MaxSpeed
- CIM_WiFiPort.PortType
- CIM_WiFiPort.PermanentAddress
- CIM_WiFiPort.NetworkAddresses
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_WiFiPort class

Represents a wireless local area network communications device that conforms to the IEEE 802.11 series of specifications.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Device::Ports"), AMENDMENT]
class CIM_WiFiPort : CIM_NetworkPort
{
  uint64 Speed;
  uint64 MaxSpeed;
  uint16 PortType;
  string PermanentAddress;
  string NetworkAddresses[];
};
```

## Members

The **CIM\_WiFiPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_WiFiPort** class has these properties.

<dl> <dt>

**MaxSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("MaxSpeed")
</dt> </dl>

The maximum supported bandwidth, in bits per second, based on the operating mode specified in the **PortType** property. For example, **MaxSpeed** is "11000000" if **PortType** contains "71" (802.11b).

</dd> <dt>

**NetworkAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("NetworkAddresses")
</dt> </dl>

An array that contains the IEEE 802 EUI-48 MAC addresses. The MAC address is formatted as twelve hexadecimal digits, with each pair representing one of the six octets of the MAC address in canonical bit order.

</dd> <dt>

**PermanentAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PermanentAddress")
</dt> </dl>

The IEEE 802 EUI-48 MAC address of the port. The MAC address is formatted as twelve hexadecimal digits, with each pair representing one of the six octets of the MAC address in canonical bit order.

</dd> <dt>

**PortType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PortType")
</dt> </dl>

The 802.11 operating mode that is enabled on the port.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="802.11a"></span><span id="802.11A"></span>

**802.11a** (70)


</dt> <dd></dd> <dt>

<span id="802.11b"></span><span id="802.11B"></span>

**802.11b** (71)


</dt> <dd></dd> <dt>

<span id="802.11g"></span><span id="802.11G"></span>

**802.11g** (72)


</dt> <dd></dd> <dt>

<span id="802.11n"></span><span id="802.11N"></span>

**802.11n** (73)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (16000..)


</dt> <dd></dd> </dl>

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Speed")
</dt> </dl>

The data rate at which the current PPDU (PLCP (Physical Layer Convergence Protocol) Protocol Data Unit) was received, in bits per second. This value is encoded in the first 4 bits of the PLCP header in each PLCP frame.

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

[**CIM\_NetworkPort**](cim-networkport.md)
</dt> </dl>

 

