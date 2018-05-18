---
Description: Retrieving Events
ms.assetid: '18c5892d-7e33-497c-ab7d-d17fea5df17e'
title: Retrieving Events
---

# Retrieving Events

The Filter Graph Manager exposes three interfaces that support event notification.

-   [**IMediaEventSink**](imediaeventsink.md) contains the method for filters to post events.
-   [**IMediaEvent**](imediaevent.md) contains methods for applications to retrieve events.
-   [**IMediaEventEx**](imediaeventex.md) inherits from and extends the [**IMediaEvent**](imediaevent.md) interface.

Filters post event notifications by calling the [**IMediaEventSink::Notify**](imediaeventsink-notify.md) method on the Filter Graph Manager. An event notification consists of an event code, which defines the type of event, and two parameters that give additional information. Depending on the event code, the parameters might contain pointers, return codes, reference times, or other information. For a complete list of event codes and parameters, see [Event Notification Codes](event-notification-codes.md).

To retrieve an event from the queue, the application calls the [**IMediaEvent::GetEvent**](imediaevent-getevent.md) method on the Filter Graph Manager. This method blocks until there is an event to return or until a specified time elapses. Assuming there is a queued event, the method returns with the event code and the two event parameters. After calling **GetEvent**, an application should always call the [**IMediaEvent::FreeEventParams**](imediaevent-freeeventparams.md) method to release any resources associated with the event parameters. For example, a parameter might be a **BSTR** value that was allocated by the filter graph.

The following code example provides an outline of how to retrieve events from the queue.


```C++
long evCode;
LONG_PTR param1, param2;
HRESULT hr;
while (hr = pEvent->GetEvent(&amp;evCode, &amp;param1, &amp;param2, 0), SUCCEEDED(hr))
{
    switch(evCode) 
    { 
        // Call application-defined functions for each 
        // type of event that you want to handle.
    } 
    hr = pEvent->FreeEventParams(evCode, param1, param2);
}
```



To override the Filter Graph Manager's default handling for an event, call the [**IMediaEvent::CancelDefaultHandling**](imediaevent-canceldefaulthandling.md) method with the event code as a parameter. You can reinstate the default handling by calling the [**IMediaEvent::RestoreDefaultHandling**](imediaevent-restoredefaulthandling.md) method. If the filter graph performs no default handling for the specified event code, calling these methods has no effect.

## Related topics

<dl> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 



