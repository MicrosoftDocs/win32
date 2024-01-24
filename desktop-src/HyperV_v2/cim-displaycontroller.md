---
description: Represents a display controller.
ms.assetid: 14598ae6-58e2-46ca-8653-b57e5833a224
title: CIM_DisplayController class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_DisplayController
- CIM_DisplayController.Description
- CIM_DisplayController.VideoProcessor
- CIM_DisplayController.VideoMemoryType
- CIM_DisplayController.OtherVideoMemoryType
- CIM_DisplayController.NumberOfVideoPages
- CIM_DisplayController.MaxMemorySupported
- CIM_DisplayController.AcceleratorCapabilities
- CIM_DisplayController.CapabilityDescriptions
- CIM_DisplayController.OtherVideoArchitecture
- CIM_DisplayController.VideoArchitecture
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_DisplayController class

Represents a display controller.

## Syntax

``` syntax
[Abstract, Version("2.25.0"), UMLPackagePath("CIM::Device::Controller"), AMENDMENT]
class CIM_DisplayController : CIM_Controller
{
  string Description;
  string VideoProcessor;
  uint16 VideoMemoryType;
  string OtherVideoMemoryType;
  uint32 NumberOfVideoPages;
  uint32 MaxMemorySupported;
  uint16 AcceleratorCapabilities[];
  string CapabilityDescriptions[];
  string OtherVideoArchitecture;
  uint16 VideoArchitecture;
};
```

## Members

The **CIM\_DisplayController** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_DisplayController** class has these properties.

<dl> <dt>

**AcceleratorCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_DisplayController**.**CapabilityDescriptions**")
</dt> </dl>

The graphics and 3D capabilities of the display controller.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Graphics_Accelerator"></span><span id="graphics_accelerator"></span><span id="GRAPHICS_ACCELERATOR"></span>

**Graphics Accelerator** (2)


</dt> <dd></dd> <dt>

<span id="3D_Accelerator"></span><span id="3d_accelerator"></span><span id="3D_ACCELERATOR"></span>

**3D Accelerator** (3)


</dt> <dd></dd> <dt>

<span id="PCI_Fast_Write"></span><span id="pci_fast_write"></span><span id="PCI_FAST_WRITE"></span>

**PCI Fast Write** (4)


</dt> <dd></dd> <dt>

<span id="MultiMonitor_Support"></span><span id="multimonitor_support"></span><span id="MULTIMONITOR_SUPPORT"></span>

**MultiMonitor Support** (5)


</dt> <dd></dd> <dt>

<span id="PCI_Mastering"></span><span id="pci_mastering"></span><span id="PCI_MASTERING"></span>

**PCI Mastering** (6)


</dt> <dd></dd> <dt>

<span id="Second_Monochrome_Adapter_Support"></span><span id="second_monochrome_adapter_support"></span><span id="SECOND_MONOCHROME_ADAPTER_SUPPORT"></span>

**Second Monochrome Adapter Support** (7)


</dt> <dd></dd> <dt>

<span id="Large_Memory_Address_Support"></span><span id="large_memory_address_support"></span><span id="LARGE_MEMORY_ADDRESS_SUPPORT"></span>

**Large Memory Address Support** (8)


</dt> <dd></dd> </dl>

</dd> <dt>

**CapabilityDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_DisplayController**.**AcceleratorCapabilities**")
</dt> </dl>

Detailed explanations for video accelerator features of the **AcceleratorCapabilities** array. The items in this array correspond to the array items in **AcceleratorCapabilities**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Video\|004.18")
</dt> </dl>

A text description of the object.

</dd> <dt>

**MaxMemorySupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), **PUnit** ("byte")
</dt> </dl>

The maximum amount of memory supported, in bytes.

</dd> <dt>

**NumberOfVideoPages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of video pages supported given the current resolutions and available memory.

</dd> <dt>

**OtherVideoArchitecture**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_DisplayController**.**VideoArchitecture**")
</dt> </dl>

