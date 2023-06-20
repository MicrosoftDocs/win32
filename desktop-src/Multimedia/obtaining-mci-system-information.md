---
title: Obtaining MCI System Information
description: Obtaining MCI System Information
ms.assetid: 06175d6e-6d09-4c95-93e9-03af870a2d3f
keywords:
- MCI_SYSINFO command
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Obtaining MCI System Information

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [sysinfo](sysinfo.md) ([**MCI\_SYSINFO**](mci-sysinfo.md)) command obtains system information about MCI devices. MCI handles this command without relaying it to any MCI device. For the command-message interface, MCI returns the system information in the [**MCI\_SYSINFO\_PARMS**](mci-sysinfo-parms.md) structure.

You can use the **sysinfo** (MCI\_SYSINFO) command to retrieve information such as the number of MCI devices on a system, the number of MCI devices of a particular type, the number of open MCI devices, and the names of the devices. This command is often called more than once to retrieve a particular piece of information. For example, you might retrieve the number of devices of a particular type in the first call and then enumerate the names of the devices in the next.

 

 




