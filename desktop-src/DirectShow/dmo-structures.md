---
description: DMO Structures
ms.assetid: 82c8ea74-1c5e-4370-9075-6db2ed6b2c91
title: DMO Structures
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMO Structures

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes the DirectX Media Object (DMO) structures.



| Structure                                                   | Description                                                 |
|-------------------------------------------------------------|-------------------------------------------------------------|
| [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type)                  | Describes the format of the data used by a stream in a DMO. |
| [**DMO\_OUTPUT\_DATA\_BUFFER**](/previous-versions/windows/desktop/api/Mediaobj/ns-mediaobj-dmo_output_data_buffer) | Describes an output buffer used by a DMO.                   |
| [**DMO\_PARTIAL\_MEDIATYPE**](/previous-versions/windows/desktop/api/Dmoreg/ns-dmoreg-dmo_partial_mediatype)    | Partially describes a media type used by a DMO.             |
| [**MP\_ENVELOPE\_SEGMENT**](/previous-versions/windows/desktop/api/Medparam/ns-medparam-mp_envelope_segment)        | Defines an envelope segment used by a media parameter.      |
| [**MP\_PARAMINFO**](/previous-versions/windows/desktop/api/Medparam/ns-medparam-mp_paraminfo)                       | Contains information about a media parameter.               |



 

## Related topics

<dl> <dt>

[DMO Reference](dmo-reference.md)
</dt> </dl>

 

 



