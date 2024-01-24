---
description: The PHONEHOOKSWITCHMODE\_ bit-flag constants describe the microphone and speaker components of a hookswitch device.
ms.assetid: 532bf089-d5ca-4a04-847d-69e48990ff5c
title: PHONEHOOKSWITCHMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONEHOOKSWITCHMODE\_ Constants

The **PHONEHOOKSWITCHMODE\_** bit-flag constants describe the microphone and speaker components of a hookswitch device.

<dl> <dt>

<span id="PHONEHOOKSWITCHMODE_MIC"></span><span id="phonehookswitchmode_mic"></span>**PHONEHOOKSWITCHMODE\_MIC**
</dt> <dd> <dl> <dt>



The device's microphone is active, the speaker is mute.


</dt> </dl> </dd> <dt>

<span id="PHONEHOOKSWITCHMODE_MICSPEAKER"></span><span id="phonehookswitchmode_micspeaker"></span>**PHONEHOOKSWITCHMODE\_MICSPEAKER**
</dt> <dd> <dl> <dt>



The device's microphone and speaker are both active.


</dt> </dl> </dd> <dt>

<span id="PHONEHOOKSWITCHMODE_ONHOOK"></span><span id="phonehookswitchmode_onhook"></span>**PHONEHOOKSWITCHMODE\_ONHOOK**
</dt> <dd> <dl> <dt>



The device's microphone and speaker are both onhook.


</dt> </dl> </dd> <dt>

<span id="PHONEHOOKSWITCHMODE_SPEAKER"></span><span id="phonehookswitchmode_speaker"></span>**PHONEHOOKSWITCHMODE\_SPEAKER**
</dt> <dd> <dl> <dt>



The device's speaker is active, the microphone is mute.


</dt> </dl> </dd> <dt>

<span id="PHONEHOOKSWITCHMODE_UNKNOWN"></span><span id="phonehookswitchmode_unknown"></span>**PHONEHOOKSWITCHMODE\_UNKNOWN**
</dt> <dd> <dl> <dt>



The device's hookswitch mode is currently unknown.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

These constants are used to provide an individual level of control over the microphone and speaker components of a phone device.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




