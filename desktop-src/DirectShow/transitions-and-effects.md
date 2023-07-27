---
description: Transitions and Effects
ms.assetid: 2925c315-4488-4961-a8f7-77a9ac571b70
title: Transitions and Effects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Transitions and Effects

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

This section describes the effects and transitions provided with DirectShow Editing Services.



| Transition                              | Description                                                                            |
|-----------------------------------------|----------------------------------------------------------------------------------------|
| [Compositor](compositor-transition.md) | Stretches the foreground into a designated rectangle, without altering the background. |
| [Key](key-transition.md)               | Performs keying based on chroma, alpha, hue, or luminance.                             |
| [SMPTE Wipe](smpte-wipe-transition.md) | Performs the standard SMPTE wipes.                                                     |



 



| Effect                                        | Description                           |
|-----------------------------------------------|---------------------------------------|
| [Alpha Setter](alpha-setter-effect.md)       | Sets the alpha bits on a video image. |
| [Volume Envelope](volume-envelope-effect.md) | Sets the volume on an audio stream.   |



 



| Source Object                                | Description                                        |
|----------------------------------------------|----------------------------------------------------|
| [Video Color Source](video-color-source.md) | Creates a continuous video image of a solid color. |



 

## Related topics

<dl> <dt>

[DirectShow Editing Services C++ Reference](directshow-editing-services-c---reference.md)
</dt> </dl>

 

 



