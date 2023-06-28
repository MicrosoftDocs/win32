---
title: Using Window Styles to Change the MCIWnd Window
description: Using Window Styles to Change the MCIWnd Window
ms.assetid: 85851c37-e3d3-45f8-9c0a-0e1392c414af
keywords:
- MCIWndCreate function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Window Styles to Change the MCIWnd Window

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

As with any window, you can change the appearance and behavior of an MCIWnd window by choosing from the standard window styles specified with the [CreateWindow](/windows/win32/api/winuser/nf-winuser-createwindowa) function. In addition, you can choose from several other window styles that are specific to MCIWnd windows. With these styles, your application can change these MCIWnd windows in the following ways:

-   Change window size.
-   Hide or display controls.
-   Issue notification messages.
-   Display information in the title bar.

You can set window styles by specifying them in the [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) function, or you can use the [**MCIWndChangeStyles**](/windows/desktop/api/Vfw/nf-vfw-mciwndchangestyles) macro to change the style of an existing MCIWnd window. You can also query an MCIWnd window for its current styles by using the [**MCIWndGetStyles**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetstyles) macro.

For a list of the MCIWnd-specific window styles, see [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea).

 

 