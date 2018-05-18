---
title: Receiving Spanning Events in the Stream Buffer Engine
description: Receiving Spanning Events in the Stream Buffer Engine
ms.assetid: '6799a507-7326-404a-af44-e1c9345617e3'
---

# Receiving Spanning Events in the Stream Buffer Engine

The Stream Buffer Engine (SBE) Version 2 (SBE2) introduces a new type of event called a spanning event. In contrast to traditional events, which are instantaneous, *spanning events* are stored as part of the content to make up part of the state of the content that follows.

For example, a recording may begin as unprotected content and then become protected midway through. A "protected" spanning event would replace the "unprotected" spanning event. As with a format change, a skip from one protection state to the other would cause a spanning event to be sourced.

Spanning events can be either global spanning events or in-band spanning events.

-   *Global spanning events* are events that contain information about a whole recording. An example of a global spanning event is the [**SBE2\_STREAM\_DESC**](sbe2-stream-desc.md) event, which describes the state of streams in the recording.
-   *In-band spanning events* are events sent with a particular stream. These events contain the information of that stream. An example of an in-band spanning event is **EVENTID\_LanguageSpanningEvent**, which indicates the language of an audio stream.

SBE2 implements the [**IBroadcastEventEx**](ibroadcasteventex.md) interface to broadcast spanning events. To receive spanning events, an object calls [**IBroadcastEventEx::FireEx**](ibroadcasteventex-fireex.md) with the GUID of the spanning event and with context information that uniquely identifies the event. A value of 0 for the third parameter to **FireEx** indicates that this event is a global spanning event. A stream ID value for the third parameter to **FireEx** indicates that the event is an in-band spanning event.

An application can use the [**ISBE2GlobalEvent**](isbe2globalevent.md) or [**ISBE2SpanningEvent**](isbe2spanningevent.md) interface (new in Windows 7) to get data from a global or in-band spanning event, respectively. Both global and in-band spanning events can be received from the [**IBroadcastEventEx**](ibroadcasteventex.md) interface..

Applications can also receive in-band spanning events by parsing media samples in a stream. The media sample for a spanning event does not contain any media data but carries the event data. To get the event data, query the sample for the [**IAttributeGet**](iattributeget.md) interface and call the [**IAttributeGet::GetAttrib**](iattributeget-getattrib.md) or [**IAttributeGet::GetAttribIndexed**](iattributeget-getattribindexed.md) method.

The example in the next section, "Registering a Broadcast Event Service" shows how to receive a spanning event that is broadcast by a [Broadcast Event Service](broadcast-service.md).

**Registering a Broadcast Event Service**

