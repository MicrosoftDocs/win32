---
description: Volume Envelope Effect
ms.assetid: 17b6d842-e79c-49b0-baa4-1535b4a2c6ae
title: Volume Envelope Effect
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Volume Envelope Effect

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Volume Envelope effect sets the volume on an audio stream.

Class ID (CLSID): {036A9790-C153-11D2-9EF7-006008039E37}

CLSID Variable Name: CLSID\_AudMixer

Properties



| Property | Type   | Default | Description                                                                                                           |
|----------|--------|---------|-----------------------------------------------------------------------------------------------------------------------|
| Vol      | double | 1.0     | Volume, as a percentage of the authored volume. You can produce audio fades by varying this property value over time. |



 

## Remarks

Each object in a timeline can have at most one volume envelope effect. In a composition or a group, the volume envelope is applied first, before any other audio effects, regardless of its priority. In a source or a track, the volume effect is applied according to its priority.

 

 



