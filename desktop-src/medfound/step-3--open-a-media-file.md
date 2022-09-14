---
description: This topic is step 3 of the tutorial How to Play Media Files with Media Foundation.
ms.assetid: cc0d2b60-64d7-49f3-844f-97487cab8466
title: 'Step 3: Open a Media File'
ms.topic: article
ms.date: 05/31/2018
---

# Step 3: Open a Media File

This topic is step 3 of the tutorial [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md). The complete code is shown in the topic [Media Session Playback Example](media-session-playback-example.md).

The `CPlayer::OpenURL` method opens a media file from a URL.


```C++
//  Open a URL for playback.
HRESULT CPlayer::OpenURL(const WCHAR *sURL)
{
    // 1. Create a new media session.
    // 2. Create the media source.
    // 3. Create the topology.
    // 4. Queue the topology [asynchronous]
    // 5. Start playback [asynchronous - does not happen in this method.]

    IMFTopology *pTopology = NULL;
    IMFPresentationDescriptor* pSourcePD = NULL;

    // Create the media session.
    HRESULT hr = CreateSession();
    if (FAILED(hr))
    {
        goto done;
    }

    // Create the media source.
    hr = CreateMediaSource(sURL, &m_pSource);
    if (FAILED(hr))
    {
        goto done;
    }

    // Create the presentation descriptor for the media source.
    hr = m_pSource->CreatePresentationDescriptor(&pSourcePD);
    if (FAILED(hr))
    {
        goto done;
    }

    // Create a partial topology.
    hr = CreatePlaybackTopology(m_pSource, pSourcePD, m_hwndVideo, &pTopology);
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

    // If SetTopology succeeds, the media session will queue an 
    // MESessionTopologySet event.

done:
    if (FAILED(hr))
    {
        m_state = Closed;
    }

    SafeRelease(&pSourcePD);
    SafeRelease(&pTopology);
    return hr;
}
```



This method performs the following steps:

1.  Calls **CPlayer::CreateSession** to create a new instance of the Media Session. See [Step 4: Create the Media Session](step-4--create-the-media-session.md).
2.  Creates a media source from the URL. The complete code for this step is shown in the topic [Using the Source Resolver](using-the-source-resolver.md).
3.  Calls [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) to get the media source's presentation descriptor. The presentation descriptor describes each streams in the source file.
4.  Creates the playback topology. Code for this step is shown in the topic [Creating Playback Topologies](creating-playback-topologies.md).
5.  Calls [**IMFMediaSession::SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) to set the topology on the Media Session.

The [**SetTopology**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-settopology) method completes asynchronously. When it completes, the CPlayer object's [**IMFAsyncCallback::Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method is called; see [Step 5: Handle Media Session Events](step-5--handle-media-session-events.md).

Next: [Step 4: Create the Media Session](step-4--create-the-media-session.md)

## Related topics

<dl> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> <dt>

[How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md)
</dt> </dl>

 

 



