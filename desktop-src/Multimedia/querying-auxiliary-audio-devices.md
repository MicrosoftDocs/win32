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
ms.date: 05/31/2018
---

# Querying Auxiliary Audio Devices

Not all multimedia systems have auxiliary audio support. You can use the [**auxGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-auxgetnumdevs) function to determine the number of controllable auxiliary devices present in a system.

To get information about a particular auxiliary audio device, use the [**auxGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-auxgetdevcaps) function. This function fills an [**AUXCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-auxcaps) structure with information about the capabilities of a specified device. This information includes the manufacturer and product identifiers, a product name for the device, and the device-driver version number.

 

 