---
description: Learning When an Event Occurs
ms.assetid: 4e44089b-676b-4220-9721-54ddf56bf760
title: Learning When an Event Occurs
ms.topic: article
ms.date: 05/31/2018
---

# Learning When an Event Occurs

To process DirectShow events, an application needs a way to find out when events are waiting in the queue. The Filter Graph Manager provides two ways to do this:

-   **Window notification:** The Filter Graph Manager sends a user-defined Windows message to an application window whenever there is a new event.
-   **Event signaling:** The Filter Graph Manager signals a Windows event if there are DirectShow events in the queue, and reset the event if the queue is empty.

An application can use either technique. Window notification is usually simpler.

**Window Notification**

To set up window notification, call the [**IMediaEventEx::SetNotifyWindow**](/windows/desktop/api/Control/nf-control-imediaeventex-setnotifywindow) method and specify a private message. Applications can use message numbers in the range from WM\_APP through 0xBFFF as private messages. Whenever the Filter Graph Manager places a new event notification in the queue, it posts this message to the designated window. The application responds to the message from within the window's message loop.

The following code example shows how to set the notification window.


```C++
#define WM_GRAPHNOTIFY WM_APP + 1   // Private message.
pEvent->SetNotifyWindow((OAHWND)g_hwnd, WM_GRAPHNOTIFY, 0);
```



The message is an ordinary Windows message, and is posted separately from the DirectShow event notification queue. The advantage of this approach is that most applications already implement a message loop. Therefore, you can incorporate DirectShow event handling without much additional work.

The following code example shows an outline of how to respond to the notification message. For a complete example, see [Responding to Events](responding-to-events.md).


```C++
LRESULT CALLBACK WindowProc( HWND hwnd, UINT msg, UINT wParam, LONG lParam)
{
    switch (msg)
    {
        case WM_GRAPHNOTIFY:
            HandleEvent();  // Application-defined function.
            break;
        // Handle other Windows messages here too.
    }
    return (DefWindowProc(hwnd, msg, wParam, lParam));
}
```



Because event notification and the message loop are both asynchronous, the queue might contain more than one event by the time your application responds to the message. Also, events can sometimes be cleared from the queue if they become invalid. Therefore, in your event handling code, call [**IAMMediaEvent::GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) until it returns a failure code, indicating that the queue is empty.

Before you release the [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) pointer, cancel event notification by calling [**SetNotifyWindow**](/windows/desktop/api/Control/nf-control-imediaeventex-setnotifywindow) with a **NULL** pointer. In your event processing code, check whether your **IMediaEventEx** pointer is valid before calling [**GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent). These steps prevent a possible error, in which the application receives the event notification after it has released the **IMediaEventEx** pointer.

**Event Signaling**

The Filter Graph Manager keeps a manual-reset event that reflects the state of the event queue. If the queue contains pending event notifications, the Filter Graph Manager signals the manual-reset event. If the queue is empty, a call to the [**IMediaEvent::GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) method resets the event. An application can use this event to determine the state of the queue.

> [!Note]  
> The terminology can be confusing here. The manual-reset event is the type of event created by the Windows [**CreateEvent**](/windows/win32/api/synchapi/nf-synchapi-createeventa) function; it has nothing to do with the events defined by DirectShow.

 

Call the [**IMediaEvent::GetEventHandle**](/windows/desktop/api/Control/nf-control-imediaevent-geteventhandle) method to get a handle to the manual-reset event. Wait for the event to be signaled by calling a function such as [**WaitForMultipleObjects**](/windows/win32/api/winuser/nf-winuser-msgwaitformultipleobjects). Once the event is signaled, call [**IMediaEvent::GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) to get the DirectShow event.

The following code example illustrates this approach. It gets the event handle, then waits in 100-millisecond intervals for the event to be signaled. If the event is signaled, it calls **GetEvent** and prints the event code and event parameters to the console window. The loop terminates when the [**EC\_COMPLETE**](ec-complete.md) event occurs, indicating that playback has completed.


```C++
HANDLE  hEvent; 
long    evCode, param1, param2;
BOOLEAN bDone = FALSE;
HRESULT hr = S_OK;
hr = pEvent->GetEventHandle((OAEVENT*)&hEvent);
if (FAILED(hr))
{
    /* Insert failure-handling code here. */
}

while(!bDone) 
{
    if (WAIT_OBJECT_0 == WaitForSingleObject(hEvent, 100))
    { 
        while (S_OK == pEvent->GetEvent(&evCode, &param1, &param2, 0)) 
        {
            printf("Event code: %#04x\n Params: %d, %d\n", evCode, param1, param2);
            pEvent->FreeEventParams(evCode, param1, param2);
            bDone = (EC_COMPLETE == evCode);
        }
    }
} 
```



Because the filter graph automatically sets or resets the event when appropriate, your application should not do so. Also, when you release the filter graph, the filter graph closes the event handle, so do not use the event handle after that point.

 

 
