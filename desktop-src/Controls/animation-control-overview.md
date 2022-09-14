---
title: About Animation Controls
description: An animation control is a window that displays an Audio-Video Interleaved (AVI) clip. An AVI clip is a series of bitmap frames like a movie. Animation controls can only display AVI clips that do not contain audio.
ms.assetid: 6be69d1a-5b2c-41d5-b6d7-e86ddac2cb0d
ms.topic: article
ms.date: 05/31/2018
---

# About Animation Controls

An *animation control* is a window that displays an Audio-Video Interleaved (AVI) clip. An AVI clip is a series of bitmap frames like a movie. Animation controls can only display AVI clips that do not contain audio.

One common use for an animation control is to indicate system activity during a lengthy operation. This is possible because the operation thread continues executing while the AVI clip is displayed. For example, the Find dialog box of Windows Explorer displays a moving magnifying glass as the system searches for a file.

> [!Note]  
> If you are using ComCtl32.dll version 6 the thread is not supported; make sure that your application does not block the UI, or else the animation will not occur.

 

An animation control can display an AVI clip originating from either an uncompressed AVI file or from an AVI file that was compressed using run-length (BI\_RLE8) encoding. You can add the AVI clip to your application as an AVI resource, or the clip can accompany your application as a separate AVI file.

> [!Note]  
> The AVI file, or resource, must not have a sound channel. The capabilities of the animation control are very limited and are subject to change. If you need a control to provide multimedia playback and recording capabilities for your application, you can use the MCIWnd control. For more information, see [MCIWnd Window Class](/windows/desktop/Multimedia/mciwnd-window-class).

 

This section discusses the following topics.

-   [Animation Control Creation](#animation-control-creation)
-   [About Animation Control Messages](#about-animation-control-messages)
-   [Default Message Processing](#default-message-processing)

## Animation Control Creation

An animation control belongs to the [**ANIMATE\_CLASS**](common-control-window-classes.md) window class. You create an animation control by using the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function or the [**Animate\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-animate_create) macro. The macro positions the animation control in the upper-left corner of the parent window and, if the [**ACS\_CENTER**](animation-control-styles.md) style is not specified, sets the width and height of the control based on the dimensions of a frame in the AVI clip. If **ACS\_CENTER** is specified, **Animate\_Create** sets the width and height of the control to zero. You can use the [**SetWindowPos**](/windows/desktop/api/winuser/nf-winuser-setwindowpos) function to set the position and size of the control.

If you create an animation control within a dialog box or from a dialog box resource, the control is automatically destroyed when the user closes the dialog box. If you create an animation control within a window, you must explicitly destroy the control.

## About Animation Control Messages

An application sends messages to an animation control to open, play, stop, and close the corresponding AVI clip. Each message has one or more macros that you can use instead of sending the message explicitly.

After creating an animation control, an application sends the [**ACM\_OPEN**](acm-open.md) message to open an AVI clip and load it into memory. The message specifies either the path of an AVI file or the name of an AVI resource. The system loads the AVI resource from the module that created the animation control.

If the animation control has the [**ACS\_AUTOPLAY**](animation-control-styles.md) style, the control begins playing the AVI clip immediately after the AVI file or AVI resource is opened. Otherwise, an application can use the [**ACM\_PLAY**](acm-play.md) message to start the AVI clip. An application can stop the clip at any time by sending the [**ACM\_STOP**](acm-stop.md) message. The last frame played remains displayed when the control finishes playing the AVI clip or when **ACM\_STOP** is sent.

An animation control can send two notification codes to its parent window: [ACN\_START](acn-start.md) and [ACN\_STOP](acn-stop.md). Most applications do not handle either notification.

To close the AVI file or AVI resource and remove it from memory, an application can use the [**Animate\_Close**](/windows/desktop/api/Commctrl/nf-commctrl-animate_close) macro, which sends [**ACM\_OPEN**](acm-open.md) with the file name or resource name set to **NULL**.

## Default Message Processing

This section describes the window messages handled by the window procedure for the [**ANIMATE\_CLASS**](common-control-window-classes.md) window class.



| Message                                    | Processing performed                                                                                                                                                                                                                                                                        |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CLOSE**](/windows/desktop/winmsg/wm-close)           | Frees the AVI file or AVI resource associated with the animation control.                                                                                                                                                                                                                   |
| [**WM\_DESTROY**](/windows/desktop/winmsg/wm-destroy)       | Frees the AVI file or AVI resource, frees an internal data structure, and then calls the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function.                                                                                                                                                |
| [**WM\_ERASEBKGND**](/windows/desktop/winmsg/wm-erasebkgnd) | Erases the window background using the current background color for static controls.                                                                                                                                                                                                        |
| [**WM\_NCCREATE**](/windows/desktop/winmsg/wm-nccreate)     | Allocates and initializes an internal data structure and then calls [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca).                                                                                                                                                                              |
| [**WM\_NCHITTEST**](/windows/desktop/inputdev/wm-nchittest) | Returns the HTTRANSPARENT hit test value.                                                                                                                                                                                                                                                   |
| [**WM\_PAINT**](/windows/desktop/gdi/wm-paint)              | Draws an AVI frame in the animation control.                                                                                                                                                                                                                                                |
| [**WM\_SIZE**](/windows/desktop/winmsg/wm-size)             | Checks if the control has the [**ACS\_CENTER**](animation-control-styles.md) style. If the control does not, it calls [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca). Otherwise, it centers the animation in the control, invalidates the control, and then calls **DefWindowProc**. |



 

 

 