---
description: DMO Interfaces
ms.assetid: 1362495b-1abb-41fd-b821-b51d8e32f137
title: DMO Interfaces
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMO Interfaces

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section contains reference entries for all the Microsoft DirectX Media Object (DMO) COM interfaces and their methods.



| Interface                                                            | Description                                                              |
|----------------------------------------------------------------------|--------------------------------------------------------------------------|
| [**IDMOQualityControl**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-idmoqualitycontrol)                     | Supports quality control on a DMO.                                       |
| [**IDMOVideoOutputOptimizations**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-idmovideooutputoptimizations) | Supports video optimizations on a DMO.                                   |
| [**IEnumDMO**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-ienumdmo)                                         | Provides methods for enumerating DMOs.                                   |
| [**IMediaBuffer**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediabuffer)                                 | Provides methods for manipulating a data buffer.                         |
| [**IMediaObject**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobject)                                 | Provides methods for manipulating a DMO.                                 |
| [**IMediaObjectInPlace**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobjectinplace)                   | Provides methods for processing data in place.                           |
| [**IMediaParamInfo**](/previous-versions/windows/desktop/api/Medparam/nn-medparam-imediaparaminfo)                           | Retrieves information about the media parameters that an object supports |
| [**IMediaParams**](/previous-versions/windows/desktop/api/Medparam/nn-medparam-imediaparams)                                 | Sets and retrieves media parameters on an object.                        |



 

## Related topics

<dl> <dt>

[DMO Reference](dmo-reference.md)
</dt> </dl>

 

 



