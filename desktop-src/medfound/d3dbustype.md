---
description: Specifies the type of I/O bus used by the graphics adapter.
ms.assetid: 11bb7e0e-8d49-45f2-89aa-7583dd925edf
title: D3DBUSTYPE enumeration (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DBUSTYPE
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DBUSTYPE enumeration

Specifies the type of I/O bus used by the graphics adapter.

## Syntax


```C++
typedef enum  { 
  D3DBUSTYPE_OTHER                                             = 0x00000000,
  D3DBUSTYPE_PCI                                               = 0x00000001,
  D3DBUSTYPE_PCIX                                              = 0x00000002,
  D3DBUSTYPE_PCIEXPRESS                                        = 0x00000003,
  D3DBUSTYPE_AGP                                               = 0x00000004,
  D3DBUSIMPL_MODIFIER_INSIDE_OF_CHIPSET                        = 0x00010000,
  D3DBUSIMPL_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_CHIP           = 0x00020000,
  D3DBUSIMPL_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_SOCKET         = 0x00030000,
  D3DBUSIMPL_MODIFIER_DAUGHTER_BOARD_CONNECTOR                 = 0x00040000,
  D3DBUSIMPL_MODIFIER_DAUGHTER_BOARD_CONNECTOR_INSIDE_OF_NUAE  = 0x00050000,
  D3DBUSIMPL_MODIFIER_NON_STANDARD                             = 0x80000000
} D3DBUSTYPE;
```



## Constants

<dl> <dt>

<span id="D3DBUSTYPE_OTHER"></span><span id="d3dbustype_other"></span>**D3DBUSTYPE\_OTHER**
</dt> <dd>

Indicates a type of bus other than the types listed here.

</dd> <dt>

<span id="D3DBUSTYPE_PCI"></span><span id="d3dbustype_pci"></span>**D3DBUSTYPE\_PCI**
</dt> <dd>

PCI bus.

</dd> <dt>

<span id="D3DBUSTYPE_PCIX"></span><span id="d3dbustype_pcix"></span>**D3DBUSTYPE\_PCIX**
</dt> <dd>

PCI-X bus.

</dd> <dt>

<span id="D3DBUSTYPE_PCIEXPRESS"></span><span id="d3dbustype_pciexpress"></span>**D3DBUSTYPE\_PCIEXPRESS**
</dt> <dd>

PCI Express bus.

</dd> <dt>

<span id="D3DBUSTYPE_AGP"></span><span id="d3dbustype_agp"></span>**D3DBUSTYPE\_AGP**
</dt> <dd>

Accelerated Graphics Port (AGP) bus.

</dd> <dt>

<span id="D3DBUSIMPL_MODIFIER_INSIDE_OF_CHIPSET"></span><span id="d3dbusimpl_modifier_inside_of_chipset"></span>**D3DBUSIMPL\_MODIFIER\_INSIDE\_OF\_CHIPSET**
</dt> <dd>

The implementation for the graphics adapter is in a motherboard chipset's north bridge. This flag implies that data never goes over an expansion bus (such as PCI or AGP) when it is transferred from main memory to the graphics adapter.

</dd> <dt>

<span id="D3DBUSIMPL_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_CHIP"></span><span id="d3dbusimpl_modifier_tracks_on_mother_board_to_chip"></span>**D3DBUSIMPL\_MODIFIER\_TRACKS\_ON\_MOTHER\_BOARD\_TO\_CHIP**
</dt> <dd>

Indicates that the graphics adapter is connected to a motherboard chipset's north bridge by tracks on the motherboard and all of the graphics adapter's chips are soldered to the motherboard. This flag implies that data never goes over an expansion bus (such as PCI or AGP) when it is transferred from main memory to the graphics adapter.

</dd> <dt>

<span id="D3DBUSIMPL_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_SOCKET"></span><span id="d3dbusimpl_modifier_tracks_on_mother_board_to_socket"></span>**D3DBUSIMPL\_MODIFIER\_TRACKS\_ON\_MOTHER\_BOARD\_TO\_SOCKET**
</dt> <dd>

The graphics adapter is connected to a motherboard chipset's north bridge by tracks on the motherboard, and all of the graphics adapter's chips are connected through sockets to the motherboard.

</dd> <dt>

<span id="D3DBUSIMPL_MODIFIER_DAUGHTER_BOARD_CONNECTOR"></span><span id="d3dbusimpl_modifier_daughter_board_connector"></span>**D3DBUSIMPL\_MODIFIER\_DAUGHTER\_BOARD\_CONNECTOR**
</dt> <dd>

The graphics adapter is connected to the motherboard through a daughterboard connector.

</dd> <dt>

<span id="D3DBUSIMPL_MODIFIER_DAUGHTER_BOARD_CONNECTOR_INSIDE_OF_NUAE"></span><span id="d3dbusimpl_modifier_daughter_board_connector_inside_of_nuae"></span>**D3DBUSIMPL\_MODIFIER\_DAUGHTER\_BOARD\_CONNECTOR\_INSIDE\_OF\_NUAE**
</dt> <dd>

The graphics adapter is connected to the motherboard through a daughterboard connector, and the graphics adapter is inside an enclosure that is not user accessible.

</dd> <dt>

<span id="D3DBUSIMPL_MODIFIER_NON_STANDARD"></span><span id="d3dbusimpl_modifier_non_standard"></span>**D3DBUSIMPL\_MODIFIER\_NON\_STANDARD**
</dt> <dd>

One of the D3DBUSIMPL\_MODIFIER\_MODIFIER\_Xxx flags is set.

</dd> </dl>

## Remarks

As many as three flags can be set. Flags in the range 0x00 through 0x04 (**D3DBUSTYPE\_Xxx**) provide the basic bus type. Flags in the range 0x10000 through 0x50000 (**D3DBUSIMPL\_MODIFIER\_Xxx**) modify the basic description. The driver sets one bus-type flag, and can set zero or one modifier flag. If the driver sets a modifier flag, it also sets the **D3DBUSIMPL\_MODIFIER\_NON\_STANDARD** flag. Flags are combined with a bitwise **OR**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>D3d9types.h (include D3d9.h)</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Video Enumerations](direct3d-video-enumerations.md)
</dt> </dl>

 

 




