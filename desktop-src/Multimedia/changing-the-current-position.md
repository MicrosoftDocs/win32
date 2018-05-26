---
title: Changing the Current Position
description: Changing the Current Position
ms.assetid: f8c4b9b5-c5fb-4292-8418-41650dcd65c0
keywords:
- MCI_SEEK command message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Changing the Current Position

To change the current position in a device element, use the [**MCI\_SEEK**](mci-seek.md) command message along with the MCI\_TO flag and the [**MCI\_SEEK\_PARMS**](mci-seek-parms.md) structure. If you use the **dwTo** member to specify a seek position with MCI\_SEEK, you should query the time format and set it, if necessary.

In addition to specifying a position with the **dwTo** member, you can specify the MCI\_SEEK\_TO\_START or MCI\_SEEK\_TO\_END flags for the *dwParam1* parameter of the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function to find the starting and ending positions of the device element. If you use one of these flags, don't specify the MCI\_TO flag.

 

 




