---
description: This article describes how to respond to events that occur in a filter graph.
ms.assetid: 1c09149b-7f34-4296-bd32-dbbae5e1d62b
title: Responding to Events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Responding to Events

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This article describes how to respond to events that occur in a filter graph.

## How Event Notification Works

While a DirectShow application is running, events can occur within the filter graph. For example, a filter might encounter a streaming error. Filters alert the Filter Graph Manager by sending events, which consist of an event code and two event parameters. The event code indicates the type of event, and the event parameters supply additional information. The meaning of the parameters depends on the event code. For a complete list of event codes, see [Event Notification Codes](event-notification-codes.md).

Some events are handled silently by the Filter Graph Manager, without the application being notified. Other events are placed on a queue for the application. Depending on the application, there are various events that you might need to handle. This article focuses on three events that are very common:

-   The [**EC\_COMPLETE**](ec-complete.md) event indicates that playback has completed normally.
-   The [**EC\_USERABORT**](ec-userabort.md) event indicates that the user has interrupted playback. Video renderers send this event if the user closes the video window.
-   The [**EC\_ERRORABORT**](ec-errorabort.md) event indicates that an error has caused playback to halt.

## Using Event Notification

An application can instruct the Filter Graph Manager to send a Windows message to a designated window whenever a new event occurs. This enables the application to respond inside the window's message loop. First, define the message that will be sent to the application window. Applications can use message numbers in the range from WM\_APP through 0xBFFF as private messages:


```C++
#define WM_GRAPHNOTIFY  WM_APP + 1
```



Next, query the Filter Graph Manager for the [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) interface and call the [**IMediaEventEx::SetNotifyWindow**](/windows/desktop/api/Control/nf-control-imediaeventex-setnotifywindow) method:


```C++
IMediaEventEx *g_pEvent = NULL;
g_pGraph->QueryInterface(IID_IMediaEventEx, (void **)&g_pEvent);
g_pEvent->SetNotifyWindow((OAHWND)g_hwnd, WM_GRAPHNOTIFY, 0);
```



This method designates the specified window (g\_hwnd) as the recipient of the message. Call the method after you create the filter graph, but before running the graph.

WM\_GRAPHNOTIFY is an ordinary Windows message. Whenever the Filter Graph Manager puts a new event on the event queue, it posts a WM\_GRAPHNOTIFY message to the designated application window. The message's *lParam* parameter is equal to the third parameter in [**SetNotifyWindow**](/windows/desktop/api/Control/nf-control-imediaeventex-setnotifywindow). This parameter enables you to send instance data with the message. The window message's *wParam* parameter is always zero.

In your application's **WindowProc** function, add a case statement for the WM\_GRAPHNOTIFY message:


```C++
case WM_GRAPHNOTIFY:
    HandleGraphEvent();
    break;
```



In the event handler function, call the [**IMediaEvent::GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) method to retrieve events from the queue:


```C++
void HandleGraphEvent()
{
    // Disregard if we don't have an IMediaEventEx pointer.
    if (g_pEvent == NULL)
    {
        return;
    }
    // Get all the events
    long evCode;
    LONG_PTR param1, param2;
    HRESULT hr;
    while (SUCCEEDED(g_pEvent->GetEvent(&evCode, &param1, &param2, 0)))
    {
        g_pEvent->FreeEventParams(evCode, param1, param2);
        switch (evCode)
        {
        case EC_COMPLETE:  // Fall through.
        case EC_USERABORT: // Fall through.
        case EC_ERRORABORT:
            CleanUp();
            PostQuitMessage(0);
            return;
        }
    } 
}
```



The [**GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) method retrieves the event code and the two event parameters. The fourth **GetEvent** parameter specifies the length of time to wait for an event, in milliseconds. Because the application calls this method in response to a WM\_GRAPHNOTIFY message, the event is already queued. Therefore, we set the time-out value to zero.

Event notification and the message loop are both asynchronous, so the queue might hold more than one event by the time your application responds to the message. Also, the Filter Graph Manager can remove certain events from the queue, if they become invalid. Therefore, you should call [**GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) until it returns a failure code, indicating the queue is empty.

In this example, the application responds to [**EC\_COMPLETE**](ec-complete.md), [**EC\_USERABORT**](ec-userabort.md), and [**EC\_ERRORABORT**](ec-errorabort.md) by invoking the application-defined CleanUp function, which causes the application to quit gracefully. The example ignores the two event parameters. After you retrieve an event, call [**IMediaEvent::FreeEventParams**](/windows/desktop/api/Control/nf-control-imediaevent-freeeventparams) to any free resources associated with the event parameters.

Note that an [**EC\_COMPLETE**](ec-complete.md) event does not cause the filter graph to stop. The application can either stop or pause the graph. If you stop the graph, filters release any resources they are holding. If you pause the graph, filters continue to hold resources. Also, when a video renderer pauses, it displays a static image of the most recent frame.

Before you release the [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) pointer, cancel event notification by calling [**SetNotifyWindow**](/windows/desktop/api/Control/nf-control-imediaeventex-setnotifywindow) with a **NULL** window handle:


```C++
// Disable event notification before releasing the graph.
g_pEvent->SetNotifyWindow(NULL, 0, 0);
g_pEvent->Release();
g_pEvent = NULL;
```



In the WM\_GRAPHNOTIFY message handler, check the [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) pointer before calling [**GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent):


```C++
if (g_pEvent == NULL) return;
```



This prevents a possible error that can occur if the application receives the event notification after releasing the pointer.

## Related topics

<dl> <dt>

[Basic DirectShow Tasks](basic-directshow-tasks.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 



