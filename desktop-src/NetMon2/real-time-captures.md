---
Description: 'Monitors receive captured network frames in real-time mode. The frames are captured by a network packet provider (NPP) using the provider's IRTC COM interface, and passed on to the monitor in one of the monitor's two execution threads.'
ms.assetid: '50aa9da2-3a8a-4514-9b1b-9c8364d074d0'
title: 'Real-Time Captures'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Real-Time Captures

Monitors receive captured network frames in real-time mode. The frames are captured by a [*network packet provider*](https://www.bing.com/search?q=*network packet provider*) (NPP) using the provider's [IRTC](irtc.md) COM interface, and passed on to the monitor in one of the monitor's two execution threads.

Monitors can limit the number of frames they have to process by passing a [*capture filter*](https://www.bing.com/search?q=*capture filter*) to the NPP that is supplying the frames. Typically, a specific monitor is designed to watch for specific types of traffic, such as HTTP, RIPX, or SMB. Unlike experts, which use sophisticated parsers to select the information to be analyzed, a monitor must examine each frame for the conditions it was designed to detect. The reason behind this frame-by-frame approach is performance. A monitor must process its frames quickly enough so that it does not fall behind the driver supplying the frames to the NPP. Otherwise, data will be lost.

 

 



