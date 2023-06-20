---
title: Closing a Device
description: Closing a Device
ms.assetid: eef40f23-2c58-4deb-a6f0-3563d9c30d10
keywords:
- MCI_CLOSE command
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Closing a Device

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**close**](close.md) ([**MCI\_CLOSE**](mci-close.md)) command releases access to a device or file. MCI frees a device when all tasks using a device have closed it. To help MCI manage the devices, your application must close each device or file when it is finished using it.

When you close an external MCI device that uses its own media instead of files (such as CD audio), the driver leaves the device in its current mode of operation. Thus, if you close a CD audio device that is playing, even though the device driver is released from memory, the CD audio device will continue to play until it reaches the end of its content.

> [!Note]  
> Closing an application with open MCI devices can prevent other applications from using those devices until Windows is restarted.

 

 

 




