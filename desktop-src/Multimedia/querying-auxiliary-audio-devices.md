---
title: Querying Auxiliary Audio Devices
description: Querying Auxiliary Audio Devices
ms.assetid: 9fc0b17f-cc93-4eab-bcb3-09f2332b352f
keywords:
- waveform audio,querying auxiliary audio devices
- auxiliary audio,querying devices
- auxiliary audio interface
- auxiliary audio devices,querying
- querying auxiliary audio devices
- auxiliary audio,interface
- auxiliary audio,devices
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Querying Auxiliary Audio Devices

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Not all multimedia systems have auxiliary audio support. You can use the [**auxGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-auxgetnumdevs) function to determine the number of controllable auxiliary devices present in a system.

To get information about a particular auxiliary audio device, use the [**auxGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-auxgetdevcaps) function. This function fills an [**AUXCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-auxcaps) structure with information about the capabilities of a specified device. This information includes the manufacturer and product identifiers, a product name for the device, and the device-driver version number.

 

 