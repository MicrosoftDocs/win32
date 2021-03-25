---
description: The PHONEPRIVILEGE\_ bit-flag constants describe the various ways in which a phone device can be opened.
ms.assetid: 1dc2fab9-b044-4ae3-8c16-fa450f9ef714
title: PHONEPRIVILEGE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONEPRIVILEGE\_ Constants

The **PHONEPRIVILEGE\_** bit-flag constants describe the various ways in which a phone device can be opened.

<dl> <dt>

<span id="PHONEPRIVILEGE_MONITOR"></span><span id="phoneprivilege_monitor"></span>**PHONEPRIVILEGE\_MONITOR**
</dt> <dd> <dl> <dt>



An application that opens a phone device with the monitor privilege is informed about events and state changes occurring on the phone. The application cannot invoke any operations on the phone device that would change its state, so only status operations can be invoked. Multiple applications can monitor a phone device at any given time.


</dt> </dl> </dd> <dt>

<span id="PHONEPRIVILEGE_OWNER"></span><span id="phoneprivilege_owner"></span>**PHONEPRIVILEGE\_OWNER**
</dt> <dd> <dl> <dt>



An application that opens a phone device with the owner privilege is allowed to change the state of the lamps, ringer, display, hookswitch, and data blocks of the phone. Opening a phone device in owner mode also provides monitoring of the phone device. Only one application is allowed to be the owner of a phone device at any given time.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




