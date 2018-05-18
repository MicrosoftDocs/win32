---
Description: Media Event Generators
ms.assetid: '2e003ad4-9fcb-4834-a335-e4969ffd3a00'
title: Media Event Generators
---

# Media Event Generators

Media Foundation provides a consistent way for objects to send events. An object can use events to signal the completion of an asynchronous method, or to notify the application about a change in the object's state.

If an object sends events, it exposes the [**IMFMediaEventGenerator**](imfmediaeventgenerator.md) interface. Whenever the object sends a new event, the event is placed in a queue. The application can request the next event from the queue by calling one of the following methods:

-   [**IMFMediaEventGenerator::GetEvent**](imfmediaeventgenerator-getevent.md)

-   [**IMFMediaEventGenerator::BeginGetEvent**](imfmediaeventgenerator-begingetevent.md)

The [**GetEvent**](imfmediaeventgenerator-getevent.md) method is synchronous. If an event is already in the queue, the method returns immediately. If there is no event in the queue, the method either fails immediately, or blocks until the next event is queued, depending on which flag you pass into **GetEvent**.

The [**BeginGetEvent**](imfmediaeventgenerator-begingetevent.md) method is asynchronous, so it never blocks. This method takes a pointer to the [**IMFAsyncCallback**](imfasynccallback.md) interface, which the application must implement. When the callback is invoked, the application calls [**IMFMediaEventGenerator::EndGetEvent**](imfmediaeventgenerator-endgetevent.md) to get the event from the queue. For more information about **IMFAsyncCallback**, see [Asynchronous Callback Methods](asynchronous-callback-methods.md).

Events are represented by the [**IMFMediaEvent**](imfmediaevent.md) interface. This interface has the following methods:

-   [**GetType**](imfmediaevent-gettype.md): Retrieves the event type. The event type indicates what happened to trigger the event.

-   [**GetStatus**](imfmediaevent-getstatus.md): Retrieves an **HRESULT** value, indicating whether the operation that triggered the event was successful. If an operation fails asynchronously, **GetStatus** returns a failure code.

-   [**GetValue**](imfmediaevent-getvalue.md): Retrieves a **PROPVARIANT** that contains event data. The event data depends on the event type. Some events do not have any data.

-   [**GetExtendedType**](imfmediaevent-getextendedtype.md): Retrieves a **GUID**. This method applies to the [MEExtendedType Event](meextendedtype.md), and provides a way to define custom events.

The [**IMFMediaEvent**](imfmediaevent.md) interface also inherits the [**IMFAttributes**](imfattributes.md) interface. Some events carry additional information as attributes.

For a list of event types and their associated data and attributes, see [Media Foundation Events](media-foundation-events.md).

## Implementing IMFMediaEventGenerator

If you are writing a plug-in component for Media Foundation, such as a custom media source or media sink, you might need to implement [**IMFMediaEventGenerator**](imfmediaeventgenerator.md). To make this easier, Media Foundation provides a helper object that implements an event queue. Create the event queue by calling the [**MFCreateEventQueue**](mfcreateeventqueue.md) function. The event queue exposes the [**IMFMediaEventQueue**](imfmediaeventqueue.md) interface. In your object's implementation of the **IMFMediaEventGenerator** methods, call the corresponding method on the event queue.

The event queue object is thread safe. Never hold the same critical section object when calling [**GetEvent**](imfmediaeventqueue-getevent.md) and [**QueueEvent**](imfmediaeventgenerator-queueevent.md), because **GetEvent** might block indefinitely waiting for [**QueueEvent**](imfmediaeventqueue-queueevent.md). If you hold the same critical section for both methods, it will cause a deadlock.

Before releasing the event queue, call [**IMFMediaEventQueue::Shutdown**](imfmediaeventqueue-shutdown.md) to release the resources that the object holds.

When your object needs to raise an event, call one of the following methods on the event queue:

-   [**IMFMediaEventQueue::QueueEvent**](imfmediaeventqueue-queueevent.md)

-   [**IMFMediaEventQueue::QueueEventParamVar**](imfmediaeventqueue-queueeventparamvar.md)

-   [**IMFMediaEventQueue::QueueEventParamUnk**](imfmediaeventqueue-queueeventparamunk.md)

These methods put a new event on the queue and signal any caller that is waiting for the next event.

The following code shows a class that implements [**IMFMediaEventGenerator**](imfmediaeventgenerator.md) using this helper object. This class defines a public **Shutdown** method that shuts down the event queue and releases the event queue pointer. This behavior would be typical for media sources and media sinks, which always have a **Shutdown** method.


