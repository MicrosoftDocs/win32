---
description: The PHONEHOOKSWITCHDEV\_ bit-flag constants describe various audio I/O devices each with its own hookswitch controllable from the computer.
ms.assetid: b3272a75-87b0-4afc-b2e2-2d65e4b49300
title: PHONEHOOKSWITCHDEV_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONEHOOKSWITCHDEV\_ Constants

The **PHONEHOOKSWITCHDEV\_** bit-flag constants describe various audio I/O devices each with its own hookswitch controllable from the computer.

<dl> <dt>

<span id="PHONEHOOKSWITCHDEV_HANDSET"></span><span id="phonehookswitchdev_handset"></span>**PHONEHOOKSWITCHDEV\_HANDSET**
</dt> <dd> <dl> <dt>



This is a standard ear- and mouthpiece phone.


</dt> </dl> </dd> <dt>

<span id="PHONEHOOKSWITCHDEV_HEADSET"></span><span id="phonehookswitchdev_headset"></span>**PHONEHOOKSWITCHDEV\_HEADSET**
</dt> <dd> <dl> <dt>



This is a headset connected to the phone set.


</dt> </dl> </dd> <dt>

<span id="PHONEHOOKSWITCHDEV_SPEAKER"></span><span id="phonehookswitchdev_speaker"></span>**PHONEHOOKSWITCHDEV\_SPEAKER**
</dt> <dd> <dl> <dt>



This is a built-in loudspeaker and microphone. This could also be an externally connected adjunct speaker to the telephone set.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

These constants are used in the [**PHONECAPS**](/windows/desktop/api/Tapi/ns-tapi-phonecaps) data structure to indicate the hookswitch device capabilities of a phone device. The [**PHONESTATUS**](/windows/desktop/api/Tapi/ns-tapi-phonestatus) structure reports the state of the phone's hookswitch devices. The function [**phoneSetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonesethookswitch) and [**phoneGetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonegethookswitch) use it as a parameter to select the phone's I/O device.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




