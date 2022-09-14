---
description: This topic is step 5 of the tutorial How to Play Media Files with Media Foundation.
ms.assetid: db9b896f-6f56-47b1-b129-331c984e0b16
title: 'Step 5: Handle Media Session Events'
ms.topic: article
ms.date: 05/31/2018
---

# Step 5: Handle Media Session Events

This topic is step 5 of the tutorial [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md). The complete code is shown in the topic [Media Session Playback Example](media-session-playback-example.md).

For background on this topic, read [Media Event Generators](media-event-generators.md). This topic contains the following sections:

-   [Getting Session Events](#getting-session-events)
-   [MESessionTopologyStatus](#mesessiontopologystatus)
-   [MEEndOfPresentation](#meendofpresentation)
-   [MENewPresentation](#menewpresentation)
-   [Related topics](#related-topics)

## Getting Session Events

To get events from the Media Session, the CPlayer object calls the [**IMFMediaEventGenerator::BeginGetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-begingetevent) method, as shown in [Step 4: Create the Media Session](step-4--create-the-media-session.md). This method is asynchronous, meaning it returns to the caller immediately. When the next session event occurs, the Media Session calls the [**IMFAsyncCallback::Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method of the CPlayer object.

It is important to remember that [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) gets called from a worker thread, not from the application thread. Therefore, the implementation of **Invoke** must be multithread-safe. One approach would be to protect the member data with a critical section. However, the `CPlayer` class shows an alternative approach:

1.  In the [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method, the CPlayer object posts a **WM\_APP\_PLAYER\_EVENT** message to the application. The message parameter is an [**IMFMediaEvent**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaevent) pointer.
2.  The application receives the **WM\_APP\_PLAYER\_EVENT** message.
3.  The application calls the `CPlayer::HandleEvent` method, passing in the [**IMFMediaEvent**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaevent) pointer.
4.  The `HandleEvent` method responds to the event.

The following code shows the [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method:


```C++
//  Callback for the asynchronous BeginGetEvent method.

HRESULT CPlayer::Invoke(IMFAsyncResult *pResult)
{
    MediaEventType meType = MEUnknown;  // Event type

    IMFMediaEvent *pEvent = NULL;

    // Get the event from the event queue.
    HRESULT hr = m_pSession->EndGetEvent(pResult, &pEvent);
    if (FAILED(hr))
    {
        goto done;
    }

    // Get the event type. 
    hr = pEvent->GetType(&meType);
    if (FAILED(hr))
    {
        goto done;
    }

    if (meType == MESessionClosed)
    {
        // The session was closed. 
        // The application is waiting on the m_hCloseEvent event handle. 
        SetEvent(m_hCloseEvent);
    }
    else
    {
        // For all other events, get the next event in the queue.
        hr = m_pSession->BeginGetEvent(this, NULL);
        if (FAILED(hr))
        {
            goto done;
        }
    }

    // Check the application state. 
        
    // If a call to IMFMediaSession::Close is pending, it means the 
    // application is waiting on the m_hCloseEvent event and
    // the application's message loop is blocked. 

    // Otherwise, post a private window message to the application. 

    if (m_state != Closing)
    {
        // Leave a reference count on the event.
        pEvent->AddRef();

        PostMessage(m_hwndEvent, WM_APP_PLAYER_EVENT, 
            (WPARAM)pEvent, (LPARAM)meType);
    }

done:
    SafeRelease(&pEvent);
    return S_OK;
}
```



The [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method performs the following steps:

1.  Call [**IMFMediaEventGenerator::EndGetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-endgetevent) to get the event. This method returns a pointer to the [**IMFMediaEvent**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaevent) interface.
2.  Call [**IMFMediaEvent::GetType**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-gettype) to get the event code.
3.  If the event code is [MESessionClosed](mesessionclosed.md), call SetEvent to set the *m\_hCloseEvent* event. The reason for this step is explained in [Step 7: Shut Down the Media Session](step-7--shut-down-the-media-session.md), and also in the code comments.
4.  For all other event codes, call [**IMFMediaEventGenerator::BeginGetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-begingetevent) to request the next event.
5.  Post a **WM\_APP\_PLAYER\_EVENT** message to the window.

The following code shows the HandleEvent method, which is called when the application receives the **WM\_APP\_PLAYER\_EVENT** message:


```C++
HRESULT CPlayer::HandleEvent(UINT_PTR pEventPtr)
{
    HRESULT hrStatus = S_OK;            
    MediaEventType meType = MEUnknown;  

    IMFMediaEvent *pEvent = (IMFMediaEvent*)pEventPtr;

    if (pEvent == NULL)
    {
        return E_POINTER;
    }

    // Get the event type.
    HRESULT hr = pEvent->GetType(&meType);
    if (FAILED(hr))
    {
        goto done;
    }

    // Get the event status. If the operation that triggered the event 
    // did not succeed, the status is a failure code.
    hr = pEvent->GetStatus(&hrStatus);

    // Check if the async operation succeeded.
    if (SUCCEEDED(hr) && FAILED(hrStatus)) 
    {
        hr = hrStatus;
    }
    if (FAILED(hr))
    {
        goto done;
    }

    switch(meType)
    {
    case MESessionTopologyStatus:
        hr = OnTopologyStatus(pEvent);
        break;

    case MEEndOfPresentation:
        hr = OnPresentationEnded(pEvent);
        break;

    case MENewPresentation:
        hr = OnNewPresentation(pEvent);
        break;

    default:
        hr = OnSessionEvent(pEvent, meType);
        break;
    }

done:
    SafeRelease(&pEvent);
    return hr;
}
```



This method calls [**IMFMediaEvent::GetType**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-gettype) to get the event type and [**IMFMediaEvent::GetStatus**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaevent-getstatus) to get the success of failure code associated with the event. The next action taken depends on the event code.

## MESessionTopologyStatus

The [MESessionTopologyStatus](mesessiontopologystatus.md) event signals a change in the status of the topology. The [**MF\_EVENT\_TOPOLOGY\_STATUS**](mf-event-topology-status-attribute.md) attribute of the event object contains the status. For this example, the only value of interest is **MF\_TOPOSTATUS\_READY**, which indicates that playback is ready to start.


```C++
HRESULT CPlayer::OnTopologyStatus(IMFMediaEvent *pEvent)
{
    UINT32 status; 

    HRESULT hr = pEvent->GetUINT32(MF_EVENT_TOPOLOGY_STATUS, &status);
    if (SUCCEEDED(hr) && (status == MF_TOPOSTATUS_READY))
    {
        SafeRelease(&m_pVideoDisplay);

        // Get the IMFVideoDisplayControl interface from EVR. This call is
        // expected to fail if the media file does not have a video stream.

        (void)MFGetService(m_pSession, MR_VIDEO_RENDER_SERVICE, 
            IID_PPV_ARGS(&m_pVideoDisplay));

        hr = StartPlayback();
    }
    return hr;
}
```



The `CPlayer::StartPlayback` method is shown in [Step 6: Control Playback](step-6--control-playback.md).

This example also calls [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) to get the [**IMFVideoDisplayControl**](/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol) interface from the [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR). This interface is needed to handle repainting and resizing the video window, also shown in [Step 6: Control Playback](step-6--control-playback.md).

## MEEndOfPresentation

The [MEEndOfPresentation](meendofpresentation.md) event signals that playback has reached the end of the file. The Media Session automatically switches back to the stopped state.


```C++
//  Handler for MEEndOfPresentation event.
HRESULT CPlayer::OnPresentationEnded(IMFMediaEvent *pEvent)
{
    // The session puts itself into the stopped state automatically.
    m_state = Stopped;
    return S_OK;
}
```



## MENewPresentation

The [MENewPresentation](menewpresentation.md) event signals the start of a new presentation. The event data is an [**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor) pointer for the new presentation.

In many cases, you will not receive this event at all. If you do, use the [**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor) pointer to create a new playback topology, as shown in [Step 3: Open a Media File](step-3--open-a-media-file.md). Then queue the new topology on the Media Session.


```C++
//  Handler for MENewPresentation event.
//
//  This event is sent if the media source has a new presentation, which 
//  requires a new topology. 

HRESULT CPlayer::OnNewPresentation(IMFMediaEvent *pEvent)
{
    IMFPresentationDescriptor *pPD = NULL;
    IMFTopology *pTopology = NULL;

    // Get the presentation descriptor from the event.
    HRESULT hr = GetEventObject(pEvent, &pPD);
    if (FAILED(hr))
    {
        goto done;
    }

    // Create a partial topology.
    hr = CreatePlaybackTopology(m_pSource, pPD,  m_hwndVideo,&pTopology);
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the topology on the media session.
    hr = m_pSession->SetTopology(0, pTopology);
    if (FAILED(hr))
    {
        goto done;
    }

    m_state = OpenPending;

done:
    SafeRelease(&pTopology);
    SafeRelease(&pPD);
    return S_OK;
}
```



Next: [Step 6: Control Playback](step-6--control-playback.md)

## Related topics

<dl> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> <dt>

[How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md)
</dt> </dl>

 

 