```C++
class MyObject : public IMFMediaEventGenerator
{
private:
    long                m_nRefCount;    // Reference count.
    CRITICAL_SECTION    m_critSec;      // Critical section.
    IMFMediaEventQueue *m_pQueue;       // Event queue.
    BOOL                m_bShutdown;    // Is the object shut down?

    // CheckShutdown: Returns MF_E_SHUTDOWN if the object was shut down.
    HRESULT CheckShutdown() const 
    {
        return (m_bShutdown? MF_E_SHUTDOWN : S_OK);
    }

public:
    MyObject(HRESULT &amp;hr) : m_nRefCount(0), m_pQueue(NULL), m_bShutdown(FALSE)
    {
        InitializeCriticalSection(&amp;m_critSec);
        
        // Create the event queue.
        hr = MFCreateEventQueue(&amp;m_pQueue);
    }

    // Shutdown: Shuts down this object.
    HRESULT Shutdown()
    {
        EnterCriticalSection(&amp;m_critSec);

        HRESULT hr = CheckShutdown();
        if (SUCCEEDED(hr))
        {
            // Shut down the event queue.
            if (m_pQueue)
            {
                hr = m_pQueue->Shutdown();
            }

            // Release the event queue.
            SAFE_RELEASE(m_pQueue);
            // Release any other objects owned by the class (not shown).

            // Set the shutdown flag.
            m_bShutdown = TRUE;
        }

        LeaveCriticalSection(&amp;m_critSec);
        return hr;
    }

    // TODO: Implement IUnknown (not shown).
    STDMETHODIMP_(ULONG) AddRef();
    STDMETHODIMP_(ULONG) Release();
    STDMETHODIMP QueryInterface(REFIID iid, void** ppv);

    // IMFMediaEventGenerator::BeginGetEvent
    STDMETHODIMP BeginGetEvent(IMFAsyncCallback* pCallback, IUnknown* pState)
    {
        EnterCriticalSection(&amp;m_critSec);

        HRESULT hr = CheckShutdown();
        if (SUCCEEDED(hr))
        {
            hr = m_pQueue->BeginGetEvent(pCallback, pState);
        }

        LeaveCriticalSection(&amp;m_critSec);
        return hr;    
    }

    // IMFMediaEventGenerator::EndGetEvent
    STDMETHODIMP EndGetEvent(IMFAsyncResult* pResult, IMFMediaEvent** ppEvent)
    {
        EnterCriticalSection(&amp;m_critSec);

        HRESULT hr = CheckShutdown();
        if (SUCCEEDED(hr))
        {
            hr = m_pQueue->EndGetEvent(pResult, ppEvent);
        }

        LeaveCriticalSection(&amp;m_critSec);
        return hr;    
    }

    // IMFMediaEventGenerator::GetEvent
    STDMETHODIMP GetEvent(DWORD dwFlags, IMFMediaEvent** ppEvent)
    {
        // Because GetEvent can block indefinitely, it requires
        // a slightly different locking strategy.
        IMFMediaEventQueue *pQueue = NULL;

        // Hold lock.
        EnterCriticalSection(&amp;m_critSec);

        // Check shutdown
        HRESULT hr = CheckShutdown();

        // Store the pointer in a local variable, so that another thread
        // does not release it after we leave the critical section.
        if (SUCCEEDED(hr))
        {
            pQueue = m_pQueue;
            pQueue->AddRef();
        }

        // Release the lock.
        LeaveCriticalSection(&amp;m_critSec);

        if (SUCCEEDED(hr))
        {
            hr = pQueue->GetEvent(dwFlags, ppEvent);
        }

        SAFE_RELEASE(pQueue);
        return hr;
    }

    // IMFMediaEventGenerator::QueueEvent
    STDMETHODIMP QueueEvent(
        MediaEventType met, REFGUID extendedType, 
        HRESULT hrStatus, const PROPVARIANT* pvValue)
    {
        EnterCriticalSection(&amp;m_critSec);

        HRESULT hr = CheckShutdown();
        if (SUCCEEDED(hr))
        {
            hr = m_pQueue->QueueEventParamVar(
                met, extendedType, hrStatus, pvValue);
        }

        LeaveCriticalSection(&amp;m_critSec);
        return hr;
    }

private:

    // The destructor is private. The caller must call Release.
    virtual ~MyObject()
    {
        assert(m_bShutdown);
        assert(m_nRefCount == 0);
    }
};
```



## Related topics

<dl> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 



