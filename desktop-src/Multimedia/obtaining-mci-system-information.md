---
title: Obtaining MCI System Information
description: Obtaining MCI System Information
ms.assetid: 06175d6e-6d09-4c95-93e9-03af870a2d3f
keywords:
- MCI_SYSINFO command
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining MCI System Information

The [sysinfo](sysinfo.md) ([**MCI\_SYSINFO**](mci-sysinfo.md)) command obtains system information about MCI devices. MCI handles this command without relaying it to any MCI device. For the command-message interface, MCI returns the system information in the [**MCI\_SYSINFO\_PARMS**](mci-sysinfo-parms.md) structure.

You can use the **sysinfo** (MCI\_SYSINFO) command to retrieve information such as the number of MCI devices on a system, the number of MCI devices of a particular type, the number of open MCI devices, and the names of the devices. This command is often called more than once to retrieve a particular piece of information. For example, you might retrieve the number of devices of a particular type in the first call and then enumerate the names of the devices in the next.

 

 




