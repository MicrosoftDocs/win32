---
description: 'An application draws in a window at a variety of times: when first creating a window, when changing the size of the window, when moving the window from behind another window, when minimizing or maximizing the window, when displaying data from an opened file, and when scrolling, changing, or selecting a portion of the displayed data.'
ms.assetid: 4b5d6842-5707-4884-a55a-e09e342cea46
title: When to Draw in a Window
ms.topic: article
ms.date: 05/31/2018
---

# When to Draw in a Window

An application draws in a window at a variety of times: when first creating a window, when changing the size of the window, when moving the window from behind another window, when minimizing or maximizing the window, when displaying data from an opened file, and when scrolling, changing, or selecting a portion of the displayed data.

The system manages actions such as moving and sizing a window. If an action affects the content of the window, the system marks the affected portion of the window as ready for updating and, at the next opportunity, sends a [**WM\_PAINT**](wm-paint.md) message to the window procedure of the window. The message is a signal to the application to determine what must be updated and to carry out the necessary drawing.

Some actions are managed by the application, such as displaying open files and selecting displayed data. For these actions, an application can mark for updating the portion of the window affected by the action, causing a [**WM\_PAINT**](wm-paint.md) message to be sent at the next opportunity. If an action requires immediate feedback, the application can draw while the action takes place, without waiting for **WM\_PAINT**. For example, a typical application highlights the area the user selects rather than waiting for the next **WM\_PAINT** message to update the area.

In all cases, an application can draw in a window as soon as it is created. To draw in the window, the application must first retrieve a handle to a display device context for the window. Ideally, an application carries out most of its drawing operations during the processing of [**WM\_PAINT**](wm-paint.md) messages. In this case, the application retrieves a display device context by calling the [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) function. If an application draws at any other time, such as from within [**WinMain**](/windows/win32/api/winbase/nf-winbase-winmain) or during the processing of keyboard or mouse messages, it calls the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) or [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) function to retrieve the display DC.

 

 
