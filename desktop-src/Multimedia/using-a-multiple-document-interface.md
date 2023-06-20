---
title: Using a Multiple Document Interface
description: Using a Multiple Document Interface
ms.assetid: bc59f19c-1064-4df8-8864-38e6d188f92f
keywords:
- MCIWndRegisterClass function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using a Multiple Document Interface

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Applications that use a multiple document interface (MDI) might need to specify window styles that are not available through the [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) function. For these applications, you can register and create an MCIWnd window by using the [**MCIWndRegisterClass**](/windows/desktop/api/Vfw/nf-vfw-mciwndregisterclass) function with the [CreateWindowEx](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. The **MCIWndRegisterClass** function registers the MCIWND\_WINDOW\_CLASS window class and then **CreateWindowEx** creates an instance of an MCIWnd window.

 

 