---
description: The PHONEBUTTONMODE\_ bit-flag constants describe the button classes.
ms.assetid: 7bf337ee-acda-42fe-b50b-370aad50dc03
title: PHONEBUTTONMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONEBUTTONMODE\_ Constants

The **PHONEBUTTONMODE\_** bit-flag constants describe the button classes.

<dl> <dt>

<span id="PHONEBUTTONMODE_CALL"></span><span id="phonebuttonmode_call"></span>**PHONEBUTTONMODE\_CALL**
</dt> <dd> <dl> <dt>



The button is assigned to a call appearance.


</dt> </dl> </dd> <dt>

<span id="PHONEBUTTONMODE_DISPLAY"></span><span id="phonebuttonmode_display"></span>**PHONEBUTTONMODE\_DISPLAY**
</dt> <dd> <dl> <dt>



The button is a "soft" button associated with the phone's display. A phone set can have zero or more display buttons.


</dt> </dl> </dd> <dt>

<span id="PHONEBUTTONMODE_DUMMY"></span><span id="phonebuttonmode_dummy"></span>**PHONEBUTTONMODE\_DUMMY**
</dt> <dd> <dl> <dt>



This value is used to describe a button/lamp position that has no corresponding button but has only a lamp.


</dt> </dl> </dd> <dt>

<span id="PHONEBUTTONMODE_FEATURE"></span><span id="phonebuttonmode_feature"></span>**PHONEBUTTONMODE\_FEATURE**
</dt> <dd> <dl> <dt>



The button is assigned to requesting features from the switch, such as hold, conference, and transfer.


</dt> </dl> </dd> <dt>

<span id="PHONEBUTTONMODE_KEYPAD"></span><span id="phonebuttonmode_keypad"></span>**PHONEBUTTONMODE\_KEYPAD**
</dt> <dd> <dl> <dt>



The button is one of the twelve keypad buttons, 0 through 9, '\*', and '\#'.


</dt> </dl> </dd> <dt>

<span id="PHONEBUTTONMODE_LOCAL"></span><span id="phonebuttonmode_local"></span>**PHONEBUTTONMODE\_LOCAL**
</dt> <dd> <dl> <dt>



The button is a local function button, such as mute or volume control.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

This enumeration type is used in the [**PHONECAPS**](/windows/desktop/api/Tapi/ns-tapi-phonecaps) data structure to describe the meaning associated with the phone's buttons.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




