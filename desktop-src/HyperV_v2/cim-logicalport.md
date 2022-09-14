---
description: The abstraction of a port or connection point of a device.
ms.assetid: ee725c64-587b-4e5f-9b1c-7a58902b0631
title: CIM_LogicalPort class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_LogicalPort
- CIM_LogicalPort.Speed
- CIM_LogicalPort.MaxSpeed
- CIM_LogicalPort.RequestedSpeed
- CIM_LogicalPort.UsageRestriction
- CIM_LogicalPort.PortType
- CIM_LogicalPort.OtherPortType
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_LogicalPort class

The abstraction of a port or connection point of a device.

## Syntax

``` syntax
[Abstract, Version("2.10.0"), UMLPackagePath("CIM::Device::Ports"), AMENDMENT]
class CIM_LogicalPort : CIM_LogicalDevice
{
  uint64 Speed;
  uint64 MaxSpeed;
  uint64 RequestedSpeed;
  uint16 UsageRestriction;
  uint16 PortType;
  string OtherPortType;
};
```

## Members

The **CIM\_LogicalPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_LogicalPort** class has these properties.

<dl> <dt>

**MaxSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bits per Second"), **PUnit** ("bit / second")
</dt> </dl>

The maximum bandwidth of the port, in bits per second.

</dd> <dt>

**OtherPortType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_LogicalPort**.**PortType**")
</dt> </dl>

Describes the type of module, when **PortType** is set to **Other** ("1").

</dd> <dt>

**PortType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_NetworkPort**](cim-networkport.md).**OtherNetworkPortType**")
</dt> </dl>

The port type.

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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (3..15999)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (16000..65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**RequestedSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bits per Second"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_LogicalPort**.**Speed**"), **PUnit** ("bit / second")
</dt> </dl>

The requested bandwidth of the port, in bits per second. The actual bandwidth is reported in the **Speed** property.

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bits per Second"), **PUnit** ("bit / second")
</dt> </dl>

The bandwidth of the port, in bits per second.

</dd> <dt>

**UsageRestriction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the port is restricted to being a front-end or back-end port.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Front-end_only"></span><span id="front-end_only"></span><span id="FRONT-END_ONLY"></span>

**Front-end only** (2)


</dt> <dd></dd> <dt>

<span id="Back-end_only"></span><span id="back-end_only"></span><span id="BACK-END_ONLY"></span>

**Back-end only** (3)


</dt> <dd></dd> <dt>

<span id="Not_restricted"></span><span id="not_restricted"></span><span id="NOT_RESTRICTED"></span>

**Not restricted** (4)


</dt> <dd></dd> </dl>

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

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> </dl>

 

