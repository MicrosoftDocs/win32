---
description: This topic is step 4 of the tutorial How to Play Media Files with Media Foundation.
ms.assetid: fe5e852f-fe0c-439d-b0c5-d32593b587cb
title: 'Step 4: Create the Media Session'
ms.topic: article
ms.date: 05/31/2018
---

# Step 4: Create the Media Session

This topic is step 4 of the tutorial [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md). The complete code is shown in the topic [Media Session Playback Example](media-session-playback-example.md).

The `CPlayer::CreateSession` creates a new instance of the Media Session.


```C++
//  Create a new instance of the media session.
HRESULT CPlayer::CreateSession()
{
    // Close the old session, if any.
    HRESULT hr = CloseSession();
    if (FAILED(hr))
    {
        goto done;
    }

    assert(m_state == Closed);

    // Create the media session.
    hr = MFCreateMediaSession(NULL, &m_pSession);
    if (FAILED(hr))
    {
        goto done;
    }

    // Start pulling events from the media session
    hr = m_pSession->BeginGetEvent((IMFAsyncCallback*)this, NULL);
    if (FAILED(hr))
    {
        goto done;
    }

    m_state = Ready;

done:
    return hr;
}
```



This method performs the following steps:

1.  Calls `CPlayer::CloseSession` to close any previous instance of the Media Session.
2.  Calls [**MFCreateMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatemediasession) to create a new instance of the Media Session.
3.  Calls the [**IMFMediaEventGenerator::BeginGetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-begingetevent) method to request the next event from the Media Session. The first parameter to **BeginGetEvent** is a pointer to the **CPlayer** object itself, which implents the [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) interface.

Event handling is described in step 5.

Next: [Step 5: Handle Media Session Events](step-5--handle-media-session-events.md)

## Related topics

<dl> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> <dt>

[How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md)
</dt> </dl>

 

 



