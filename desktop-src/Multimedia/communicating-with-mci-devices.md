---
title: Communicating with MCI Devices
description: Communicating with MCI Devices
ms.assetid: 2408f8e4-d040-40f5-a880-1ecb8025656c
keywords:
- MCIWndSendString macro
- mciSendString function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Communicating with MCI Devices

The driver of each MCI device maintains a list of its current settings and capabilities, so it can issue an accurate response when it is queried for information.

When you want to communicate with an MCI device, you can use MCIWnd macros and functions. Many of the most common MCI commands and queries are defined as macros. However, if the task you want to perform is unavailable as a function or macro, you can send MCI commands directly to the device driver by using the [**MCIWndSendString**](/windows/win32/Vfw/nf-vfw-mciwndsendstring?branch=master) macro or by using either the message form or string form of the MCI commands. Using the **MCIWndSendString** macro is equivalent to using the [**mciSendString**](/windows/win32/Mmsystem/?branch=master) function as follows:


```C++
mciSendString(sz, Null, 0, Null) 
```



The parameters of [**MCIWndSendString**](/windows/win32/Vfw/nf-vfw-mciwndsendstring?branch=master) include only the window handle and the string form of the command. To retrieve the information returned by a string command, use the [**MCIWndReturnString**](/windows/win32/Vfw/nf-vfw-mciwndreturnstring?branch=master) macro.

For more information about MCI, see [MCI](mci.md).

> [!Note]  
> You must exclude the device alias from the MCI command when you use **MCIWndSendString**. The MCIWnd library adds this alias when it sends the command to the MCI device.

 

 

 




