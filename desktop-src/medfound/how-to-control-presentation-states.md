---
Description: How to Control Presentation States
ms.assetid: 978373ef-b2a4-4035-b889-e28a037c0ab5
title: How to Control Presentation States
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Control Presentation States

The Media Session provides transport control such as changing presentation states (Play, Pause, and Stop in a playlist-style playback scenario). This topic describes Media Session methods that an application should call to change the playback state.

The following table shows the valid presentation state transitions.



| State transition | Description                                                                                |
|------------------|--------------------------------------------------------------------------------------------|
| Play -&gt; Pause | The presentation clock freezes.                                                            |
| Play -&gt; Stop  | The presentation clock is reset.                                                           |
| Pause -&gt; Play | The presentation clock resumes from the time it froze during the Play to Pause transition. |
| Pause -&gt; Stop | The presentation clock is reset.                                                           |
| Stop -&gt; Play  | The presentation clock starts from the beginning of the presentation.                      |
| Stop -&gt; Pause | Not allowed.                                                                               |



 

## To change presentation states

-   Call the [**IMFMediaSession::Pause**](/windows/win32/mfidl/nf-mfidl-imfmediasession-pause?branch=master) method to pause playback.

    ```C++
    hr = pMediaSession->Pause();
    ```

    

    Before calling this method, the application must call the [**IMFMediaSession::GetSessionCapabilities**](/windows/win32/mfidl/nf-mfidl-imfmediasession-getsessioncapabilities?branch=master) method to discover whether the media source supports the Pause state. If it does, this method returns **MFSESSIONCAP\_PAUSE** in the *pdwCaps* parameter.

    Pause temporarily stops the Media Session, the presentation clock, and the stream sink for the current presentation. After the call completes successfully, the application receives a [MESessionPaused](mesessionpaused.md) event.

-   Call the [**IMFMediaSession::Stop**](/windows/win32/mfidl/nf-mfidl-imfmediasession-stop?branch=master) method to stop playback.

    ```C++
    hr = pMediaSession->Stop();
    ```

    

    This method stops the Media Session by stopping the media source, the corresponding clocks, and stream sinks. If the Media Session is controlling the [Sequencer Source](sequencer-source.md), the underlying native sources are stopped by the sequencer source. After the Media Session is stopped, the application receives a [MESessionStopped](mesessionstopped.md) event.

-   Call the [**IMFMediaSession::Start**](/windows/win32/mfidl/nf-mfidl-imfmediasession-start?branch=master) method to start playback or seek to a new position.

    ```C++
    hr = pMediaSession->Start(NULL, &amp;var);
    ```

    

    This method starts the Media Session from Pause and Stop states. The Media Session is responsible for setting up the data flow in the pipeline. This method instructs the Media Session to start the presentation clock. After this call, Media Session sends a [MESessionStarted](mesessionstarted.md) event to the application.

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> </dl>

 

 



