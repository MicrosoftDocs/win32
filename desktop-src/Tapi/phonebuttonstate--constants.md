---
description: The PHONEBUTTONSTATE bit-flag constants describe the buttons positions.
ms.assetid: f1196e31-65c6-4ade-a0b7-c7758ce97be1
title: PHONEBUTTONSTATE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONEBUTTONSTATE_ Constants

The **PHONEBUTTONSTATE_** bit-flag constants describe the button's positions.

<dl> <dt>

<span id="PHONEBUTTONSTATE_DOWN"></span><span id="phonebuttonstate_down"></span>**PHONEBUTTONSTATE_DOWN**
</dt> <dd> <dl> <dt>



The button is in the "down" state (pressed down).


</dt> </dl> </dd> <dt>

<span id="PHONEBUTTONSTATE_UNAVAIL"></span><span id="phonebuttonstate_unavail"></span>**PHONEBUTTONSTATE_UNAVAIL**
</dt> <dd> <dl> <dt>



Indicates that the up or down state of the button is not known to the service provider, and will not become known at a future time. (TAPI versions 1.4 and later)


</dt> </dl> </dd> <dt>

<span id="PHONEBUTTONSTATE_UNKNOWN"></span><span id="phonebuttonstate_unknown"></span>**PHONEBUTTONSTATE_UNKNOWN**
</dt> <dd> <dl> <dt>



Indicates that the up or down state of the button is not known at this time, but may become known at a future time. (TAPI versions 1.4 and later)


</dt> </dl> </dd> <dt>

<span id="PHONEBUTTONSTATE_UP"></span><span id="phonebuttonstate_up"></span>**PHONEBUTTONSTATE_UP**
</dt> <dd> <dl> <dt>



The button is in the "up" state.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

For backward compatibility, it is the responsibility of the service provider to examine the negotiated API version on the phone, and to not use those PHONEBUTTONSTATE_ values that the negotiated version does not support.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




