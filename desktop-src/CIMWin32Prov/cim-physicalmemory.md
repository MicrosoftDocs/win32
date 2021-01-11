---
description: The CIM\_PhysicalMemory class represents low-level memory devices, such as SIMMS, DIMMs, raw memory chips, and so on.
ms.assetid: a25c5f00-cd85-42e6-9b26-8e9380b3c73b
ms.tgt_platform: multiple
title: CIM_PhysicalMemory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_PhysicalMemory
- CIM_PhysicalMemory.BankLabel
- CIM_PhysicalMemory.Capacity
- CIM_PhysicalMemory.Caption
- CIM_PhysicalMemory.CreationClassName
- CIM_PhysicalMemory.DataWidth
- CIM_PhysicalMemory.Description
- CIM_PhysicalMemory.FormFactor
- CIM_PhysicalMemory.HotSwappable
- CIM_PhysicalMemory.InstallDate
- CIM_PhysicalMemory.InterleavePosition
- CIM_PhysicalMemory.Manufacturer
- CIM_PhysicalMemory.MemoryType
- CIM_PhysicalMemory.Model
- CIM_PhysicalMemory.Name
- CIM_PhysicalMemory.OtherIdentifyingInfo
- CIM_PhysicalMemory.PartNumber
- CIM_PhysicalMemory.PositionInRow
- CIM_PhysicalMemory.PoweredOn
- CIM_PhysicalMemory.Removable
- CIM_PhysicalMemory.Replaceable
- CIM_PhysicalMemory.SerialNumber
- CIM_PhysicalMemory.SKU
- CIM_PhysicalMemory.Speed
- CIM_PhysicalMemory.Status
- CIM_PhysicalMemory.Tag
- CIM_PhysicalMemory.TotalWidth
- CIM_PhysicalMemory.Version
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_PhysicalMemory class

