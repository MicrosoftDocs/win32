---
title: Communicating with MCI Devices
description: Communicating with MCI Devices
ms.assetid: '2408f8e4-d040-40f5-a880-1ecb8025656c'
keywords: ["MCIWndSendString macro", "mciSendString function"]
---

# Communicating with MCI Devices

The driver of each MCI device maintains a list of its current settings and capabilities, so it can issue an accurate response when it is queried for information.

When you want to communicate with an MCI device, you can use MCIWnd macros and functions. Many of the most common MCI commands and queries are defined as macros. However, if the task you want to perform is unavailable as a function or macro, you can send MCI commands directly to the device driver by using the [**MCIWndSendString**](mciwndsendstring.md) macro or by using either the message form or string form of the MCI commands. Using the **MCIWndSendString** macro is equivalent to using the [**mciSendString**](mcisendstring.md) function as follows:


```C++
mciSendString(sz, Null, 0, Null) 
```



The parameters of [**MCIWndSendString**](mciwndsendstring.md) include only the window handle and the string form of the command. To retrieve the information returned by a string command, use the [**MCIWndReturnString**](mciwndreturnstring.md) macro.

For more information about MCI, see [MCI](mci.md).

> [!Note]  
> You must exclude the device alias from the MCI command when you use **MCIWndSendString**. The MCIWnd library adds this alias when it sends the command to the MCI device.

 

 

 




