---
description: Represents a physical memory device located on a computer system and available to the operating system.
ms.assetid: 34baca53-ab85-4e06-9853-71b904ede4ab
ms.tgt_platform: multiple
title: Win32_PhysicalMemory class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Win32_PhysicalMemory
- Win32_PhysicalMemory.Attributes
- Win32_PhysicalMemory.BankLabel
- Win32_PhysicalMemory.Capacity
- Win32_PhysicalMemory.Caption
- Win32_PhysicalMemory.ConfiguredClockSpeed
- Win32_PhysicalMemory.ConfiguredVoltage
- Win32_PhysicalMemory.CreationClassName
- Win32_PhysicalMemory.DataWidth
- Win32_PhysicalMemory.Description
- Win32_PhysicalMemory.DeviceLocator
- Win32_PhysicalMemory.FormFactor
- Win32_PhysicalMemory.HotSwappable
- Win32_PhysicalMemory.InstallDate
- Win32_PhysicalMemory.InterleaveDataDepth
- Win32_PhysicalMemory.InterleavePosition
- Win32_PhysicalMemory.Manufacturer
- Win32_PhysicalMemory.MaxVoltage
- Win32_PhysicalMemory.MemoryType
- Win32_PhysicalMemory.MinVoltage
- Win32_PhysicalMemory.Model
- Win32_PhysicalMemory.Name
- Win32_PhysicalMemory.OtherIdentifyingInfo
- Win32_PhysicalMemory.PartNumber
- Win32_PhysicalMemory.PositionInRow
- Win32_PhysicalMemory.PoweredOn
- Win32_PhysicalMemory.Removable
- Win32_PhysicalMemory.Replaceable
- Win32_PhysicalMemory.SerialNumber
- Win32_PhysicalMemory.SKU
- Win32_PhysicalMemory.SMBIOSMemoryType
- Win32_PhysicalMemory.Speed
- Win32_PhysicalMemory.Status
- Win32_PhysicalMemory.Tag
- Win32_PhysicalMemory.TotalWidth
- Win32_PhysicalMemory.TypeDetail
- Win32_PhysicalMemory.Version
api_type:
- DllExport
api_location:
- CIMWin32.dll
---

# Win32\_PhysicalMemory class

