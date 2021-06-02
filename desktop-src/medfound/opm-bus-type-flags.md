---
description: The flags listed in the following table specify the type of I/O bus used by the graphics adapter.
ms.assetid: 6c8ec020-5f12-453b-bbeb-3baabb1ca213
title: OPM Bus Type Flags (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM Bus Type Flags

The flags listed in the following table specify the type of I/O bus used by the graphics adapter.



| Constant/value                                                                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="OPM_BUS_TYPE_OTHER"></span><span id="opm_bus_type_other"></span><dl> <dt>**OPM\_BUS\_TYPE\_OTHER**</dt> <dt>0x00000000</dt> </dl>                                                                                                                                                                      | Indicates a type of bus other than the types listed here.<br/>                                                                                                                                                                                                                                                                                                                       |
| <span id="OPM_BUS_TYPE_PCI"></span><span id="opm_bus_type_pci"></span><dl> <dt>**OPM\_BUS\_TYPE\_PCI**</dt> <dt>0x00000001</dt> </dl>                                                                                                                                                                            | PCI bus.<br/>                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="OPM_BUS_TYPE_PCIX"></span><span id="opm_bus_type_pcix"></span><dl> <dt>**OPM\_BUS\_TYPE\_PCIX**</dt> <dt>0x00000002</dt> </dl>                                                                                                                                                                         | PCI-X bus.<br/>                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="OPM_BUS_TYPE_PCIEXPRESS"></span><span id="opm_bus_type_pciexpress"></span><dl> <dt>**OPM\_BUS\_TYPE\_PCIEXPRESS**</dt> <dt>0x00000003</dt> </dl>                                                                                                                                                       | PCI Express bus.<br/>                                                                                                                                                                                                                                                                                                                                                                |
| <span id="OPM_BUS_TYPE_AGP"></span><span id="opm_bus_type_agp"></span><dl> <dt>**OPM\_BUS\_TYPE\_AGP**</dt> <dt>0x00000004</dt> </dl>                                                                                                                                                                            | Accelerated Graphics Port (AGP) bus.<br/>                                                                                                                                                                                                                                                                                                                                            |
| <span id="OPM_BUS_IMPLEMENTATION_MODIFIER_INSIDE_OF_CHIPSET"></span><span id="opm_bus_implementation_modifier_inside_of_chipset"></span><dl> <dt>**OPM\_BUS\_IMPLEMENTATION\_MODIFIER\_INSIDE\_OF\_CHIPSET**</dt> <dt>0x00010000</dt> </dl>                                                                      | The implementation for the graphics adapter is in a motherboard chipset's north bridge. This flag implies that data never goes over an expansion bus (such as PCI or AGP) when it is transferred from main memory to the graphics adapter. <br/>                                                                                                                                     |
| <span id="OPM_BUS_IMPLEMENTATION_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_CHIP"></span><span id="opm_bus_implementation_modifier_tracks_on_mother_board_to_chip"></span><dl> <dt>**OPM\_BUS\_IMPLEMENTATION\_MODIFIER\_TRACKS\_ON\_MOTHER\_BOARD\_TO\_CHIP**</dt> <dt>0x00020000</dt> </dl>                            | The graphics adapter is connected to a motherboard chipset's north bridge by tracks on the motherboard, and all of the graphics adapter's chips (integrated circuits) are soldered to the motherboard. <br/>                                                                                                                                                                         |
| <span id="OPM_BUS_IMPLEMENTATION_MODIFIER_TRACKS_ON_MOTHER_BOARD_TO_SOCKET"></span><span id="opm_bus_implementation_modifier_tracks_on_mother_board_to_socket"></span><dl> <dt>**OPM\_BUS\_IMPLEMENTATION\_MODIFIER\_TRACKS\_ON\_MOTHER\_BOARD\_TO\_SOCKET**</dt> <dt>0x00030000</dt> </dl>                      | The graphics adapter is connected to a motherboard chipset's north bridge by tracks on the motherboard, and all of the graphics adapter's chips are connected through sockets to the motherboard.<br/>                                                                                                                                                                               |
| <span id="OPM_BUS_IMPLEMENTATION_MODIFIER_DAUGHTER_BOARD_CONNECTOR"></span><span id="opm_bus_implementation_modifier_daughter_board_connector"></span><dl> <dt>**OPM\_BUS\_IMPLEMENTATION\_MODIFIER\_DAUGHTER\_BOARD\_CONNECTOR**</dt> <dt>0x00040000</dt> </dl>                                                 | The graphics adapter is connected to the motherboard through a daughterboard connector.<br/>                                                                                                                                                                                                                                                                                         |
| <span id="OPM_BUS_IMPLEMENTATION_MODIFIER_DAUGHTER_BOARD_CONNECTOR_INSIDE_OF_NUAE"></span><span id="opm_bus_implementation_modifier_daughter_board_connector_inside_of_nuae"></span><dl> <dt>**OPM\_BUS\_IMPLEMENTATION\_MODIFIER\_DAUGHTER\_BOARD\_CONNECTOR\_INSIDE\_OF\_NUAE**</dt> <dt>0x00050000</dt> </dl> | The graphics adapter is connected to the motherboard through a daughterboard connector, and the graphics adapter is inside an enclosure that is not user accessible.<br/>                                                                                                                                                                                                            |
| <span id="OPM_BUS_IMPLEMENTATION_MODIFIER_NON_STANDARD"></span><span id="opm_bus_implementation_modifier_non_standard"></span><dl> <dt>**OPM\_BUS\_IMPLEMENTATION\_MODIFIER\_NON\_STANDARD**</dt> <dt>0x80000000</dt> </dl>                                                                                      | Nonstandard modifier. (Optional.)<br/>                                                                                                                                                                                                                                                                                                                                               |
| <span id="OPM_COPP_COMPATIBLE_BUS_TYPE_INTEGRATED"></span><span id="opm_copp_compatible_bus_type_integrated"></span><dl> <dt>**OPM\_COPP\_COMPATIBLE\_BUS\_TYPE\_INTEGRATED**</dt> <dt>0x80000000</dt> </dl>                                                                                                     | Integrated bus. This flag is used only in COPP emulation mode. It indicates that the command and status signals between the graphics adapter and other subsystems on the computer are not available on an expansion bus that has a public specification and standard connector type, unless it is a memory bus. This flag can be combined with an **OPM\_BUS\_TYPE\_Xxx** flag.<br/> |



## Remarks

Up to three flags can be set, using a bitwise **OR**. Flags in the range 0x00 through 0x04 (**OPM\_BUS\_TYPE\_Xxx**) give the basic bus type. Flags in the range 0x10000 through 0x50000 (**OPM\_BUS\_IMPLEMENTATION\_MODIFIER\_Xxx**) modify the basic description. The driver sets one bus-type flag, and can optionally set up to one modifier flag. In addition, the driver can optionally set the **OPM\_BUS\_IMPLEMENTATION\_MODIFIER\_NON\_STANDARD** flag.

In COPP emulation mode, the driver does not use the modifier flags, but it might set the **OPM\_COPP\_COMPATIBLE\_BUS\_TYPE\_INTEGRATED** flag.

The OPM\_BUG\_TYPE\_Xxxx flags and the **OPM\_COPP\_COMPATIBLE\_BUS\_TYPE\_INTEGRATED** flag are equivalent to values from the [**COPP\_BusType**](/windows/win32/api/dxva9typ/ne-dxva9typ-copp_bustype) enumeration used in Certified Output Protection Protocol (COPP).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[OPM Enumerations](opm-enumerations.md)
</dt> </dl>

 

 
