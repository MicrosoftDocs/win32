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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying Auxiliary Audio Devices

Not all multimedia systems have auxiliary audio support. You can use the [**auxGetNumDevs**](https://www.bing.com/search?q=**auxGetNumDevs**) function to determine the number of controllable auxiliary devices present in a system.

To get information about a particular auxiliary audio device, use the [**auxGetDevCaps**](https://www.bing.com/search?q=**auxGetDevCaps**) function. This function fills an [**AUXCAPS**](https://www.bing.com/search?q=**AUXCAPS**) structure with information about the capabilities of a specified device. This information includes the manufacturer and product identifiers, a product name for the device, and the device-driver version number.

 

 




