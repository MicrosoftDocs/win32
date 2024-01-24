---
description: A child window is a window with the WS\_CHILD or WS\_CHILDWINDOW style.
ms.assetid: d8110492-c1b9-4b49-9b34-587adb7c65c9
title: Child Window Update Region
ms.topic: article
ms.date: 05/31/2018
---

# Child Window Update Region

A child window is a window with the WS\_CHILD or WS\_CHILDWINDOW style. Like other window styles, child windows receive [**WM\_PAINT**](wm-paint.md) messages to prompt updating. Each child window has an update region, which either the system or the application can set to generate eventual **WM\_PAINT** messages.

A child window's update and visible regions are affected by the child's parent window; this is not true for windows of other styles. The system often sets the child window's update region when it sets the parent window's update region, causing the child window to receive [**WM\_PAINT**](wm-paint.md) messages when the parent window receives them. The system limits the location of the child window's visible region to within the client area of the parent window and clips any portion of the child window moved outside the parent window.

The system sets the update region for a child window whenever part of the parent window's update region includes a portion of the child window. In such cases, the system first sends a [**WM\_PAINT**](wm-paint.md) message to the parent window and then sends a message to the child window, allowing the child to restore any portions of the window that the parent may have drawn over.

The system does not set the parent's update region when the child's is set. An application cannot generate a [**WM\_PAINT**](wm-paint.md) message for the parent window by invalidating the child window. Similarly, an application cannot generate a **WM\_PAINT** message for the child by invalidating a portion of the parent's client area that lies entirely under the child window. In such cases, neither window receives a **WM\_PAINT** message.

An application can prevent a child window's update region from being set when the parent window's is set by specifying the WS\_CLIPCHILDREN style when creating the parent window. When this style is set, the system excludes the child windows from the parent's visible region and therefore ignores any portion of the update region that may contain the child windows. When the application paints in the parent window, any drawing that would cover the child window is clipped, making a subsequent [**WM\_PAINT**](wm-paint.md) message to the child window unnecessary.

The update and visible regions of a child window are also affected by the child window's siblings. Sibling windows are any windows that have a common parent window. If sibling windows overlap, then setting the update region for one affects the update region of another, causing [**WM\_PAINT**](wm-paint.md) messages to be sent to both windows. If a window in the parent chain is composited (a window with WX\_EX\_COMPOSITED), sibling windows receive **WM\_PAINT** messages in the reverse order of their position in the Z order. Given this, the window highest in the Z order (on the top) receives its **WM\_PAINT** message last, and vice versa. If a window in the parent chain is not composited, sibling windows receive **WM\_PAINT** messages in Z order.

Sibling windows are not automatically clipped. One sibling can draw over another overlapping sibling even if the window that is drawing has a lower position in the Z order. An application can prevent this by specifying the WS\_CLIPSIBLINGS style when creating the windows. When this style is set, the system excludes all portions of an overlapping sibling window from a window's visible region if the overlapping sibling window has a higher position in the Z order.

> [!Note]  
> The update and visible regions for windows that have the WS\_POPUP or WS\_POPUPWINDOW style are not affected by their parent windows.

 

 

 



