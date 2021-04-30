---
description: Phone device support is supplementary rather than basic, so service providers are not required to support phone devices.
ms.assetid: '4d9f3b32-20d0-4550-9b3d-db97df8ea289'
title: Phone Devices
ms.topic: article
ms.date: 05/31/2018
---

# Phone Devices

Phone device support is supplementary rather than basic, so service providers are not required to support phone devices.

Just as a line device class is an abstraction of a physical line device, the phone device class represents a device-independent abstraction of a telephone set. TAPI treats line and phone devices as devices that are independent of each other. In other words, you can use a phone (device) without using an associated line, and you can use a line (device) without using a phone.

Service providers that fully implement this independence can offer uses for these devices not defined by traditional telephony protocols. For example, a person can use the handset of the desktop's phone as a waveform audio device for voice recording or playback, perhaps without the switch's knowledge that the phone is in use. In such an implementation, lifting the local phone handset need not automatically send an offhook signal to the switch.

This independence also allows an application to ring the local telephone in a manner that is independent of incoming calls. The capabilities of service providers are limited by the capabilities of the hardware and software used to interconnect the switch, the phone, and the computer.

TAPI includes functions to retrieve device capabilities that allow clients to determine whether such a usage model is supported.

This section describes phone devices and explains how to use the TAPI phone functions to access these devices.

-   [Phone Device](phone-device-elements.md)
-   [Initialization and Shutdown](initialization-and-shutdown.md)

 

 



