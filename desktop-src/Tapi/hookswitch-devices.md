---
description: A phone device can have multiple hookswitch devices.
ms.assetid: 39e3f24d-55d8-4830-8599-383954c8a107
title: Hookswitch Devices
ms.topic: article
ms.date: 05/31/2018
---

# Hookswitch Devices

A phone device can have multiple hookswitch devices. A hookswitch is the switch that connects or disconnects a device from the phone line. On a telephone, for example, this is the switch that is automatically activated when a user lifts the receiver from the cradle to get a new dial tone. TAPI defines three types of hookswitch devices for a phone: handset, speakerphone, and headset. Each hookswitch device has a speaker and a microphone component, and operates in one of four hookswitch modes:

-   **Onhook** The hookswitch device is onhook, and both its microphone and speaker are disabled.
-   **Microphone only** The hookswitch device is offhook, its microphone is enabled, and its speaker is mute.
-   **Speaker only** The hookswitch device is offhook, its microphone is mute, and its speaker is enabled.
-   **Microphone and speaker** The hookswitch device is offhook, and both microphone and speaker are enabled.

The [**phoneSetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonesethookswitch) function is used to set the hookswitch mode of one or more of the hookswitch devices of an open phone device. For example, to mute or unmute the microphone or speaker component of a hookswitch device, use **phoneSetHookSwitch** with the appropriate hookswitch mode. The [**phoneGetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonegethookswitch) function can be used to query the hookswitch mode of a hookswitch device of an open phone device.

When the mode of a phone's hookswitch device is changed manually, for example by lifting the handset from its cradle, a [**PHONE\_STATE**](phone-state.md) message is sent to the application to notify the application about the state change. Parameters to this message provide an indication of the change.

The volume of the speaker component of a hookswitch device can be set with [**phoneSetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonesetvolume). Volume setting is different from mute in that muting a speaker and later unmuting it will preserve the volume setting of the speaker. The [**phoneGetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonegetvolume) function can be used to return the current volume setting of a hookswitch device's speaker of an open phone device.

The microphone component of a hookswitch device can also be gain controlled. Gain setting is different from mute in that muting a microphone and later unmuting it will preserve the gain setting of the microphone. Use [**phoneSetGain**](/windows/desktop/api/Tapi/nf-tapi-phonesetgain) to set the gain of a hookswitch device's microphone of an open phone device, and [**phoneGetGain**](/windows/desktop/api/Tapi/nf-tapi-phonegetgain) to return the gain setting of a hookswitch device's microphone of an opened phone.

When the volume or gain of a phone's hookswitch device is changed, a PHONE\_STATE message is sent to the application function to notify the application about the state change. Parameters to this message provide an indication of the change.

 

 