The **CIM\_PhysicalMemory** class represents low-level memory devices, such as SIMMS, DIMMs, raw memory chips, and so on.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, UUID("{FAF76B7B-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_PhysicalMemory : CIM_Chip
{
  string   BankLabel;
  uint64   Capacity;
  string   Caption;
  string   CreationClassName;
  uint16   DataWidth;
  string   Description;
  uint16   FormFactor;
  boolean  HotSwappable;
  datetime InstallDate;
  uint32   InterleavePosition;
  string   Manufacturer;
  uint16   MemoryType;
  string   Model;
  string   Name;
  string   OtherIdentifyingInfo;
  string   PartNumber;
  uint32   PositionInRow;
  boolean  PoweredOn;
  boolean  Removable;
  boolean  Replaceable;
  string   SerialNumber;
  string   SKU;
  uint32   Speed;
  string   Status;
  string   Tag;
  uint16   TotalWidth;
  string   Version;
};
```

## Members

The **CIM\_PhysicalMemory** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PhysicalMemory** class has these properties.

<dl> <dt>

**BankLabel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.4")
</dt> </dl>

Labeled bank in which the memory is located. For example, "Bank 0" or "Bank A".

</dd> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.5"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bytes")
</dt> </dl>

Total capacity of the physical memory, in bytes.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

Short textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Name of the class or subclass used in the creation of an instance. When used with other key properties of the class, this property allows all instances of the class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**DataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.8"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bits")
</dt> </dl>

Data width of the physical memory, in bits. A data width of 0 (zero) , and a total width of 8, indicates that the memory is solely used to provide error correction bits.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
</dt> </dl>

Textual description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**FormFactor**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("FormFactor"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.6")
</dt> </dl>

Implementation form factor for the chip. For example, values such as SIMM, TSOP, or PGA can be specified.

This property is inherited from [**CIM\_Chip**](cim-chip.md).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

Other

</dd> <dt>

2
</dt> <dd>

SIP

</dd> <dt>

3
</dt> <dd>

DIP

</dd> <dt>

4
</dt> <dd>

ZIP

</dd> <dt>

5
</dt> <dd>

SOJ

</dd> <dt>

6
</dt> <dd>

Proprietary

</dd> <dt>

7
</dt> <dd>

SIMM

</dd> <dt>

8
</dt> <dd>

DIMM

</dd> <dt>

9
</dt> <dd>

TSOP

</dd> <dt>

10
</dt> <dd>

PGA

</dd> <dt>

11
</dt> <dd>

RIMM

</dd> <dt>

12
</dt> <dd>

SODIMM

</dd> <dt>

13
</dt> <dd>

SRIMM

</dd> <dt>

14
</dt> <dd>

SMD

</dd> <dt>

15
</dt> <dd>

SSMP

</dd> <dt>

16
</dt> <dd>

QFP

</dd> <dt>

17
</dt> <dd>

TQFP

</dd> <dt>

18
</dt> <dd>

SOIC

</dd> <dt>

19
</dt> <dd>

LCC

</dd> <dt>

20
</dt> <dd>

PLCC

</dd> <dt>

21
</dt> <dd>

BGA

</dd> <dt>

22
</dt> <dd>

FPBGA

</dd> <dt>

23
</dt> <dd>

LGA

</dd> </dl>

</dd> <dt>

**HotSwappable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the package can be hot-swapped. A physical package can be hot-swapped if the element can be replaced by a physically different (but equivalent) one while the containing package is turned on. For example, a fan component may be designed to be hot-swapped. All components that can be hot-swapped are inherently removable and replaceable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InterleavePosition**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device Mapped Addresses\|001.7")
</dt> </dl>

Position of the physical memory in an interleave. A value of 0 indicates non-interleaved, 1 indicates the first position, 2 indicates the second position, and so on. For example, in a 2:1 interleave, a value of 1 indicates that the memory is in the even position.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Name of the organization responsible for producing the physical element. For more information, see the **Vendor** property of [**CIM\_Product**](cim-product.md).

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**MemoryType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.9")
</dt> </dl>

Type of physical memory.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="DRAM"></span><span id="dram"></span>

**DRAM** (2)


</dt> <dd></dd> <dt>

<span id="Synchronous_DRAM"></span><span id="synchronous_dram"></span><span id="SYNCHRONOUS_DRAM"></span>

**Synchronous DRAM** (3)


</dt> <dd></dd> <dt>

<span id="Cache_DRAM"></span><span id="cache_dram"></span><span id="CACHE_DRAM"></span>

**Cache DRAM** (4)


</dt> <dd></dd> <dt>

<span id="EDO"></span><span id="edo"></span>

**EDO** (5)


</dt> <dd></dd> <dt>

<span id="EDRAM"></span><span id="edram"></span>

**EDRAM** (6)


</dt> <dd></dd> <dt>

<span id="VRAM"></span><span id="vram"></span>

**VRAM** (7)


</dt> <dd></dd> <dt>

<span id="SRAM"></span><span id="sram"></span>

**SRAM** (8)


</dt> <dd></dd> <dt>

<span id="RAM"></span><span id="ram"></span>

**RAM** (9)


</dt> <dd></dd> <dt>

<span id="ROM"></span><span id="rom"></span>

**ROM** (10)


</dt> <dd></dd> <dt>

<span id="Flash"></span><span id="flash"></span><span id="FLASH"></span>

**Flash** (11)


</dt> <dd></dd> <dt>

<span id="EEPROM"></span><span id="eeprom"></span>

**EEPROM** (12)


</dt> <dd></dd> <dt>

<span id="FEPROM"></span><span id="feprom"></span>

**FEPROM** (13)


</dt> <dd></dd> <dt>

<span id="EPROM"></span><span id="eprom"></span>

**EPROM** (14)


</dt> <dd></dd> <dt>

<span id="CDRAM"></span><span id="cdram"></span>

**CDRAM** (15)


</dt> <dd></dd> <dt>

<span id="3DRAM"></span><span id="3dram"></span>

**3DRAM** (16)


</dt> <dd></dd> <dt>

<span id="SDRAM"></span><span id="sdram"></span>

**SDRAM** (17)


</dt> <dd></dd> <dt>

<span id="SGRAM"></span><span id="sgram"></span>

**SGRAM** (18)


</dt> <dd></dd> <dt>

<span id="RDRAM"></span><span id="rdram"></span>

**RDRAM** (19)


</dt> <dd></dd> <dt>

<span id="DDR"></span><span id="ddr"></span>

**DDR** (20)


</dt> <dd></dd> <dt>

<span id="DDR2"></span><span id="ddr2"></span>

**DDR2** (21)


</dt> <dd></dd> <dt>

<span id="DDR2_FB-DIMM"></span><span id="ddr2_fb-dimm"></span>

**DDR2 FB-DIMM** (22)


</dt> <dd></dd> </dl>

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Name by which the physical element is generally known.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional data, beyond asset tag information, that can be used to identify a physical element. One example is bar-code data that is associated with an element, which also has an asset tag. Note that if only bar-code data is available, and is unique and able to be used as an element key, this property would be null and the bar-code data would be used as the class key in the **Tag** property. This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PartNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Part number assigned by the organization that produced or manufactured the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PositionInRow**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device Mapped Addresses\|001.6")
</dt> </dl>

Position of the physical memory in a row. For example, if it takes two 8-bit memory devices to form a 16-bit row, then a value of 2 indicates that the memory is the second device. A value of 0 is an invalid value for this property.

</dd> <dt>

**PoweredOn**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the physical element is powered on.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Removable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this element is designed to be taken in and out of the physical container in which it is normally found, without impairing the function of the overall packaging. A package is considered removable even if the power must be off to perform the removal. If the power can be on and the package removed, then the element is removable and can be hot-swapped. For example, an ungradable processor chip is removable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**Replaceable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, it is possible to replace the element with a physically different one. For example, some computer systems allow the main processor chip to be upgraded to one of a higher clock rating. In this case, the processor is said to be replaceable. All removable components are inherently replaceable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Manufacturer-allocated number used to identify the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**SKU**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Stock-keeping unit number for the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("nanoseconds")
</dt> </dl>

Speed of the physical memory, in nanoseconds.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
</dt> </dl>

Current status of the object. This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**Tag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Arbitrary string that uniquely identifies the physical element and serves as the element's key. This property can contain information, such as asset tag or serial number data. The key for [**CIM\_PhysicalElement**](cim-physicalelement.md) is placed very high in the object hierarchy to independently identify the hardware or entity, regardless of physical placement in (or on) cabinets, adapters, and so on. For example, a removable component that can be hot-swapped can be taken from its containing (scoping) package and be temporarily unused. The object still continues to exist and can even be inserted into a different scoping container. The key for a physical element is an arbitrary string that is defined independently of placement or location-oriented hierarchy.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**TotalWidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.7"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bits")
</dt> </dl>

Total width, in bits, of the physical memory, including check or error correction bits. If there are no error correction bits, the value in this property should match that specified for the **DataWidth** property.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Version of the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> </dl>

## Remarks

The **CIM\_PhysicalMemory** class is derived from [**CIM\_Chip**](cim-chip.md).

WMI does not implement this class. For WMI classes derived from **CIM\_PhysicalMemory**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Chip**](cim-chip.md)
</dt> </dl>

 

