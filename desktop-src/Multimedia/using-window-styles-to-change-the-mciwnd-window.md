---
title: Using Window Styles to Change the MCIWnd Window
description: Using Window Styles to Change the MCIWnd Window
ms.assetid: '85851c37-e3d3-45f8-9c0a-0e1392c414af'
keywords: ["MCIWndCreate function"]
---

# Using Window Styles to Change the MCIWnd Window

As with any window, you can change the appearance and behavior of an MCIWnd window by choosing from the standard window styles specified with the [CreateWindow](http://go.microsoft.com/fwlink/p/?linkid=17095) function. In addition, you can choose from several other window styles that are specific to MCIWnd windows. With these styles, your application can change these MCIWnd windows in the following ways:

-   Change window size.
-   Hide or display controls.
-   Issue notification messages.
-   Display information in the title bar.

You can set window styles by specifying them in the [**MCIWndCreate**](mciwndcreate.md) function, or you can use the [**MCIWndChangeStyles**](mciwndchangestyles.md) macro to change the style of an existing MCIWnd window. You can also query an MCIWnd window for its current styles by using the [**MCIWndGetStyles**](mciwndgetstyles.md) macro.

For a list of the MCIWnd-specific window styles, see [**MCIWndCreate**](mciwndcreate.md).

 

 