The **Win32\_PhysicalMemory** [WMI class](../wmisdk/retrieving-a-class.md) represents a physical memory device located on a computer system and available to the operating system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{FAF76B93-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class Win32_PhysicalMemory : CIM_PhysicalMemory
{
  uint32   Attributes;
  string   BankLabel;
  uint64   Capacity;
  string   Caption;
  uint32   ConfiguredClockSpeed;
  uint32   ConfiguredVoltage;
  string   CreationClassName;
  uint16   DataWidth;
  string   Description;
  string   DeviceLocator;
  uint16   FormFactor;
  boolean  HotSwappable;
  datetime InstallDate;
  uint16   InterleaveDataDepth;
  uint32   InterleavePosition;
  string   Manufacturer;
  uint32   MaxVoltage;
  uint16   MemoryType;
  uint32   MinVoltage;
  string   Model;
  string   Name;
  string   OtherIdentifyingInfo;
  string   PartNumber;
  uint32   PositionInRow;
  boolean  PoweredOn;
  boolean  Removable;
  boolean  Replaceable;
  string   SerialNumber;
  string   SKU;
  uint32   SMBIOSMemoryType;
  uint32   Speed;
  string   Status;
  string   Tag;
  uint16   TotalWidth;
  uint16   TypeDetail;
  string   Version;
};
```

## Members

The **Win32\_PhysicalMemory** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PhysicalMemory** class has these properties.

<dl> <dt>

**Attributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 17\|Attributes")
</dt> </dl>

SMBIOS - Type 17 - Attributes. Represents the RANK.

This value comes from the **Attributes** member of the **Memory Device** structure in the SMBIOS information.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**BankLabel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Memory Device\|002.4")
</dt> </dl>

Physically labeled bank where the memory is located.

Examples: "Bank 0", "Bank A"

This value comes from the **Bank Locator** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

</dd> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Memory Device\|002.5"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Total capacity of the physical memory—in bytes.

This value comes from the **Memory Device** structure in the SMBIOS version information. For SMBIOS versions 2.1 thru 2.6 the value comes from the **Size** member. For SMBIOS version 2.7+ the value comes from the **Extended Size** member.

This property is inherited from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Caption")
</dt> </dl>

Short description of the object—a one-line string.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ConfiguredClockSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 17\|Configured Memory Clock Speed")
</dt> </dl>

The configured clock speed of the memory device, in megahertz (MHz), or 0, if the speed is unknown.

This value comes from the **Configured Memory Clock Speed** member of the **Memory Device** structure in the SMBIOS information.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**ConfiguredVoltage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 17\|Configured voltage")
</dt> </dl>

Configured voltage for this device, in millivolts, or 0, if the voltage is unknown.

This value comes from the **Configured voltage** member of the **Memory Device** structure in the SMBIOS information.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the first concrete class that appears in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, the property allows all instances of this class and its subclasses to be identified uniquely.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**DataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Memory Device\|002.8"), [**Units**](../wmisdk/standard-qualifiers.md) ("bits")
</dt> </dl>

Data width of the physical memory—in bits. A data width of 0 (zero) and a total width of 8 (eight) indicates that the memory is used solely to provide error correction bits.

This value comes from the **Data Width** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Description")
</dt> </dl>

Description of an object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**DeviceLocator**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 17\|Device Locator")
</dt> </dl>

Label of the socket or circuit board that holds the memory.

Example: "SIMM 3"

This value comes from the **Device Locator** member of the **Memory Device** structure in the SMBIOS information.

</dd> <dt>

**FormFactor**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Memory Device\|002.6")
</dt> </dl>

Implementation form factor for the chip.

This value comes from the **Form Factor** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_Chip**](cim-chip.md).

<dt>



 (0)


</dt> <dd>

Unknown

</dd> <dt>



 (1)


</dt> <dd>

Other

</dd> <dt>



 (2)


</dt> <dd>

SIP

</dd> <dt>



 (3)


</dt> <dd>

DIP

</dd> <dt>



 (4)


</dt> <dd>

ZIP

</dd> <dt>



 (5)


</dt> <dd>

SOJ

</dd> <dt>



 (6)


</dt> <dd>

Proprietary

</dd> <dt>



 (7)


</dt> <dd>

SIMM

</dd> <dt>



 (8)


</dt> <dd>

DIMM

</dd> <dt>



 (9)


</dt> <dd>

TSOP

</dd> <dt>



 (10)


</dt> <dd>

PGA

</dd> <dt>



 (11)


</dt> <dd>

RIMM

</dd> <dt>



 (12)


</dt> <dd>

SODIMM

</dd> <dt>



 (13)


</dt> <dd>

SRIMM

</dd> <dt>



 (14)


</dt> <dd>

SMD

</dd> <dt>



 (15)


</dt> <dd>

SSMP

</dd> <dt>



 (16)


</dt> <dd>

QFP

</dd> <dt>



 (17)


</dt> <dd>

TQFP

</dd> <dt>



 (18)


</dt> <dd>

SOIC

</dd> <dt>



 (19)


</dt> <dd>

LCC

</dd> <dt>



 (20)


</dt> <dd>

PLCC

</dd> <dt>



 (21)


</dt> <dd>

BGA

</dd> <dt>



 (22)


</dt> <dd>

FPBGA

</dd> <dt>



 (23)


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

If **TRUE**, this physical media component can be replaced with a physically different but equivalent one while the containing package has the power applied. For example, a fan component may be designed to be hot-swapped. All components that can be hot-swapped are inherently removable and replaceable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Install Date")
</dt> </dl>

Date and time the object is installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InterleaveDataDepth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 20\|Interleaved Data Depth")
</dt> </dl>

Unsigned 16-bit integer maximum number of consecutive rows of data that are accessed in a single interleaved transfer from the memory device. If the value is 0 (zero), the memory is not interleaved.

</dd> <dt>

**InterleavePosition**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Memory Device Mapped Addresses\|001.7")
</dt> </dl>

Position of the physical memory in an interleave. For example, in a 2:1 interleave, a value of "1" indicates that the memory is in the "even" position.

This property is inherited from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

<dt>

0
</dt> <dd>

Noninterleaved

</dd> <dt>

1
</dt> <dd>

First position

</dd> <dt>

2
</dt> <dd>

Second position

</dd> </dl>

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Name of the organization responsible for producing the physical element.

This value comes from the **Manufacturer** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**MaxVoltage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 17\|Maximum voltage")
</dt> </dl>

The maximum operating voltage for this device, in millivolts, or 0, if the voltage is unknown.

This value comes from the **Maximum voltage** member of the **Memory Device** structure in the SMBIOS information.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**MemoryType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Memory Device\|002.9")
</dt> </dl>

Type of physical memory. This is a CIM value that is mapped to the SMBIOS value. The **SMBIOSMemoryType** property contains the raw SMBIOS memory type.

This value comes from the **Memory Type** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="DRAM"></span><span id="dram"></span>

<span id="DRAM"></span><span id="dram"></span>**DRAM** (2)


</dt> <dd></dd> <dt>

<span id="Synchronous_DRAM"></span><span id="synchronous_dram"></span><span id="SYNCHRONOUS_DRAM"></span>

<span id="Synchronous_DRAM"></span><span id="synchronous_dram"></span><span id="SYNCHRONOUS_DRAM"></span>**Synchronous DRAM** (3)


</dt> <dd></dd> <dt>

<span id="Cache_DRAM"></span><span id="cache_dram"></span><span id="CACHE_DRAM"></span>

<span id="Cache_DRAM"></span><span id="cache_dram"></span><span id="CACHE_DRAM"></span>**Cache DRAM** (4)


</dt> <dd></dd> <dt>

<span id="EDO"></span><span id="edo"></span>

<span id="EDO"></span><span id="edo"></span>**EDO** (5)


</dt> <dd></dd> <dt>

<span id="EDRAM"></span><span id="edram"></span>

<span id="EDRAM"></span><span id="edram"></span>**EDRAM** (6)


</dt> <dd></dd> <dt>

<span id="VRAM"></span><span id="vram"></span>

<span id="VRAM"></span><span id="vram"></span>**VRAM** (7)


</dt> <dd></dd> <dt>

<span id="SRAM"></span><span id="sram"></span>

<span id="SRAM"></span><span id="sram"></span>**SRAM** (8)


</dt> <dd></dd> <dt>

<span id="RAM"></span><span id="ram"></span>

<span id="RAM"></span><span id="ram"></span>**RAM** (9)


</dt> <dd></dd> <dt>

<span id="ROM"></span><span id="rom"></span>

<span id="ROM"></span><span id="rom"></span>**ROM** (10)


</dt> <dd></dd> <dt>

<span id="Flash"></span><span id="flash"></span><span id="FLASH"></span>

<span id="Flash"></span><span id="flash"></span><span id="FLASH"></span>**Flash** (11)


</dt> <dd></dd> <dt>

<span id="EEPROM"></span><span id="eeprom"></span>

<span id="EEPROM"></span><span id="eeprom"></span>**EEPROM** (12)


</dt> <dd></dd> <dt>

<span id="FEPROM"></span><span id="feprom"></span>

<span id="FEPROM"></span><span id="feprom"></span>**FEPROM** (13)


</dt> <dd></dd> <dt>

<span id="EPROM"></span><span id="eprom"></span>

<span id="EPROM"></span><span id="eprom"></span>**EPROM** (14)


</dt> <dd></dd> <dt>

<span id="CDRAM"></span><span id="cdram"></span>

<span id="CDRAM"></span><span id="cdram"></span>**CDRAM** (15)


</dt> <dd></dd> <dt>

<span id="3DRAM"></span><span id="3dram"></span>

<span id="3DRAM"></span><span id="3dram"></span>**3DRAM** (16)


</dt> <dd></dd> <dt>

<span id="SDRAM"></span><span id="sdram"></span>

<span id="SDRAM"></span><span id="sdram"></span>**SDRAM** (17)


</dt> <dd></dd> <dt>

<span id="SGRAM"></span><span id="sgram"></span>

<span id="SGRAM"></span><span id="sgram"></span>**SGRAM** (18)


</dt> <dd></dd> <dt>

<span id="RDRAM"></span><span id="rdram"></span>

<span id="RDRAM"></span><span id="rdram"></span>**RDRAM** (19)


</dt> <dd></dd> <dt>

<span id="DDR"></span><span id="ddr"></span>

<span id="DDR"></span><span id="ddr"></span>**DDR** (20)


</dt> <dd></dd> <dt>

<span id="DDR2"></span><span id="ddr2"></span>

<span id="DDR2"></span><span id="ddr2"></span>**DDR2** (21)


</dt> <dd>

DDR2—May not be available.

</dd> <dt>

<span id="DDR2_FB-DIMM"></span><span id="ddr2_fb-dimm"></span>

<span id="DDR2_FB-DIMM"></span><span id="ddr2_fb-dimm"></span>**DDR2 FB-DIMM** (22)


</dt> <dd>

DDR2—FB-DIMM,May not be available.

</dd> <dt>

24
</dt> <dd>

DDR3—May not be available.

</dd> <dt>

25
</dt> <dd>

FBD2

</dt> <dd></dd> <dt>

<span id="DDR4"></span><span id="DDR4"></span>**DDR4** (26)

</dd> </dl>

</dd> <dt>

**MinVoltage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 20\|Minimum voltage")
</dt> </dl>

The minimum operating voltage for this device, in millivolts, or 0, if the voltage is unknown.

This value comes from the **Minimum voltage** member of the **Memory Device** structure in the SMBIOS information.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
</dt> </dl>

Name for the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Name")
</dt> </dl>

Label for the object. When subclassed, the property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional data, beyond asset tag information, that can be used to identify a physical element. One example is bar code data associated with an element that also has an asset tag. If only bar code data is available and unique or able to be used as an element key, this property is be **NULL** and the bar code data is used as the class key in the tag property.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PartNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Part number assigned by the organization responsible for producing or manufacturing the physical element.

This value comes from the **Part Number** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**PositionInRow**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Memory Device Mapped Addresses\|001.6")
</dt> </dl>

Position of the physical memory in a row. For example, if it takes two 8-bit memory devices to form a 16-bit row, then a value of 2 (two) means that this memory is the second device—0 (zero) is an invalid value for this property.

This property is inherited from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

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

If **TRUE**, a physical component is removable (if it is designed to be taken in and out of the physical container in which it is normally found, without impairing the function of the overall packaging). A component can still be removable if power must be "off" to perform the removal. If power can be "on" and the component removed, then the element is removable and can be hot-swapped. For example, an upgradable processor chip is removable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**Replaceable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, this physical media component can be replaced with a physically different one. For example, some computer systems allow the main processor chip to be upgraded to one of a higher clock rating. In this case, the processor is said to be replaceable. All removable components are inherently replaceable.

This property is inherited from [**CIM\_PhysicalComponent**](cim-physicalcomponent.md).

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
</dt> </dl>

Manufacturer-allocated number to identify the physical element.

This value comes from the **Serial Number** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**SKU**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
</dt> </dl>

Stock keeping unit number for the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> <dt>

**SMBIOSMemoryType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 17\|Memory\_Type")
</dt> </dl>

The raw SMBIOS memory type. The value of the **MemoryType** property is a CIM value that is mapped to the SMBIOS value.

**Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not supported before Windows Server 2016 and Windows 10.

</dd> <dt>

**Speed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("nanoseconds")
</dt> </dl>

Speed of the physical memory—in nanoseconds.

This value comes from the **Speed** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (10), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Status")
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The possible values are.

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

Qualifiers: [**Key**](../wmisdk/key-qualifier.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**Override**](../wmisdk/standard-qualifiers.md) ("Tag"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Unique identifier for the physical memory device that is represented by an instance of **Win32\_PhysicalMemory**. This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

Example: "Physical Memory 1"

</dd> <dt>

**TotalWidth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Memory Device\|002.7"), [**Units**](../wmisdk/standard-qualifiers.md) ("bits")
</dt> </dl>

Total width, in bits, of the physical memory, including check or error correction bits. If there are no error correction bits, the value in this property should match what is specified for the **DataWidth** property.

This value comes from the **Total Width** member of the **Memory Device** structure in the SMBIOS information.

This property is inherited from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

</dd> <dt>

**TypeDetail**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("SMBIOS\|Type 17\|Type Detail")
</dt> </dl>

Type of physical memory represented.

This value comes from the **Type Detail** member of the **Memory Device** structure in the SMBIOS information.

<dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>**Reserved** (1)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (2)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (4)


</dt> <dd></dd> <dt>

<span id="Fast-paged"></span><span id="fast-paged"></span><span id="FAST-PAGED"></span>

<span id="Fast-paged"></span><span id="fast-paged"></span><span id="FAST-PAGED"></span>**Fast-paged** (8)


</dt> <dd></dd> <dt>

<span id="Static_column"></span><span id="static_column"></span><span id="STATIC_COLUMN"></span>

<span id="Static_column"></span><span id="static_column"></span><span id="STATIC_COLUMN"></span>**Static column** (16)


</dt> <dd></dd> <dt>

<span id="Pseudo-static"></span><span id="pseudo-static"></span><span id="PSEUDO-STATIC"></span>

<span id="Pseudo-static"></span><span id="pseudo-static"></span><span id="PSEUDO-STATIC"></span>**Pseudo-static** (32)


</dt> <dd></dd> <dt>

<span id="RAMBUS"></span><span id="rambus"></span>

<span id="RAMBUS"></span><span id="rambus"></span>**RAMBUS** (64)


</dt> <dd></dd> <dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>**Synchronous** (128)


</dt> <dd></dd> <dt>

<span id="CMOS"></span><span id="cmos"></span>

<span id="CMOS"></span><span id="cmos"></span>**CMOS** (256)


</dt> <dd></dd> <dt>

<span id="EDO"></span><span id="edo"></span>

<span id="EDO"></span><span id="edo"></span>**EDO** (512)


</dt> <dd></dd> <dt>

<span id="Window_DRAM"></span><span id="window_dram"></span><span id="WINDOW_DRAM"></span>

<span id="Window_DRAM"></span><span id="window_dram"></span><span id="WINDOW_DRAM"></span>**Window DRAM** (1024)


</dt> <dd></dd> <dt>

<span id="Cache_DRAM"></span><span id="cache_dram"></span><span id="CACHE_DRAM"></span>

<span id="Cache_DRAM"></span><span id="cache_dram"></span><span id="CACHE_DRAM"></span>**Cache DRAM** (2048)


</dt> <dd></dd> <dt>

<span id="Non-volatile"></span><span id="non-volatile"></span><span id="NON-VOLATILE"></span>

<span id="Non-volatile"></span><span id="non-volatile"></span><span id="NON-VOLATILE"></span>**Non-volatile** (4096)


</dt> <dd>

Nonvolatile

</dd> </dl>

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
</dt> </dl>

Version of the physical element.

This property is inherited from [**CIM\_PhysicalElement**](cim-physicalelement.md).

</dd> </dl>

## Remarks

The **Win32\_PhysicalMemory** class is derived from [**CIM\_PhysicalMemory**](cim-physicalmemory.md).

## Examples

The [Get-ComputerInfo - Query Computer Info From Local/Remote Computers - (WMI)](https://Gallery.TechNet.Microsoft.Com/Get-ComputerInfo-Query-23dd6042) PowerShell sample on TechNet Gallery uses a number of calls to hardware and software, including **Win32\_PhysicalMemory**, to display information about a local or remote system.

The [Server Report](https://Gallery.TechNet.Microsoft.Com/Server-Report-7b4ac2fb) PowerShell sample on TechNet gallery uses a number of calls to hardware and software, including **Win32\_PhysicalMemory**, to gather server information and publish in Word document.

The following PowerShell code sample retrieves information regarding the physical memory of the local computer.


```PowerShell
function get-WmiMemoryFormFactor {
param ([uint16] $char)

If ($char -ge 0 -and  $char  -le 22) {

switch ($char) {
0     {"00-Unknown"}
1     {"01-Other"}
2     {"02-SiP"}
3     {"03-DIP"}
4     {"04-ZIP"}
5     {"05-SOJ"}
6     {"06-Proprietary"}
7     {"07-SIMM"}
8     {"08-DIMM"}
9     {"09-TSOPO"}
10     {"10-PGA"}
11     {"11-RIM"}
12     {"12-SODIMM"}
13     {"13-SRIMM"}
14     {"14-SMD"}
15     {"15-SSMP"}
16     {"16-QFP"}
17     {"17-TQFP"}
18     {"18-SOIC"}
19     {"19-LCC"}
20     {"20-PLCC"}
21     {"21-FPGA"}
22     {"22-LGA"}
}
}

else {"{0} - undefined value" -f $char
}

Return
}

# Helper function to return memory Interleave  Position

function get-WmiInterleavePosition {
param ([uint32] $char)

If ($char -ge 0 -and  $char -le 2) {

switch ($char) {
0     {"00-Non-Interleaved"}
1     {"01-First Position"}
2     {"02-Second Position"}
}
}

else {"{0} - undefined value" -f $char
}

Return
}


# Helper function to return Memory Tupe
function get-WmiMemoryType {
param ([uint16] $char)

If ($char -ge 0 -and  $char  -le 20) {

switch ($char) {
0     {"00-Unknown"}
1     {"01-Other"}
2     {"02-DRAM"}
3     {"03-Synchronous DRAM"}
4     {"04-Cache DRAM"}
5     {"05-EDO"}
6     {"06-EDRAM"}
7     {"07-VRAM"}
8     {"08-SRAM"}
9     {"09-ROM"}
10     {"10-ROM"}
11     {"11-FLASH"}
12     {"12-EEPROM"}
13     {"13-FEPROM"}
14     {"14-EPROM"}
15     {"15-CDRAM"}
16     {"16-3DRAM"}
17     {"17-SDRAM"}
18     {"18-SGRAM"}
19     {"19-RDRAM"}
20     {"20-DDR"}
}

}

else {"{0} - undefined value" -f $char
}

Return
}


# Get the object
$memory = Get-WMIObject Win32_PhysicalMemory

#  Format and Print
"System has {0} memory sticks:" -f $memory.count

Foreach ($stick in $memory) {

# Do some conversions
$cap=$stick.capacity/1mb
$ff=get-WmiMemoryFormFactor($stick.FormFactor)
$ilp=get-WmiInterleavePosition($stick.InterleavePosition)
$mt=get-WMIMemoryType($stick.MemoryType)

# print details of each stick
"BankLabel            {0}"  -f $stick.banklabel
"Capacity (MB)        {0}"  -f $cap
"Caption              {0}"  -f $stick.Caption
"CreationClassName    {0}"  -f $stick.creationclassname
"DataWidth            {0}"  -f $stick.DataWidth
"Description          {0}"  -f $stick.Description
"DeviceLocator        {0}"  -f $stick.DeviceLocator
"FormFactor           {0}"  -f $ff
"HotSwappable         {0}"  -f $stick.HotSwappable
"InstallDate          {0}"  -f $stick.InstallDate
"InterleaveDataDepth  {0}"  -f $stick.InterleaveDataDepth
"InterleavePosition   {0}"  -f $ilp
"Manufacturer         {0}"  -f $stick.Manufacturer
"MemoryType           {0}"  -f $mt
"Model                {0}"  -f $stick.Model
"Name                 {0}"  -f $stick.Name
"OtherIdentifyingInfo {0}"  -f $stick.OtherIdentifyingInfo
"PartNumber           {0}"  -f $stick.PartNumber
"PositionInRow        {0}"  -f $stick.PositionInRow
"PoweredOn            {0}"  -f $stick.PoweredOn
"Removable            {0}"  -f $stick.Removable
"Replaceable          {0}"  -f $stick.Replaceable
"SerialNumber         {0}"  -f $stick.SerialNumber
"SKU                  {0}"  -f $stick.SKU 
"Speed                {0}"  -f $stick.Speed 
"Status               {0}"  -f $stick.Status
"Tag                  {0}"  -f $stick.Tag
"TotalWidth           {0}"  -f $stick.TotalWidth 
"TypeDetail           {0}"  -f $stick.TypeDetail
"Version              {0}"  -f $stick.Version
""
}
"-----"
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PhysicalMemory**](cim-physicalmemory.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
