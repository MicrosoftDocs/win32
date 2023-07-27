---
description: Frame Stepping Property Set
ms.assetid: 01abe1fe-fc2f-44cb-9546-45a8d682a179
title: Frame Stepping Property Set
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Frame Stepping Property Set

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Decoders that implement frame-accurate seeking under Microsoft DirectShow must implement the AM\_KSPROPSETID\_FrameStep property set, which is used in conjunction with the [**IVideoFrameStep**](/windows/desktop/api/Strmif/nn-strmif-ivideoframestep) interface.



| Label | Value |
|-------------------|----------------------------|
| Property Set GUID | AM\_KSPROPSETID\_FrameStep |



 



| Property ID                              | Description                                                                                                                                                                     |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AM\_PROPERTY\_FRAMESTEP\_STEP            | Instructs the decoder to begin a step operation and passes an [**AM\_PROPERTY\_FRAMESTEP**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-am_framestep_step) structure that specifies the number of steps.            |
| AM\_PROPERTY\_FRAMESTEP\_CANCEL          | Instructs the decoder to cancel the current step operation. No instance data is associated with this property.                                                                  |
| AM\_PROPERTY\_FRAMESTEP\_CANSTEP         | The decoder returns S\_OK on this instruction to indicate that it can perform frame stepping, S\_FALSE otherwise. No instance data is passed when this property is set.         |
| AM\_PROPERTY\_FRAMESTEP\_CANSTEPMULTIPLE | The decoder returns S\_OK on this instruction to indicate that it can step multiple frames at a time, S\_FALSE otherwise. No instance data is passed when this property is set. |



 

## Related topics

<dl> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 



