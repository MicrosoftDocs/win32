---
description: Audio Capture
ms.assetid: 2b7fbdcb-7b59-407e-8e82-e66bd5606507
title: Audio Capture
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio Capture

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

An application can use DirectShow to capture audio data from microphones, tape players, and other devices, through the inputs on the sound card. Typical scenarios include:

-   Recording a voiceover narration for later dubbing over a video stream.
-   Converting legacy analog audio content to digital format.
-   Capturing voice or music for transmission over a network.

End users have several options for capturing audio from the sound card to the hard disk. Most cards provide applications for mixing and recording from their audio inputs. Windows provides Sound Recorder, a simple utility application for recording from a microphone. The Windows Media Encoder can be incorporated into a DirectShow application as a [DirectX Media Object](directx-media-objects.md) (DMO). This section describes how to integrate audio capture functionality within your own application using DirectShow.

This section contains the following topics:

-   [About the Audio Capture Filter](about-the-audio-capture-filter.md)
-   [Selecting a Capture Device](selecting-a-capture-device.md)
-   [Creating an Audio Capture Graph](creating-an-audio-capture-graph.md)
-   [Creating an Audio Capture Graph with Preview](creating-an-audio-capture-graph-with-preview.md)
-   [Setting Audio Capture Properties](setting-audio-capture-properties.md)

## Related topics

<dl> <dt>

[Using DirectShow](using-directshow.md)
</dt> </dl>

 

 