A description of the video architecture type when the **VideoArchitecture** property contains "1" (Other).

</dd> <dt>

**OtherVideoMemoryType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_DisplayController**.**VideoMemoryType**")
</dt> </dl>

The video memory type when the **VideoMemoryType** property is "1" (Other).

</dd> <dt>

**VideoArchitecture**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The display controllers video architecture used to generate the video signal. Usually, a dedicated video processor generates the video signal in accordance with the specified architecture. The architecture indicates of the maximum resolution capability of the display controller.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="CGA"></span><span id="cga"></span>

**CGA** (2)


</dt> <dd></dd> <dt>

<span id="EGA"></span><span id="ega"></span>

**EGA** (3)


</dt> <dd></dd> <dt>

<span id="VGA"></span><span id="vga"></span>

**VGA** (4)


</dt> <dd></dd> <dt>

<span id="SVGA"></span><span id="svga"></span>

**SVGA** (5)


</dt> <dd></dd> <dt>

<span id="MDA"></span><span id="mda"></span>

**MDA** (6)


</dt> <dd></dd> <dt>

<span id="HGC"></span><span id="hgc"></span>

**HGC** (7)


</dt> <dd></dd> <dt>

<span id="MCGA"></span><span id="mcga"></span>

**MCGA** (8)


</dt> <dd></dd> <dt>

<span id="8514A"></span><span id="8514a"></span>

**8514A** (9)


</dt> <dd></dd> <dt>

<span id="XGA"></span><span id="xga"></span>

**XGA** (10)


</dt> <dd></dd> <dt>

<span id="Linear_Frame_Buffer"></span><span id="linear_frame_buffer"></span><span id="LINEAR_FRAME_BUFFER"></span>

**Linear Frame Buffer** (11)


</dt> <dd></dd> <dt>

<span id="PC-98"></span><span id="pc-98"></span>

**PC-98** (160)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (0x8000..)


</dt> <dd></dd> </dl>

</dd> <dt>

**VideoMemoryType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Video\|004.6"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_DisplayController**.**OtherVideoMemoryType**")
</dt> </dl>

The type of video memory.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="VRAM"></span><span id="vram"></span>

**VRAM** (2)


</dt> <dd></dd> <dt>

<span id="DRAM"></span><span id="dram"></span>

**DRAM** (3)


</dt> <dd></dd> <dt>

<span id="SRAM"></span><span id="sram"></span>

**SRAM** (4)


</dt> <dd></dd> <dt>

<span id="WRAM"></span><span id="wram"></span>

**WRAM** (5)


</dt> <dd></dd> <dt>

<span id="EDO_RAM"></span><span id="edo_ram"></span>

**EDO RAM** (6)


</dt> <dd></dd> <dt>

<span id="Burst_Synchronous_DRAM"></span><span id="burst_synchronous_dram"></span><span id="BURST_SYNCHRONOUS_DRAM"></span>

**Burst Synchronous DRAM** (7)


</dt> <dd></dd> <dt>

<span id="Pipelined_Burst_SRAM"></span><span id="pipelined_burst_sram"></span><span id="PIPELINED_BURST_SRAM"></span>

**Pipelined Burst SRAM** (8)


</dt> <dd></dd> <dt>

<span id="CDRAM"></span><span id="cdram"></span>

**CDRAM** (9)


</dt> <dd></dd> <dt>

<span id="3DRAM"></span><span id="3dram"></span>

**3DRAM** (10)


</dt> <dd></dd> <dt>

<span id="SDRAM"></span><span id="sdram"></span>

**SDRAM** (11)


</dt> <dd></dd> <dt>

<span id="SGRAM"></span><span id="sgram"></span>

**SGRAM** (12)


</dt> <dd></dd> </dl>

</dd> <dt>

**VideoProcessor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A text description of the video processor/controller.

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

[**CIM\_Controller**](cim-controller.md)
</dt> </dl>

 

