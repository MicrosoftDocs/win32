---
description: This topic is step 7 of the tutorial Audio/Video Playback in DirectShow.
ms.assetid: 2e542a2d-fc71-41d5-9abd-0dfa70719c0f
title: 'Step 7: Transport Controls'
ms.topic: article
ms.date: 05/31/2018
---

# Step 7: Transport Controls

This topic is step 7 of the tutorial [Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md). The complete code is shown in the topic [DirectShow Playback Example](directshow-playback-example.md).

The last step is to add transport controls (play, pause, and stop). To play the file, call [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run).


```C++
HRESULT DShowPlayer::Play()
{
    if (m_state != STATE_PAUSED && m_state != STATE_STOPPED)
    {
        return VFW_E_WRONG_STATE;
    }

    HRESULT hr = m_pControl->Run();
    if (SUCCEEDED(hr))
    {
        m_state = STATE_RUNNING;
    }
    return hr;
}
```



To pause, call [**IMediaControl::Pause**](/windows/desktop/api/Control/nf-control-imediacontrol-pause).


```C++
HRESULT DShowPlayer::Pause()
{
    if (m_state != STATE_RUNNING)
    {
        return VFW_E_WRONG_STATE;
    }

    HRESULT hr = m_pControl->Pause();
    if (SUCCEEDED(hr))
    {
        m_state = STATE_PAUSED;
    }
    return hr;
}
```



To stop, call [**IMediaControl::Stop**](/windows/desktop/api/Control/nf-control-imediacontrol-stop).


```C++
HRESULT DShowPlayer::Stop()
{
    if (m_state != STATE_RUNNING && m_state != STATE_PAUSED)
    {
        return VFW_E_WRONG_STATE;
    }

    HRESULT hr = m_pControl->Stop();
    if (SUCCEEDED(hr))
    {
        m_state = STATE_STOPPED;
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md)
</dt> <dt>

[DirectShow Playback Example](directshow-playback-example.md)
</dt> <dt>

[Filter States](filter-states.md)
</dt> </dl>

 

 



