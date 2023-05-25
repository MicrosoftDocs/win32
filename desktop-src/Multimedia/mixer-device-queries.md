---
title: Mixer Device Queries
description: Mixer Device Queries
ms.assetid: 3b453802-954b-4356-9ad5-0f8376b6199d
keywords:
- multimedia audio,mixer device queries
- audio,mixer device queries
- audio mixers,device queries
- mixers,device queries
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Mixer Device Queries

\[The feature associated with this page, [Audio Mixers](/windows/win32/multimedia/audio-mixers), is a legacy feature. It has been superseded by [Volume Controls](/windows/win32/coreaudio/volume-controls). **Volume Controls** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Volume Controls** instead of **Audio Mixers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The mixer services provide functions for determining the number of mixer devices present in the system and the capabilities of the devices. You can also use a mixer services function to determine the device identifier for a mixer device.

You can use the [**mixerGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetnumdevs) function to determine how many mixer devices are present in the system. Mixer devices are identified by a device identifier. Device identifiers are determined implicitly from the number of devices present in a given system. They range from zero through one less than the number of devices present.

Before using a mixer device, you must determine its capabilities. Audio capabilities can vary from one multimedia computer to another, so applications need to work with a variety of audio hardware.

You can use the [**mixerGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetdevcaps) function to determine the capabilities of mixer devices. This function fills a [**MIXERCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-mixercaps) structure with information about the capabilities of a specified device.

The [**mixerGetID**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetid) function retrieves the audio mixer device identifier associated with a specified device handle. For example, you could use this function to retrieve the device identifier for an audio mixer and then use the device identifier to adjust the volume or to display another control.

 

 