---
description: Most drawing carried out during processing of the WM\_PAINT message is asynchronous; that is, there is a delay between the time a portion of the window is invalidated and the time WM\_PAINT is sent.
ms.assetid: c4eac615-6526-4ca6-854b-b4a598da13a4
title: Synchronous and Asynchronous Drawing
ms.topic: article
ms.date: 05/31/2018
---

# Synchronous and Asynchronous Drawing

Most drawing carried out during processing of the [**WM\_PAINT**](wm-paint.md) message is asynchronous; that is, there is a delay between the time a portion of the window is invalidated and the time WM\_PAINT is sent. During the delay, the application typically retrieves messages from the queue and carries out other tasks. The reason for the delay is that the system generally treats drawing in a window as a low-priority operation and works as though user-input messages and messages that may affect the position or size of a window will be processed before WM\_PAINT .

In some cases, it is necessary for an application to draw synchronously that is, draw in the window immediately after invalidating a portion of the window. A typical application draws its main window immediately after creating the window to signal the user that the application has started successfully. The system draws some control windows synchronously, such as buttons, because such windows serve as the focus for user input. Although any window with a simple drawing routine can be drawn synchronously, all such drawing should be done quickly and should not interfere with the application's ability to respond to user input.

The [**UpdateWindow**](/windows/desktop/api/Winuser/nf-winuser-updatewindow) and [**RedrawWindow**](/windows/desktop/api/Winuser/nf-winuser-redrawwindow) functions allow for synchronous drawing. **UpdateWindow** sends a [**WM\_PAINT**](wm-paint.md) message directly to the window if the update region is not empty. **RedrawWindow** also sends a **WM\_PAINT** message, but gives the application greater control over how to draw the window, such as whether to draw the nonclient area and window background or whether to send the message regardless of whether the update region is empty. These functions send the **WM\_PAINT** message directly to the window, regardless of the number of other messages in the application message queue.

Any window requiring time-consuming drawing operations should be drawn asynchronously to prevent pending messages from being blocked as the window is drawn. Also, any application that frequently invalidates small portions of a window should allow these invalid portions to consolidate into a single asynchronous [**WM\_PAINT**](wm-paint.md) message, rather than a series of synchronous **WM\_PAINT** messages.

 

 



