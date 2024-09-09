---
title: Communicating with MCI Devices
description: Communicating with MCI Devices
ms.assetid: 2408f8e4-d040-40f5-a880-1ecb8025656c
keywords:
- MCIWndSendString macro
- mciSendString function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Communicating with MCI Devices

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The driver of each MCI device maintains a list of its current settings and capabilities, so it can issue an accurate response when it is queried for information.

When you want to communicate with an MCI device, you can use MCIWnd macros and functions. Many of the most common MCI commands and queries are defined as macros. However, if the task you want to perform is unavailable as a function or macro, you can send MCI commands directly to the device driver by using the [**MCIWndSendString**](/windows/desktop/api/Vfw/nf-vfw-mciwndsendstring) macro or by using either the message form or string form of the MCI commands. Using the **MCIWndSendString** macro is equivalent to using the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function as follows:


```C++
mciSendString(sz, Null, 0, Null) 
```



The parameters of [**MCIWndSendString**](/windows/desktop/api/Vfw/nf-vfw-mciwndsendstring) include only the window handle and the string form of the command. To retrieve the information returned by a string command, use the [**MCIWndReturnString**](/windows/desktop/api/Vfw/nf-vfw-mciwndreturnstring) macro.

For more information about MCI, see [MCI](mci.md).

> [!Note]  
> You must exclude the device alias from the MCI command when you use **MCIWndSendString**. The MCIWnd library adds this alias when it sends the command to the MCI device.

 

 

 