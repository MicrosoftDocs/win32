---
Description: This topic is step 4 of the tutorial How to Play Media Files with Media Foundation.
ms.assetid: fe5e852f-fe0c-439d-b0c5-d32593b587cb
title: Step 4 Create the Media Session
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
    hr = MFCreateMediaSession(NULL, &amp;m_pSession);
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
2.  Calls [**MFCreateMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatemediasession?branch=master) to create a new instance of the Media Session.
3.  Calls the [**IMFMediaEventGenerator::BeginGetEvent**](/windows/win32/mfobjects/nf-mfobjects-imfmediaeventgenerator-begingetevent?branch=master) method to request the next event from the Media Session. The first parameter to **BeginGetEvent** is a pointer to the **CPlayer** object itself, which implents the [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) interface.

Event handling is described in step 5.

Next: [Step 5: Handle Media Session Events](step-5--handle-media-session-events.md)

## Related topics

<dl> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> <dt>

[How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md)
</dt> </dl>

 

 



