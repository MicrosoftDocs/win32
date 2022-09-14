---
description: This topic is step 7 of the tutorial How to Play Media Files with Media Foundation.
ms.assetid: c31444df-8717-4ca8-a9ec-72cbb0ee4125
title: 'Step 7: Shut Down the Media Session'
ms.topic: article
ms.date: 05/31/2018
---

# Step 7: Shut Down the Media Session

This topic is step 7 of the tutorial [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md). The complete code is shown in the topic [Media Session Playback Example](media-session-playback-example.md).

To shut down the [Media Session](media-session.md), perform the following steps:

1.  Call [**IMFMediaSession::Close**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-close) to close the current presentation.
2.  Wait for the [MESessionClosed](mesessionclosed.md) event. This event is guaranteed to be the last event from the Media Session.
3.  Call [**IMFMediaSession::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-shutdown). This method causes the Media Sessions to release resources.
4.  Call [**IMFMediaSource::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown) on the current media source.

The following method shuts down the Media Session. It uses an event handle (*m\_hCloseEvent*) to wait for the [MESessionClosed](mesessionclosed.md) event. See [Step 5: Handle Media Session Events](step-5--handle-media-session-events.md).


```C++
//  Close the media session. 
HRESULT CPlayer::CloseSession()
{
    //  The IMFMediaSession::Close method is asynchronous, but the 
    //  CPlayer::CloseSession method waits on the MESessionClosed event.
    //  
    //  MESessionClosed is guaranteed to be the last event that the 
    //  media session fires.

    HRESULT hr = S_OK;

    SafeRelease(&m_pVideoDisplay);

    // First close the media session.
    if (m_pSession)
    {
        DWORD dwWaitResult = 0;

        m_state = Closing;
           
        hr = m_pSession->Close();
        // Wait for the close operation to complete
        if (SUCCEEDED(hr))
        {
            dwWaitResult = WaitForSingleObject(m_hCloseEvent, 5000);
            if (dwWaitResult == WAIT_TIMEOUT)
            {
                assert(FALSE);
            }
            // Now there will be no more events from this session.
        }
    }

    // Complete shutdown operations.
    if (SUCCEEDED(hr))
    {
        // Shut down the media source. (Synchronous operation, no events.)
        if (m_pSource)
        {
            (void)m_pSource->Shutdown();
        }
        // Shut down the media session. (Synchronous operation, no events.)
        if (m_pSession)
        {
            (void)m_pSession->Shutdown();
        }
    }

    SafeRelease(&m_pSource);
    SafeRelease(&m_pSession);
    m_state = Closed;
    return hr;
}
```



Before the application exits, shut down the Media Session, and then call [**MFShutdown**](/windows/desktop/api/mfapi/nf-mfapi-mfshutdown) to shut down the Microsoft Media Foundation platform.


```C++
//  Release all resources held by this object.
HRESULT CPlayer::Shutdown()
{
    // Close the session
    HRESULT hr = CloseSession();

    // Shutdown the Media Foundation platform
    MFShutdown();

    if (m_hCloseEvent)
    {
        CloseHandle(m_hCloseEvent);
        m_hCloseEvent = NULL;
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> <dt>

[How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md)
</dt> </dl>

 

 



