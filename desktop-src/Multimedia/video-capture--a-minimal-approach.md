---
title: Video Capture A Minimal Approach
description: Video Capture A Minimal Approach
ms.assetid: e39ff590-69c0-4927-90c2-786c6082068f
keywords:
- Video for Windows (VFW),video capture
- VFW (Video for Windows),video capture
ms.topic: article
ms.date: 05/31/2018
---

# Video Capture: A Minimal Approach

Video capture digitizes a stream of video and audio data, and stores it on a hard disk or some other type of persistent storage device. This section describes how to add a simple form of video capture to an application using three statements of code. It also describes how to end or abort a capture session by sending messages to the capture window.

An AVICap capture window handles the details of streaming audio and video capture to AVI files. This frees your application from involvement in the AVI file format, video and audio buffer management, and the low-level access of video and audio device drivers. AVICap provides a flexible interface for applications. You can add video capture to your application, using only the following lines of code:


```C++
hWndC = capCreateCaptureWindow ( "My Own Capture Window", 
    WS_CHILD | WS_VISIBLE , 0, 0, 160, 120, hwndParent, nID);

SendMessage (hWndC, WM_CAP_DRIVER_CONNECT, 0 /* wIndex */, 0L);

SendMessage (hWndC, WM_CAP_SEQUENCE, 0, 0L);
 
```



A macro interface is also available that provides an alternative to using the [SendMessage](/windows/win32/api/winuser/nf-winuser-sendmessage) function and improves the readability of an application. The following example uses the macro interface to add video capture to an application.


```C++
hWndC = capCreateCaptureWindow (   "My Own Capture Window", 
    WS_CHILD | WS_VISIBLE ,   0, 0, 160, 120, hwndParent, nID);

capDriverConnect (hWndC, 0);

capCaptureSequence (hWndC); 
 
```



After your application creates a capture window of the AVICap window class and connects it to a video driver, the capture window is ready to capture data. At this point, your application can simply send the [**WM\_CAP\_SEQUENCE**](wm-cap-sequence.md) message (or the [**capCaptureSequence**](/windows/desktop/api/Vfw/nf-vfw-capcapturesequence) macro) to begin capturing.

Using default settings, WM\_CAP\_SEQUENCE initiates the capture of video and audio input to a file named CAPTURE.AVI. Capture continues until one of the following events occurs:

-   The user presses the ESC key or a mouse button.
-   Your application stops or aborts capture operation.
-   The disk becomes full.

In an application, you can stop streaming captured data to a file by sending the [**WM\_CAP\_STOP**](wm-cap-stop.md) (or the [**capCaptureStop**](/windows/desktop/api/Vfw/nf-vfw-capcapturestop) macro) message to a capture window. You can also abort the capture operation by sending the [**WM\_CAP\_ABORT**](wm-cap-abort.md) message (or the [**capCaptureAbort**](/windows/desktop/api/Vfw/nf-vfw-capcaptureabort) macro) to a capture window.

 

 