Before an application can receive global spanning events from the Stream Buffer Engine, it must establish a connection with the event service that broadcasts the events. If the filter graph already contains an event service, the application can query the [Filter Graph Manager](https://msdn.microsoft.com/library/windows/desktop/dd373399) to obtain a connection to that service. Otherwise, the application must create and register the event service.

In the following code example, the application first queries the [Filter Graph Manager](https://msdn.microsoft.com/library/windows/desktop/dd373399). If it does not find an event service, it creates and registers a new [**Broadcast Event Service**](broadcast-service.md) object for the service.


```C++
HRESULT HookupGraphEventService(IFilterGraph *pGraph)
{
    HRESULT hr = S_OK;
        CComQIPtr<IServiceProvider> spServiceProvider(pGraph);
        if (!spServiceProvider)
        {
            return E_NOINTERFACE;
        }
        hr = spServiceProvider->QueryService(SID_SBroadcastEventService, 
            IID_IBroadcastEventEx, 
            reinterpret_cast<void**>(&amp;spBroadcastEvent));
        if (FAILED(hr))
        {
            // Create the Broadcast Event Service object.
            hr = spBroadcastEvent.CoCreateInstance(
                CLSID_BroadcastEventService,
                NULL, CLSCTX_INPROC_SERVER);
            
            CComQIPtr<IRegisterServiceProvider> spRegService(pGraph);
            
            // Register the Broadcast Event Service object as a service.
            hr = spRegService->RegisterService(
                SID_SBroadcastEventService,
                spBroadcastEvent);
        }
    }
    return hr;
}
```



**Registering and Unregistering for Global Spanning Events**

Applications that receive global spanning events from the Stream Buffer Engine must explicitly register to receive these events. The following example shows how to register to receive global spanning events:


```C++
// Establish the connection point to receive events.
HRESULT RegisterForSBEGlobalEvents()
{
    CComQIPtr<IConnectionPoint> spConnectionPoint(spBroadcastEvent);
    HRESULT hr = spConnectionPoint->Advise(static_cast<IBroadcastEventEx*>(this),
        &amp;dwBroadcastEventCookie);
    return hr;
}
```



Similarly, when an application no longer wants to receive SBE global spanning events, it can "unregister" by releasing the connection point, as shown in the following example:


```C++
// Unregister for events.
HRESULT SBEGlobalEvent::UnRegisterForSBEGlobalEvents()
{
    HRESULT hr = S_OK;
    if(!m_dwBroadcastEventCookie)
    {
        return S_OK; // Not registered for events; nothing to do.
    }
    CComQIPtr<IConnectionPoint> spConnectionPoint(m_spBroadcastEvent);
    if(!spConnectionPoint)
    {
        return E_NOINTERFACE;
    }
    
    // Release the connection point.
    hr = spConnectionPoint->Unadvise(m_dwBroadcastEventCookie);
    if (FAILED(hr))
    {
        // Error: Unable to unadvise the connection point.
        return hr;
    }
    dwBroadcastEventCookie = 0;
    m_spBroadcastEvent.Release();
    return S_OK;
}
```



**Handling Global Spanning Events**

When the [Stream Buffer Source](stream-buffer-source-filter.md) filter raises a global spanning event by calling the [**IBroadcastEventEx::FireEx**](ibroadcasteventex-fireex.md) method, applications that handle that global spanning event call a handler method to acquire the event data and act on the event. The following code sample shows how an application might handle the [SBE2\_STREAM\_DESC\_EVENT](stream-buffer-engine-codes.md) event, which signals an update to one of the streams for a Stream Buffer Source filter:


```C++
// The one IBroadcastEventEx method.
STDMETHOD(FireEx)(GUID eventID, ULONG param1, ULONG param2, ULONG param3, ULONG param4)
{
     HRESULT hr = S_OK;
     // The one defined event.
     if (eventID == SBE2_STREAM_DESC_EVENT)
     {
         // A Stream description event.
         hr = HandleStreamDescEvent(eventID, param1, param2, param3, param4);
     }
     return hr;
}
```



The handler method queries the [**Stream Buffer Source**](stream-buffer-source-filter.md) filter to obtain a pointer to the [**ISBE2GlobalEvent**](isbe2globalevent.md) interface.

The handler then must perform the following actions:

1.  If the required buffer size is unknown, call the [**GetEvent**](isbe2globalevent-getevent.md) method by using the interface pointer to get the size of the buffer required to hold the event data. The **GetEvent** call passes **NULL** for the *pb* parameter to get the required buffer size, in bytes, in the *pcb* return parameter. If the required buffer size is known, that value can be passed as the value of the *pcb* parameter.
2.  Allocate the buffer that will hold the event data.
3.  Call [**GetEvent**](isbe2globalevent-getevent.md) again to return the actual event data in the buffer allocated in step 2.

The following example illustrates these steps:


```C++
// Handle Stream Desc Event
HRESULT HandleStreamDescEvent(GUID eventID, ULONG param1, ULONG param2,
                            ULONG param3, ULONG param4)
{
    HRESULT hr = S_OK;
    BOOL fSpanning = FALSE;

    CComQIPtr<ISBE2GlobalEvent> spSBE2GlobalEvent = spSBEFilter;
    DVR_STREAM_DESC* pStreamDesc = NULL;
    DWORD dwDescriptorSize = 0;
        
    // get size
    hr = spSBE2GlobalEvent->GetEvent(eventID,  param1, param2, param3, param4, 
                                &amp;fSpanning, &amp;dwDescriptorSize, NULL);

    pStreamDesc = (DVR_STREAM_DESC*) new BYTE [dwDescriptorSize];

    hr = spSBE2GlobalEvent->GetEvent(eventID,  param1, param2, param3, param4, 
                    &amp;fSpanning, &amp;dwDescriptorSize, reinterpret_cast<BYTE *> (pStreamDesc));
}
```



## Related topics

<dl> <dt>

[About the Filter Graph Manager](https://msdn.microsoft.com/library/windows/desktop/dd373399)
</dt> <dt>

[**Broadcast Event Service Object**](broadcast-service.md)
</dt> <dt>

[**IBroadcastEventEx**](ibroadcasteventex.md)
</dt> <dt>

[**IBroadcastEventEx::FireEx**](ibroadcasteventex-fireex.md)
</dt> <dt>

[**ISBE2GlobalEvent**](isbe2globalevent.md)
</dt> <dt>

[**ISBE2GlobalEvent::GetEvent**](isbe2globalevent-getevent.md)
</dt> </dl>

 

 




