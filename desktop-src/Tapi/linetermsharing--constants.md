---
description: The LINETERMSHARING\_ bit-flag constants describe different ways in which a terminal can be shared between line devices, addresses, or calls.
ms.assetid: 50a52a50-4d94-4068-9ea4-bea862400036
title: LINETERMSHARING_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINETERMSHARING\_ Constants

The **LINETERMSHARING\_** bit-flag constants describe different ways in which a terminal can be shared between line devices, addresses, or calls.

<dl> <dt>

<span id="LINETERMSHARING_PRIVATE"></span><span id="linetermsharing_private"></span>**LINETERMSHARING\_PRIVATE**
</dt> <dd> <dl> <dt>



The terminal device is private to a single line device.


</dt> </dl> </dd> <dt>

<span id="LINETERMSHARING_SHAREDCONF"></span><span id="linetermsharing_sharedconf"></span>**LINETERMSHARING\_SHAREDCONF**
</dt> <dd> <dl> <dt>



The terminal device can be used by multiple lines. The [**lineSetTerminal**](/windows/desktop/api/Tapi/nf-tapi-linesetterminal) requests of the various terminals end up being merged or conferenced at the terminal.


</dt> </dl> </dd> <dt>

<span id="LINETERMSHARING_SHAREDEXCL"></span><span id="linetermsharing_sharedexcl"></span>**LINETERMSHARING\_SHAREDEXCL**
</dt> <dd> <dl> <dt>



The terminal device can be used by multiple lines. The last line device to do a [**lineSetTerminal**](/windows/desktop/api/Tapi/nf-tapi-linesetterminal) or [**TSPI\_lineSetTerminal**](/windows/win32/api/tspi/nf-tspi-tspi_linesetterminal) to the terminal for a given terminal mode will have exclusive connection to the terminal for that mode.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

These constants describe the classes of control and information streams that can be routed directly between a line device and a terminal device (such as a phone set).

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

