---
description: The LINETERMMODE\_ bit-flag constants describe different types of events on a phone line that can be routed to a terminal device.
ms.assetid: 60af1687-8958-4918-be21-a13780c60974
title: LINETERMMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINETERMMODE\_ Constants

The **LINETERMMODE\_** bit-flag constants describe different types of events on a phone line that can be routed to a terminal device.

<dl> <dt>

<span id="LINETERMMODE_BUTTONS"></span><span id="linetermmode_buttons"></span>**LINETERMMODE\_BUTTONS**
</dt> <dd> <dl> <dt>



These are button-press events sent from the terminal to the line.


</dt> </dl> </dd> <dt>

<span id="LINETERMMODE_DISPLAY"></span><span id="linetermmode_display"></span>**LINETERMMODE\_DISPLAY**
</dt> <dd> <dl> <dt>



This is display information sent from the line to the terminal.


</dt> </dl> </dd> <dt>

<span id="LINETERMMODE_HOOKSWITCH"></span><span id="linetermmode_hookswitch"></span>**LINETERMMODE\_HOOKSWITCH**
</dt> <dd> <dl> <dt>



These are hookswitch events sent from the terminal to the line.


</dt> </dl> </dd> <dt>

<span id="LINETERMMODE_LAMPS"></span><span id="linetermmode_lamps"></span>**LINETERMMODE\_LAMPS**
</dt> <dd> <dl> <dt>



These are lamp events sent from the line to the terminal.


</dt> </dl> </dd> <dt>

<span id="LINETERMMODE_MEDIABIDIRECT"></span><span id="linetermmode_mediabidirect"></span>**LINETERMMODE\_MEDIABIDIRECT**
</dt> <dd> <dl> <dt>



This is the bidirectional media stream associated with a call on the line and the terminal. Use this value when the routing of both unidirectional channels of a call's media stream cannot be controlled independently.


</dt> </dl> </dd> <dt>

<span id="LINETERMMODE_MEDIAFROMLINE"></span><span id="linetermmode_mediafromline"></span>**LINETERMMODE\_MEDIAFROMLINE**
</dt> <dd> <dl> <dt>



This is the unidirectional media stream from the line to the terminal associated with a call on the line. Use this value when the routing of both unidirectional channels of a call's media stream can be controlled independently.


</dt> </dl> </dd> <dt>

<span id="LINETERMMODE_MEDIATOLINE"></span><span id="linetermmode_mediatoline"></span>**LINETERMMODE\_MEDIATOLINE**
</dt> <dd> <dl> <dt>



This is the unidirectional media stream from the terminal to the line associated with a call on the line. Use this value when the routing of both unidirectional channels of a call's media stream can be controlled independently.


</dt> </dl> </dd> <dt>

<span id="LINETERMMODE_RINGER"></span><span id="linetermmode_ringer"></span>**LINETERMMODE\_RINGER**
</dt> <dd> <dl> <dt>



This is ringer-control information sent from the switch to the terminal.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

These constants describe the classes of control and information streams that can be routed directly between a line device and a terminal device (such as a phone set).

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




