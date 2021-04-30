---
description: Using Windowed Mode
ms.assetid: 09ee4568-348b-4cf9-bb38-dada291cdef9
title: Using Windowed Mode
ms.topic: article
ms.date: 05/31/2018
---

# Using Windowed Mode

> [!Note]  
> The legacy [Video Renderer Filter](video-renderer-filter.md) always uses windowed mode. The VMR-7 and VMR-9 filters use windowed mode by default, but also support windowless mode.

 

In windowed mode, the video renderer creates its own window where it paints the video frames. Unless you specify otherwise, this window is a top-level window with its own borders and title bar. Most of the time, however, you will attach the video window to an application window, so that the video is integrated into your application UI. This requires the following steps:

1.  Query for **IVideoWindow**.
2.  Set the parent window.
3.  Set new window styles.
4.  Position the video window inside the owner window.
5.  Notify the video window of WM\_MOVE messages.

**Query for IVideoWindow**

Before starting playback, query the Filter Graph Manager for the **IVideoWindow** interface:


```C++
IVideoWindow *pVidWin = NULL;
pGraph->QueryInterface(IID_IVideoWindow, (void **)&pVidWin);
```



**Set the Parent Window**

To set the parent window, call the [**IVideoWindow::put\_Owner**](/windows/desktop/api/Control/nf-control-ivideowindow-put_owner) method with a handle to your application window. This method takes a variable of type [**OAHWND**](oahwnd.md), so cast the handle to this type:


```C++
pVidWin->put_Owner((OAHWND)hwnd);
```



**Set New Window Styles**

Change the style of the video window by calling the [**IVideoWindow::put\_WindowStyle**](/windows/desktop/api/Control/nf-control-ivideowindow-put_windowstyle) method:


```C++
pVidWin->put_WindowStyle(WS_CHILD | WS_CLIPSIBLINGS);
```



The WS\_CHILD flag sets the window to be a child window, and the WS\_CLIPSIBLINGS flag prevents the window from drawing inside the client area of another child window.

**Position the Video Window**

To set the position of the video relative to the application window's client area, call the [**IVideoWindow::SetWindowPosition**](/windows/desktop/api/Control/nf-control-ivideowindow-setwindowposition) method. This method takes a rectangle that specifies the left edge, top edge, width, and height of the video window. For example, the following code stretches the video window to fit the entire client area of the parent window:


```C++
RECT rc;
GetClientRect(hwnd, &rc);
pVidWin->SetWindowPosition(0, 0, rc.right, rc.bottom);
```



To get the native size of the video, call the [**IBasicVideo::GetVideoSize**](/windows/desktop/api/Control/nf-control-ibasicvideo-getvideosize) method on the Filter Graph Manager. You can use that information to scale the video and keep the correct aspect ratio.

**Respond to WM\_MOVE Messages**

For best performance, you should notify the video renderer whenever the window moves while the graph is paused. Call the [**IVideoWindow::NotifyOwnerMessage**](/windows/desktop/api/Control/nf-control-ivideowindow-notifyownermessage) method to forward the WM\_MOVE message:


```C++
// (Inside your WindowProc)
case WM_MOVE:
    pVidWin->NotifyOwnerMessage((OAHWND)hWnd, msg, wParam, lParam);
    break;
```



If the renderer is using a hardware overlay, this notification causes the renderer to update the overlay position. (The VMR-9 does not use overlays, so you do not need to call this method if you are using the VMR-9.)

**Clean Up**

Before the application exits, stop the graph and reset the video window's owner to **NULL**. Otherwise, window messages might be sent to the wrong window, which is likely to cause errors. Also, hide video window, or else you might see a video image flicker on the screen momentarily:


```C++
pControl->Stop(); 
pVidWin->put_Visible(OAFALSE);
pVidWin->put_Owner(NULL);  
```



> [!Note]  
> If the parent of the video window is a child of your main application window (in other words, if the video window is a child of a child), you should create the video window using **CoCreateInstance** and add it to the graph, instead of letting the Filter Graph Manager add the video renderer during [Intelligent Connect](intelligent-connect.md). This ensures that the video window and your child window are repainted at the same time. Otherwise, the child window may paint over the video window.

 

## Related topics

<dl> <dt>

[Video Rendering](video-rendering.md)
</dt> </dl>

 

 



